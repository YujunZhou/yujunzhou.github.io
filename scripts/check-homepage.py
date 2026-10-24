"""Browser acceptance checks for the static homepage. Requires Playwright + Chrome.
Run with the local preview server at http://127.0.0.1:8765.
"""
import json
import os
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'docs/redesign-2026-10-23/after'
BASE = os.environ.get('PREVIEW_URL', 'http://127.0.0.1:8765')
OUT.mkdir(parents=True, exist_ok=True)
results = []
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=os.environ.get('CHROME_PATH', '/usr/bin/google-chrome'), headless=True, args=['--no-sandbox'])
    for width, height in [(1440, 1000), (390, 844), (320, 740)]:
        page = browser.new_page(viewport={'width': width, 'height': height}, device_scale_factor=1, reduced_motion='reduce')
        errors, failures = [], []
        page.on('pageerror', lambda error: errors.append(str(error)))
        page.on('response', lambda response: failures.append(f'{response.status} {response.url}') if response.status >= 400 else None)
        page.goto(BASE, wait_until='networkidle')
        page.evaluate('document.fonts.ready')
        # Load all lazy images before capturing and checking their dimensions.
        page.locator('main img').evaluate_all("images => images.forEach(i => i.loading = 'eager')")
        page.wait_for_function('Array.from(document.querySelectorAll("main img")).every(i => i.complete && i.naturalWidth > 0)')
        # Decode and paint after scrolling; complete/naturalWidth alone do not
        # guarantee off-screen async images are painted in a full-page capture.
        for img in page.locator('main img').all():
            img.scroll_into_view_if_needed()
            img.evaluate('image => image.decode()')
        page.evaluate("document.querySelectorAll('img').forEach(i => i.decoding = 'sync')")
        page.evaluate('scrollTo({top: 0, behavior: \"instant\"})')
        page.wait_for_timeout(200)
        page.screenshot(path=str(OUT / f'local-{width}-viewport.png'))
        page.screenshot(path=str(OUT / f'local-{width}-full.png'), full_page=True)
        for selector, name in [('#research', 'research'), ('#news', 'news')]:
            page.locator(selector).screenshot(path=str(OUT / f'local-{width}-{name}.png'))
        size = page.evaluate('({viewport: innerWidth, page: document.documentElement.scrollWidth})')
        overflow = page.locator('body *').evaluate_all('''elements => elements.filter(e => {
          const r = e.getBoundingClientRect();
          return r.width && (r.right > innerWidth + 1 || r.left < -1) && !e.matches('.skip-link');
        }).map(e => ({tag:e.tagName, class:e.className, text:e.textContent.slice(0,60)}))''')
        assert size['page'] <= width, (width, size)
        assert not overflow, (width, overflow)
        assert not errors and not failures, (errors, failures)
        assert page.locator('.research-item').count() == 8
        assert page.locator('.publication').count() == 12
        assert page.locator('.news-section > .news-list > li').count() == 5
        assert page.locator('.earlier-updates li').count() == 13
        assert page.locator('.contact-links a').all_text_contents() == ['CV ↗', 'Email', 'Google Scholar', 'GitHub', 'LinkedIn']
        details = page.locator('.earlier-updates')
        summary = details.locator('summary')
        assert not details.evaluate('e => e.open')
        summary.focus()
        page.keyboard.press('Enter')
        assert details.evaluate('e => e.open')
        assert details.locator('.when-open').is_visible()
        assert details.locator('li').first.is_visible()
        page.screenshot(path=str(OUT / f'local-{width}-news-expanded.png'), full_page=True)
        page.keyboard.press('Space')
        assert not details.evaluate('e => e.open')
        assert details.locator('.when-closed').is_visible()
        author_details = page.locator('.author-details')
        author_details.locator('summary').focus()
        page.keyboard.press('Enter')
        assert author_details.evaluate('e => e.open')
        assert author_details.locator('.authors').is_visible()
        author_details.locator('summary').press('Enter')
        anchors = page.locator('a[href^="#"]').evaluate_all('as => as.map(a => a.getAttribute("href"))')
        for href in anchors:
            assert page.locator(href).count() == 1, href
        images = page.locator('.research-figure img').evaluate_all('''images => images.map(i => ({src:i.getAttribute('src'), width:i.clientWidth, height:i.clientHeight, naturalWidth:i.naturalWidth, naturalHeight:i.naturalHeight}))''')
        for image in images:
            assert abs(image['width'] / image['height'] - image['naturalWidth'] / image['naturalHeight']) < .04, image
        # The figure viewer keeps transparent figures on white, supports real-size
        # inspection, and returns keyboard focus to the activating link on Escape.
        link = page.locator('article[aria-labelledby="paper-4"] .figure-link')
        link.focus()
        page.keyboard.press('Enter')
        dialog = page.locator('.figure-dialog')
        assert dialog.is_visible()
        dialog.locator('img').evaluate('e => e.decode()')
        assert dialog.locator('img').get_attribute('alt')
        assert page.locator('.figure-close').evaluate('e => e === document.activeElement')
        dialog.screenshot(path=str(OUT / f'local-{width}-figure-viewer.png'))
        zoom = page.locator('.figure-zoom')
        zoom.click()
        assert zoom.get_attribute('aria-pressed') == 'true'
        assert page.locator('.figure-stage').evaluate('e => e.scrollWidth > e.clientWidth')
        assert page.evaluate('document.documentElement.scrollWidth') == width
        page.keyboard.press('Escape')
        assert not dialog.is_visible()
        assert link.evaluate('e => e === document.activeElement')
        page.wait_for_function("!document.body.classList.contains('figure-open')")
        # No JS dependency: content and disclosure remain accessible with scripts disabled.
        results.append(dict(width=width,height=height,dimensions=size,overflow=overflow,errors=errors,failed_responses=failures,keyboard_disclosures='Enter opens; Space closes',images=images))
        page.close()
    page = browser.new_page(java_script_enabled=False)
    page.goto(BASE)
    page.locator('.earlier-updates summary').click()
    assert page.locator('.earlier-updates li').first.is_visible()
    assert page.locator('h1').inner_text().startswith('Yujun Zhou')
    browser.close()
(OUT / 'browser-checks.json').write_text(json.dumps(results, indent=2))
print(json.dumps(results, indent=2))
