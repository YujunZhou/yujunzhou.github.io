---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I am a third-year(2023 Spring-now) Ph.D student in [Mine Lab](https://mine-lab-nd.github.io/) in Computer Science at [University of Notre Dame](https://www.nd.edu/), advised by [Prof. Xiangliang Zhang](https://sites.nd.edu/xiangliang-zhang/). I’m also a graduate student in [Foundation Models and Applications Lab (FMAL)](https://lucyinstitute.nd.edu/centers-and-labs/foundation-models-and-applications-lab-fmal/) at [Lucy Family Institute for Data & Society](https://lucyinstitute.nd.edu/). Before this, I received my B.E. degree in Computer Science and Engineering at the [University of Electronic Science and Technology of China (UESTC)](https://en.uestc.edu.cn/) and my M.S degree in Computer Science at [King Abdullah University of Science and Technology (KAUST)](https://www.kaust.edu.sa/en).


I am deeply interested in Large Language Model (LLM) Reasoning and trustworthy LLMs. I aim to understand how LLMs reason, where their reasoning fails, and how to enhance their ability to generalize beyond seen problems. In parallel, I study how to make LLMs more reliable, safe, and aligned when applied to safety-critical contexts. Also, I am engaged in [ND-IBM Tech Ethics Lab Collaborative Project](https://ethics.nd.edu/labs-and-centers/notre-dame-ibm-technology-ethics-lab/), where I explore ways to extend the trustworthiness of LLMs to practical domains such as laboratory safety and investigate the misalignment behaviors.

<blockquote style="font-size: 16px; line-height: 1.6;">
    I am seeking potential research collaborations and the position of industry research intern. If you are interested, please <a href="mailto:yzhou25@nd.edu">contact me</a>.
</blockquote>


# 🔥 News
- *2024.08*: &nbsp; One first-author paper has been accepted by EMNLP Findings 2025!
- *2025.08*: &nbsp; I’m excited to share that I have extended my internship at Tencent AI Lab！
- *2025.05*: &nbsp; I joined Tencent AI Lab as a research intern this summer! See you in Seattle！
- *2025.05*: &nbsp; One Paper is accepted by ACL Findings 2025!
- *2025.04*: &nbsp; One Paper is accepted by IJCAI 2025 Survey Track!
- *2025.01*: &nbsp; Thrilled to be awarded OpenAI’s Researcher Access Program.
- *2024.09*: &nbsp; One first-author paper has been accepted by EMNLP 2024!
- *2024.09*: &nbsp; One paper has been accepted by NeurIPS 2024 Dataset and Benchmark Track as a spotlight!
- *2024.05*: &nbsp; One Paper is accepted by ACL 2024!
- *2024.05*: &nbsp; One first-author paper has been accepted by ICML 2024!
- *2022.12*: &nbsp; One Paper is accepted by AAAI 2023!
- *2022.10*: &nbsp; One Paper is accepted by BigData 2022!
- *2022.01*: &nbsp; One paper is accepted by ICLR 2022!

# 📝 Selected Publications 

See more publications in my [Google Scholar](https://scholar.google.com/citations?user=t0c7rQQAAAAJ&hl=en)

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv Preprint</div><img src='images/evol-rl.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![Arxiv Preprint](https://img.shields.io/badge/Arxiv-Preprint-b4d723) [Evolving Language Models without Labels: Majority Drives Selection, Novelty Promotes Variation](https://arxiv.org/abs/2509.15194)

**Yujun Zhou**&#42;, Zhenwen Liang&#42;, Haolin Liu, Wenhao Yu, Kishan Panaganti, Linfeng Song, Dian Yu, Xiangliang Zhang, Haitao Mi, Dong Yu

[**Code**](https://github.com/YujunZhou/EVOL-RL)

[**Huggingface Models**](https://huggingface.co/collections/yujunzhou/evol-rl-68d8f3f7e2fadab49d6c3b9b)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP Findings 2025</div><img src='images/finelogic.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![EMNLP Findings 2025](https://img.shields.io/badge/EMNLP(Findings)-2025-e87223) [Dissecting Logical Reasoning in LLMs: A Fine-Grained Evaluation and Supervision Study](https://arxiv.org/abs/2506.04810)

**Yujun Zhou**&#42;, Jiayi Ye&#42;, Zipeng Ling&#42;, Yufei Han, Yue Huang, Haomin Zhuang, Zhenwen Liang, Kehan Guo, Taicheng Guo, Xiangqi Wang, Xiangliang Zhang

[**Code**](https://github.com/YujunZhou/FineLogic)

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2024</div><img src='images/ICAG.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![EMNLP 2024](https://img.shields.io/badge/EMNLP-2024-e87213) [Defending Jailbreak Prompts via In-Context Adversarial Game](https://arxiv.org/abs/2402.13148)

**Yujun Zhou**, Yufei Han, Haomin Zhuang, Taicheng Guo, Kehan Guo, Zhenwen Liang, Hongyan Bao, and Xiangliang Zhang

[**Code**](https://github.com/YujunZhou/In-Context-Adversarial-Game)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2024</div><img src='images/IGSG.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

![ICML 2024](https://img.shields.io/badge/ICML-2024-A84111) [Attack-free Evaluating and Enhancing Adversarial Robustness on Categorical Data](https://openreview.net/pdf?id=8ERo4jph0A)

**Yujun Zhou***, Yufei Han*, Haomin Zhuang, Hongyan Bao, Xiangliang Zhang

[**Code**](https://github.com/YujunZhou/IGSG)

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv Preprint</div><img src='images/labsafety.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
![Arxiv Preprint](https://img.shields.io/badge/Arxiv-Preprint-b4d723) [LabSafety Bench: Benchmarking LLMs on Safety Issues in Scientific Labs](https://yujunzhou.github.io/LabSafetyBench.github.io/), **Yujun Zhou**, Jingdong Yang, Yue Huang, Kehan Guo, Zoe Emory, Bikram Ghosh, Amita Bedar, Sujay Shekar, Pin-Yu Chen, Tian Gao, Werner Geyer, Nuno Moniz, Nitesh V Chawla, Xiangliang Zhang
  
[**Code**](https://github.com/YujunZhou/LabSafety-Bench)

[**Dataset**](https://huggingface.co/datasets/yujunzhou/LabSafety_Bench)

</div>
</div>

- ![Arxiv Preprint](https://img.shields.io/badge/Arxiv-Preprint-b4d723) [On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective](https://arxiv.org/abs/2502.14296), Yue Huang, Chujie Gao, Siyuan Wu, Haoran Wang, Xiangqi Wang, **Yujun Zhou**, Yanbo Wang, Jiayi Ye, Jiawen Shi, Qihui Zhang, Yuan Li, Han Bao, Zhaoyi Liu, Tianrui Guan, Dongping Chen, Ruoxi Chen, Kehan Guo, Andy Zou, Bryan Hooi Kuen-Yew, Caiming Xiong, Elias Stengel-Eskin, Hongyang Zhang, Hongzhi Yin, Huan Zhang, Huaxiu Yao, Jaehong Yoon, Jieyu Zhang, Kai Shu, Kaijie Zhu, Ranjay Krishna, Swabha Swayamdipta, Taiwei Shi, Weijia Shi, Xiang Li, Yiwei Li, Yuexing Hao, Zhihao Jia, Zhize Li, Xiuying Chen, Zhengzhong Tu, Xiyang Hu, Tianyi Zhou, Jieyu Zhao, Lichao Sun, Furong Huang, Or Cohen Sasson, Prasanna Sattigeri, Anka Reuel, Max Lamparth, Yue Zhao, Nouha Dziri, Yu Su, Huan Sun, Heng Ji, Chaowei Xiao, Mohit Bansal, Nitesh V Chawla, Jian Pei, Jianfeng Gao, Michael Backes, Philip S Yu, Neil Zhenqiang Gong, Pin-Yu Chen, Bo Li, Xiangliang Zhang
- ![NeurIPS 2024 Spotlight](https://img.shields.io/badge/NeurIPS-2024-2024) [Can LLMs Solve Molecule Puzzles? A Multimodal Benchmark for Molecular Structure Elucidation](https://kehanguo2.github.io/Molpuzzle.io/), Kehan Guo, Bozhao Nan, **Yujun Zhou**, Taicheng Guo, Zhichun Guo, Mihir Surve, Zhenwen Liang, Nitesh V. Chawla, Olaf Wiest, Xiangliang Zhang
- ![Arxiv Preprint](https://img.shields.io/badge/Arxiv-Preprint-b4d723) [Social Science Meets LLMs: How Reliable Are Large Language Models in Social Simulations?](https://arxiv.org/abs/2410.23426), Yue Huang*, Zhengqing Yuan*, **Yujun Zhou***, Kehan Guo, Xiangqi Wang, Haomin Zhuang, Weixiang Sun, Lichao Sun, Jindong Wang, Yanfang Ye, Xiangliang Zhang
- ![Arxiv Preprint](https://img.shields.io/badge/Arxiv-Preprint-b4d723) [Position: We Need An Adaptive Interpretation of Helpful, Honest, and Harmless Principles](https://arxiv.org/abs/2502.06059), Yue Huang, Chujie Gao, **Yujun Zhou**, Kehan Guo, Xiangqi Wang, Or Cohen-Sasson, Max Lamparth, Xiangliang Zhang
- ![Arxiv Preprint](https://img.shields.io/badge/Arxiv-Preprint-b4d723) [Beyond Single-Value Metrics: Evaluating and Enhancing LLM Unlearning with Cognitive Diagnosis](https://arxiv.org/abs/2502.13996), Yicheng Lang, Kehan Guo, Yue Huang, **Yujun Zhou**, Haomin Zhuang, Tianyu Yang, Yao Su, Xiangliang Zhang
- ![Arxiv Preprint](https://img.shields.io/badge/Arxiv-Preprint-b4d723) [Artificial Intelligence in Spectroscopy: Advancing Chemistry from Prediction to Generation and Beyond](https://arxiv.org/abs/2502.09897), Kehan Guo, Yili Shen, Gisela Abigail Gonzalez-Montiel, Yue Huang, **Yujun Zhou**, Mihir Surve, Zhichun Guo, Prayel Das, Nitesh V Chawla, Olaf Wiest, Xiangliang Zhang
- ![ACL 2024](https://img.shields.io/badge/ACL-2024-A27D46) [SceMQA: A Scientific College Entrance Level Multimodal Question Answering Benchmark](https://scemqa.github.io/), Zhenwen Liang, Kehan Guo, Gang Liu, Taicheng Guo, **Yujun Zhou**, Tianyu Yang, Jiajun Jiao, Renjie Pi, Jipeng Zhang, Xiangliang Zhang
- ![AAAI 2023](https://img.shields.io/badge/AAAI-2023-f3d6a3)[Towards efficient and domain-agnostic evasion attack with high-dimensional categorical inputs](https://ojs.aaai.org/index.php/AAAI/article/download/25828/25600), Hongyan Bao, Yufei Han, **Yujun Zhou**, Xin Gao, Xiangliang Zhang
- ![ICLR 2022](https://img.shields.io/badge/ICLR-2022-d7a2b3) [Towards understanding the robustness against evasion attack on categorical data](https://openreview.net/pdf?id=BmJV7kyAmg), Hongyan Bao, Yufei Han, **Yujun Zhou**, Yun Shen, Xiangliang Zhang

<!--# 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. -->

# 📖 Educations
- *2023.01 - Present*, Ph.D, <img src='images/Notre_Dame.png' style='width: 1.2em;'> [University of Notre Dame](https://www.nd.edu/)  
- *2021.09 - 2022.12*, M.S,  <img src='images/kaust.png' style='width: 1.2em;'> [King Abdullah University of Science and Technology](https://www.kaust.edu.sa/en)
- *2017.09 - 2021.06*, B.Eng,  <img src='images/uestc.png' style='width: 1.2em;'> [University of Electronic Science and Technology of China](https://en.uestc.edu.cn/)


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Map Widget</title>
    <style>
        .map-container {
            width: 300px; 
            margin: 0 auto; 
            text-align: center; 
        }
        .map-container iframe {
            width: 100%; 
            height: 300px; 
        }
    </style>
</head>
<body>
    <div class="map-container">
<script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=23pIdJVhMjN_8WNUnKTi-FQTV-hOMyUeuluWO9V4xPc&cl=ffffff&w=a"></script>
    </div>
</body>
</html>


<!--# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)-->

<!--# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.-->
