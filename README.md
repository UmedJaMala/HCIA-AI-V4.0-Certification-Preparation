# Huawei Certified ICT Associate - Artificial Intelligence (HCIA-AI V4.0)
### Complete Certification Preparation Suite · Verified Pearson VUE Recalls · 900-Question Master Bank · Interactive CBT Simulator

<p align="left">
  <a href="https://e.huawei.com/en/talent/#/cert/product-details?target=qualification&badgeId=0&qualificationId=399"><img src="https://img.shields.io/badge/Certification-Huawei_HCIA--AI_V4.0-1F2937?style=flat&logo=huawei&logoColor=EF4444" alt="Certification: Huawei HCIA-AI V4.0" /></a>
  <a href="https://e.huawei.com/en/talent/"><img src="https://img.shields.io/badge/Exam_Code-H13--311_V4.0-1F2937?style=flat&logo=target&logoColor=38BDF8" alt="Exam Code: H13-311" /></a>
  <a href="./01_Official_Huawei_Materials/"><img src="https://img.shields.io/badge/Official_Courseware-473_Slides-1F2937?style=flat&logo=bookstack&logoColor=10B981" alt="Official Slides: 473 Slides" /></a>
  <a href="./02_Verified_Exam_Recalls/"><img src="https://img.shields.io/badge/Verified_Recalls-41Q_&_60Q-1F2937?style=flat&logo=gitbook&logoColor=F59E0B" alt="Verified Recalls: 41Q & 60Q" /></a>
  <a href="#simulator"><img src="https://img.shields.io/badge/Exam_Simulator-Pearson_VUE_CBT-1F2937?style=flat&logo=terminal&logoColor=10B981" alt="Exam Simulator" /></a>
  <a href="./04_AI_Generated_Summaries_Archive/"><img src="https://img.shields.io/badge/Question_Bank-900_Items-1F2937?style=flat&logo=gitbook&logoColor=38BDF8" alt="Question Bank: 900 Items" /></a>
  <a href="./05_Hands_on_Labs/"><img src="https://img.shields.io/badge/GullNas_Vision-PyTorch_ResNet50-1F2937?style=flat&logo=pytorch&logoColor=EE4C2C" alt="GullNas Vision: PyTorch ResNet50" /></a>
  <a href="https://github.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/releases"><img src="https://img.shields.io/badge/Release-v1.3.0-1F2937?style=flat&logo=git&logoColor=A855F7" alt="Release: v1.3.0" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-1F2937?style=flat&logo=opensourceinitiative&logoColor=94A3B8" alt="License: MIT" /></a>
</p>

<p align="left">
  <a href="#simulator"><img src="https://img.shields.io/badge/Exam_Simulator-10B981?style=flat&logo=terminal&logoColor=white" alt="Exam Simulator" /></a>
  <a href="#overview"><img src="https://img.shields.io/badge/Overview-21262D?style=flat" alt="Overview" /></a>
  <a href="#structure"><img src="https://img.shields.io/badge/Structure-21262D?style=flat" alt="Structure" /></a>
  <a href="#official"><img src="https://img.shields.io/badge/01._Official_Courseware-21262D?style=flat" alt="Official Courseware" /></a>
  <a href="#recalls"><img src="https://img.shields.io/badge/02._Verified_Recalls-21262D?style=flat" alt="Verified Recalls" /></a>
  <a href="#practice-archive"><img src="https://img.shields.io/badge/03._Question_Banks_&_Code-21262D?style=flat" alt="Question Banks & Code" /></a>
  <a href="#labs"><img src="https://img.shields.io/badge/04._Hands--on_Labs-21262D?style=flat" alt="Hands-on Labs" /></a>
  <a href="#curriculum"><img src="https://img.shields.io/badge/Curriculum_Breakdown-21262D?style=flat" alt="Curriculum Breakdown" /></a>
  <a href="#roadmap"><img src="https://img.shields.io/badge/Retake_Roadmap-21262D?style=flat" alt="Retake Roadmap" /></a>
  <a href="#author"><img src="https://img.shields.io/badge/Author_&_Connect-21262D?style=flat" alt="Author & Connect" /></a>
</p>

---

<a id="overview"></a>
## Overview

This repository is an organized, comprehensive, and student-focused preparation suite for the **Huawei HCIA-AI V4.0 Certification Exam (`H13-311_V4.0`)**. 

Curated by **Umed Jamal Nouri** (Senior B.Sc. Electrical Engineering student at Salahaddin University – Erbil), this suite synthesizes official courseware, hands-on lab experiments, verified Pearson VUE exam recalls, and extensive question banks into a clean, intuitive structure designed to help candidates prepare methodically and pass the certification with confidence.

${\color{#10B981}\textsf{\textbf{TIP}}}$ &nbsp;**Official Exam Specification (`H13-311_V4.0`):** 60 examination items (Single Choice, Multiple Choice, True/False) · 90-minute limit · Passing threshold: **600 / 1000 points** (60%).

---

<a id="structure"></a>
## Repository Structure

The entire repository is structured strictly according to the **Recommended Study Roadmap** into **5 dedicated, numbered directories** culminating in an interactive Pearson VUE CBT exam simulator:

```text
HCIA-AI/
│
├── 01_Official_Huawei_Materials/                                <- Phase 1: Untouched Official Curriculum
│   ├── 01_HCIA-AI_V4.0_Exam_Outline.pdf                         (Official syllabus & domain weights)
│   ├── 02_HCIA-AI_V4.0_Training_Material.pdf                    (Official 473-slide comprehensive curriculum)
│   └── 08_HCIA-AI_V4.0_Official_Lab_Guide.pdf                   (Official Huawei lab manual)
│
├── 02_Verified_Exam_Recalls/                                    <- Phase 2: Authentic Recalls & Slide Solutions
│   ├── 05_HCIA-AI_V4.0_Real_Exam_Recalled_Questions_60Q.pdf     (Full 1000-point authentic real exam simulation)
│   ├── 06_HCIA-AI_V4.0_Real_Exam_Recalled_Questions_41Q.pdf     (Historical candidate recall exam)
│   └── 41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.md                      (Slide proofs, trap analysis & derivations)
│
├── 03_Interactive_Exam_Simulator/                               <- Phase 3: Pearson VUE CBT Terminal Engine
│   ├── take_exam.py                                             (Full CBT exam simulator with [S] slide shortcut)
│   └── exam_database.json                                       (Audited 904-question database with slide references)
│
├── 04_AI_Generated_Summaries_Archive/                           <- Phase 4: Systematic Bank & Code Mastery
│   ├── 01_HCIA-AI_V4.0_Master_Question_Bank_Questions_Only_900Q.pdf (Unsolved for self-assessment)
│   ├── 02_HCIA-AI_V4.0_Master_Question_Bank_900Q.pdf            (Complete bank with full answer keys)
│   ├── 03_HCIA-AI_V4.0_Master_Question_Bank_Solved_Direct_Answers_900Q.pdf (Direct answers for rapid review)
│   ├── 03_HCIA-AI_V4.0_Comprehensive_Exam_Focus_Study_Guide.pdf (In-depth topic notes & formulas)
│   ├── 04_HCIA-AI_V4.0_Onsite_Masterclass_Core_Concepts_and_Exam_Tips.pdf (Instructor tips & conceptual traps)
│   ├── 07_HCIA-AI_V4.0_High_Yield_Exam_Focus_Summary.pdf        (24-hour final sprint review)
│   ├── 09_HCIA-AI_V4.0_Mock_Exam_66_Questions_and_Answers.pdf    (Legacy mock questions)
│   ├── 03_Code_Mastery_Guide/                                   (Code writing guide & printable SOMA sheets)
│   │   ├── 01_HCIA-AI_V4.0_Code_Writing_Fill_in_the_Blank_Mastery_Guide.pdf (70 high-yield syntax drills)
│   │   └── 02_HCIA-AI_V4.0_Student_Answer_Sheets_Printable.pdf   (10-page printable bubble answer sheets)
│   └── Individual_Modules_100Q/                                 (Modules 01 to 09, 100 questions each)
│       ├── Module_01_AI_Overview_100Q.pdf
│       ├── Module_02_Machine_Learning_100Q.pdf
│       ├── Module_03_Deep_Learning_and_Foundation_Models_100Q.pdf
│       ├── Module_04_AI_Development_Framework_100Q.pdf
│       ├── Module_05_AI_Business_Process_and_Prompt_Engineering_100Q.pdf
│       ├── Module_06_Cutting_Edge_AI_Applications_100Q.pdf
│       ├── Module_07_Comprehensive_Final_Mock_Exam_100Q.pdf
│       ├── Module_08_Practice_Exam_Set_1_100Q.pdf
│       └── Module_09_Practice_Exam_Set_2_100Q.pdf
│
├── 05_Hands_on_Labs/                                            <- Phase 5: Hands-on Experiments & Labs
│   ├── 01_Linear_Regression.ipynb
│   ├── 02_Linear_Regression_Expansion_Experiment.ipynb
│   ├── 03_Logistic_Regression.ipynb
│   ├── 04_Decision_Tree.ipynb
│   ├── 05_K-means_Clustering.ipynb
│   ├── 06_Deep_Learning_Lab_Guide.docx
│   └── Dataset/ (MNIST, ResNet-50 weights, TextCNN, Web UI)
│
└── take_exam.py                                                 <- 🚀 Root Launcher for Pearson VUE CBT Exam Simulator
```

---

<a id="simulator"></a>
## 🚀 Interactive Pearson VUE Exam Simulator (`take_exam.py`)

A full-featured, interactive computer-based test (CBT) simulator designed to run directly in your terminal. It authentically replicates the **Pearson VUE testing engine** with live 90-minute countdown, question interleaving, bookmarking/flagging, and diagnostic scoring:

```bash
python take_exam.py
```
*(or run directly from `python 03_Interactive_Exam_Simulator/take_exam.py`)*

### 🎯 Simulator Modes & Key Features:
* **Mode 1: Official Real Exam Simulation (Dual-Difficulty CBT):**
  Integrates **BOTH** difficulty tiers into a single authentic 60-question Pearson VUE exam:
  * **30 Moderate Questions:** Foundational definitions, standard ML/DL concepts, and curriculum core items.
  * **30 Hard & Tricky Questions:** Authentic engineering scenarios featuring *John*, CNN dimension calculations ($X=[8,3,100,100] \to [8,32,48,48]$), LoRA 500-domain fine-tuning, and deceptive Pearson VUE traps.
  * **Timing & Scoring:** Exact 1000 Points · 90-Minute countdown timer · Official pass threshold: 600 / 1000 Points.
* **Mode 2: `[Verified Official & Recalled Questions Only]` (Recommended for Retake):**
  Practices exclusively on the authentic recall questions verified 100% against the official 473 slides, eliminating AI filler and outdated V3.0 questions.
* **`[S]` Instant Slide Reference Shortcut:**
  Press **`S`** at any point during question answering or review to toggle an inline box displaying the exact Chapter, Slide Number, verbatim official Huawei quote, and Pearson VUE trap notes!
* **Authentic Pearson VUE Navigation:** Flag for review (`F`), skip, back, review grid (`R`), and jump to unanswered items (`U`).
* **Multi-Answer Audited Grading:**
  Corrects multi-answer combinations (where multiple-answer questions require exact selections), ensuring rigorous grading of `ABCD`, `ABC`, `AB`, and `ABD` combinations.
* **Diagnostic Score Report:** Evaluates your total score against the official passing threshold (**600 / 1000 Points**), displays visual mastery bars per module, and lets you review every missed item with its verified answer and official slide citation.

---

<a id="official"></a>
## 01. Official Huawei Courseware (`01_Official_Huawei_Materials/`)

Contains untouched, authorized Huawei curriculum files representing the primary source of truth for the `H13-311_V4.0` examination:

| Document | Description | Direct Download (PDF) | Repository View |
| :--- | :--- | :---: | :---: |
| **01_HCIA-AI_V4.0_Exam_Outline** | Official Huawei certification syllabus, domain percentages, and detailed test item topics. | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/01_Official_Huawei_Materials/01_HCIA-AI_V4.0_Exam_Outline.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./01_Official_Huawei_Materials/01_HCIA-AI_V4.0_Exam_Outline.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **02_HCIA-AI_V4.0_Training_Material** | Complete 473-slide official training deck covering all 6 syllabus modules. Primary reference for all exam questions. | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **08_HCIA-AI_V4.0_Official_Lab_Guide** | Official step-by-step laboratory experiment guide for Machine Learning and Deep Learning. | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/01_Official_Huawei_Materials/08_HCIA-AI_V4.0_Official_Lab_Guide.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./01_Official_Huawei_Materials/08_HCIA-AI_V4.0_Official_Lab_Guide.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |

---

<a id="recalls"></a>
## 02. Verified Exam Recalls & Slide Solutions (`02_Verified_Exam_Recalls/`)

Contains authentic recalled exam sets from recent successful test-takers alongside a 1,476-line master solution guide with slide proofs:

| Document | Description | Direct Download / View | Repository Link |
| :--- | :--- | :---: | :---: |
| **05_Real_Exam_Recalled_Questions_60Q** | Full 60-question Pearson VUE exam simulation with exact 1000-point weighting, authentic candidate recalls, CNN dimension tracing, and official slide citations. | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/02_Verified_Exam_Recalls/05_HCIA-AI_V4.0_Real_Exam_Recalled_Questions_and_Verified_Answers_60Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./02_Verified_Exam_Recalls/05_HCIA-AI_V4.0_Real_Exam_Recalled_Questions_and_Verified_Answers_60Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **06_Real_Exam_Recalled_Questions_41Q** | Verified solutions for the 41 historical exam questions directly recalled from recent test-takers with step-by-step derivations. | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/02_Verified_Exam_Recalls/06_HCIA-AI_V4.0_Real_Exam_Recalled_Questions_and_Verified_Answers_41Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./02_Verified_Exam_Recalls/06_HCIA-AI_V4.0_Real_Exam_Recalled_Questions_and_Verified_Answers_41Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.md** | Complete 1,476-line master audit containing verbatim quotes from official slides, mathematical proofs, and Pearson VUE trap analysis. | <a href="./02_Verified_Exam_Recalls/41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.md"><img src="https://img.shields.io/badge/View_Guide-Markdown-10B981?style=flat" alt="View Guide" /></a> | <a href="./02_Verified_Exam_Recalls/41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.md"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |

---

<a id="practice-archive"></a>
## 03. Question Banks, Code Guide & Study Summaries (`04_AI_Generated_Summaries_Archive/`)

Contains **900 categorized practice questions**, 70 high-yield code syntax drills, printable SOMA answer sheets, and summary study notes:

### Master Editions (All 900 Questions in Single Volume)
- `SOLVED` &nbsp; **03_HCIA-AI_V4.0_Master_Question_Bank_Solved_Direct_Answers_900Q.pdf (180 Pages)** &nbsp; <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/03_HCIA-AI_V4.0_Master_Question_Bank_Solved_Direct_Answers_900Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> <a href="./04_AI_Generated_Summaries_Archive/03_HCIA-AI_V4.0_Master_Question_Bank_Solved_Direct_Answers_900Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a>  
  *Accelerated recall format: verified answer key and concise technical explanation directly below each question.*
- `STANDARD` &nbsp; **02_HCIA-AI_V4.0_Master_Question_Bank_900Q.pdf (180 Pages)** &nbsp; <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/02_HCIA-AI_V4.0_Master_Question_Bank_900Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> <a href="./04_AI_Generated_Summaries_Archive/02_HCIA-AI_V4.0_Master_Question_Bank_900Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a>  
  *Modular self-study format: discrete in-place answer strip positioned at the footer of each 5-item page.*
- `EXAM-MODE` &nbsp; **01_HCIA-AI_V4.0_Master_Question_Bank_Questions_Only_900Q.pdf (189 Pages)** &nbsp; <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/01_HCIA-AI_V4.0_Master_Question_Bank_Questions_Only_900Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> <a href="./04_AI_Generated_Summaries_Archive/01_HCIA-AI_V4.0_Master_Question_Bank_Questions_Only_900Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a>  
  *Rigorous blind testing: zero visible solutions throughout practice; full answer matrix on pages 181–189.*

### Code Mastery & Printable SOMA Answer Sheets (`03_Code_Mastery_Guide/`)
| Document | Description | Direct Download (PDF) | Repository View |
| :--- | :--- | :---: | :---: |
| **01_Code_Writing_Mastery_Guide** | 70 authentic exam-format fill-in-the-blank items covering PyTorch workflow, MindSpore Cell/construct, 0-D scalar tensors, CNN dimension tracing (2x Conv2d + 2x MaxPool2d), FNN DAG topology, Transformer Positional Encoding, and PEFT LoRA with verified solutions. | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/03_Code_Mastery_Guide/01_HCIA-AI_V4.0_Code_Writing_Fill_in_the_Blank_Mastery_Guide.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/03_Code_Mastery_Guide/01_HCIA-AI_V4.0_Code_Writing_Fill_in_the_Blank_Mastery_Guide.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **02_Student_Answer_Sheets_Printable** | 10-page printable bubble answer sheets (SOMA style) adapted dynamically for all 9 modules with self-grading checkboxes `[✓/✗]` matching Single Choice, True/False, Multiple Select, and Fill-in blanks. | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/03_Code_Mastery_Guide/02_HCIA-AI_V4.0_Student_Answer_Sheets_Printable.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/03_Code_Mastery_Guide/02_HCIA-AI_V4.0_Student_Answer_Sheets_Printable.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |

### Study Guides & High-Yield Summaries
- `STEP-03` &nbsp; **03_HCIA-AI_V4.0_Comprehensive_Exam_Focus_Study_Guide.pdf** &nbsp; <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/03_HCIA-AI_V4.0_Comprehensive_Exam_Focus_Study_Guide.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> <a href="./04_AI_Generated_Summaries_Archive/03_HCIA-AI_V4.0_Comprehensive_Exam_Focus_Study_Guide.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a>  
  *In-depth technical breakdown: Activation formulas (ReLU, Sigmoid, GELU, Swish), Backpropagation calculus, MindSpore construct/Cell, Atlas 900 vs 500, CANN layers, and prompt engineering.*
- `STEP-04` &nbsp; **04_HCIA-AI_V4.0_Onsite_Masterclass_Core_Concepts_and_Exam_Tips.pdf** &nbsp; <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/04_HCIA-AI_V4.0_Onsite_Masterclass_Core_Concepts_and_Exam_Tips.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> <a href="./04_AI_Generated_Summaries_Archive/04_HCIA-AI_V4.0_Onsite_Masterclass_Core_Concepts_and_Exam_Tips.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a>  
  *Onsite instructor notes, key conceptual traps, and exam-taking tips.*
- `STEP-07` &nbsp; **07_HCIA-AI_V4.0_High_Yield_Exam_Focus_Summary.pdf** &nbsp; <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/07_HCIA-AI_V4.0_High_Yield_Exam_Focus_Summary.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> <a href="./04_AI_Generated_Summaries_Archive/07_HCIA-AI_V4.0_High_Yield_Exam_Focus_Summary.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a>  
  *7-page executive summary designed for rapid review 24 hours prior to the examination.*
- `STEP-09` &nbsp; **09_HCIA-AI_V4.0_Mock_Exam_66_Questions_and_Answers.pdf** &nbsp; <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/09_HCIA-AI_V4.0_Mock_Exam_66_Questions_and_Answers.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> <a href="./04_AI_Generated_Summaries_Archive/09_HCIA-AI_V4.0_Mock_Exam_66_Questions_and_Answers.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a>  
  *Legacy 66-question practice pool for historical reference.*

### Modular Chapter Practice Exams (`Individual_Modules_100Q/`)
All modular practice exams are housed in the dedicated subfolder [`04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/`](./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/). Each PDF is strictly 20 pages (100 questions):

| Module / Domain | Weight | Questions | Direct Download (PDF) | Repository View |
| :--- | :---: | :---: | :---: | :---: |
| **Module 01: AI Overview** | 10% | 100 Q | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_01_AI_Overview_100Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_01_AI_Overview_100Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **Module 02: Machine Learning Overview** | 20% | 100 Q | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_02_Machine_Learning_100Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_02_Machine_Learning_100Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **Module 03: Deep Learning & Foundation Models** | 30% | 100 Q | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_03_Deep_Learning_and_Foundation_Models_100Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_03_Deep_Learning_and_Foundation_Models_100Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **Module 04: AI Development Framework** | 20% | 100 Q | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_04_AI_Development_Framework_100Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_04_AI_Development_Framework_100Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **Module 05: Business Process & Prompt Engineering** | 15% | 100 Q | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_05_AI_Business_Process_and_Prompt_Engineering_100Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_05_AI_Business_Process_and_Prompt_Engineering_100Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **Module 06: Cutting-Edge AI Applications** | 5% | 100 Q | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_06_Cutting_Edge_AI_Applications_100Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_06_Cutting_Edge_AI_Applications_100Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **Module 07: Comprehensive Final Mock Exam** | Mock | 100 Q | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_07_Comprehensive_Final_Mock_Exam_100Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_07_Comprehensive_Final_Mock_Exam_100Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **Module 08: Practice Exam Set 1** | Mock | 100 Q | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_08_Practice_Exam_Set_1_100Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_08_Practice_Exam_Set_1_100Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |
| **Module 09: Practice Exam Set 2** | Mock | 100 Q | <a href="https://raw.githubusercontent.com/UmedJaMala/HCIA-AI-V4.0-Certification-Preparation/main/04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_09_Practice_Exam_Set_2_100Q.pdf"><img src="https://img.shields.io/badge/Download_PDF-0284C7?style=flat" alt="Download PDF" /></a> | <a href="./04_AI_Generated_Summaries_Archive/Individual_Modules_100Q/Module_09_Practice_Exam_Set_2_100Q.pdf"><img src="https://img.shields.io/badge/View_in_Repo-181717?style=flat&logo=github&logoColor=white" alt="View in Repo" /></a> |

---

<a id="labs"></a>
## 04. Hands-on Laboratory Experiments (`05_Hands_on_Labs/`)

Contains complete, runnable implementations of all officially required machine learning and deep learning lab practicals alongside a production-grade vision AI application:

### Jupyter Notebooks & Experiments
- `01_Linear_Regression.ipynb` & `02_Linear_Regression_Expansion_Experiment.ipynb`
- `03_Logistic_Regression.ipynb`
- `04_Decision_Tree.ipynb`
- `05_K-means_Clustering.ipynb`
- `06_Deep_Learning_Lab_Guide.docx`
- `Dataset/TextCNN/` — NLP sentiment analysis pipeline on movie reviews.
- `Dataset/CODE/` — Standalone HTML visualizers for experiment outputs.

---

### Interactive Deep Learning Web App: GullNas Vision

A high-performance, modern Claymorphism web application powered by **PyTorch ResNet-50** for real-time botanical flower classification across 5 categories (*Daisy, Dandelion, Roses, Sunflowers, Tulips*):

${\color{#8B5CF6}\textsf{\textbf{IMPORTANT}}}$ &nbsp;**Production Vision Benchmark:** Fine-tuned `torchvision.models.resnet50` on NVIDIA RTX 5060 Laptop GPU achieves **90.20% overall accuracy** with **~5–8 ms inference latency**.

```bash
# To run GullNas Vision locally:
cd 05_Hands_on_Labs/Dataset/MNIST/
python app.py
```

---

<a id="curriculum"></a>
## Official Curriculum Breakdown (`H13-311_V4.0`)

| Chapter | Module Title | Exam Weight | Key Focus Areas in V4.0 |
| :--- | :--- | :---: | :--- |
| **01** | **AI Overview** | **10%** | AI History, Symbolism/Connectionism/Behaviorism, DeepSeek influence, AI Governance & Ethics |
| **02** | **Machine Learning Overview** | **20%** | Supervised/Unsupervised/RL, Data Cleansing (Dirty Data), Decision Trees (ID3, C4.5, CART), KNN, Evaluation Metrics (Confusion Matrix, Precision, Recall, F1) |
| **03** | **Basics of Deep Learning & Foundation Models** | **30%** | Perceptron & XOR, Activation Functions (Sigmoid, Tanh, ReLU), CNN (Kernels, Stride, Padding, Pooling), RNN & LSTM gates, Transformer Self-Attention |
| **04** | **AI Development Framework** | **20%** | Computational Graphs (Static vs Dynamic), **PyTorch** core APIs (`torch.nn`, `torch.optim`, `torchvision`), Tensor shapes & manipulation, Training loop |
| **05** | **AI Business Process Overview** | **15%** | Business workflow, Distributed Training (Data/Tensor/Pipeline parallelism), PEFT (**LoRA**, Prefix Tuning), **RLHF** (SFT $\to$ RM $\to$ PPO), **Prompt Engineering** (Zero-Shot-CoT) |
| **06** | **Cutting-edge AI Applications** | **5%** | CV, NLP, Robotics (RT-2), Intelligent Recommendation, **AI4Science** (AlphaFold, FermiNet, GNoME, DeePMD) |

---

<a id="roadmap"></a>
## Recommended Study & Retake Roadmap

${\color{#10B981}\textsf{\textbf{TIP}}}$ &nbsp;**Structured Preparation Sequence:** Progress methodically from fundamental AI theory through code syntax to timed mock exams.

1. **Phase 1: Official Courseware Study (`01_Official_Huawei_Materials/`)**  
   Read through the [02_Training_Material](./01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf) (473 slides) and review the [01_Exam_Outline](./01_Official_Huawei_Materials/01_HCIA-AI_V4.0_Exam_Outline.pdf) and [08_Official_Lab_Guide](./01_Official_Huawei_Materials/08_HCIA-AI_V4.0_Official_Lab_Guide.pdf).

2. **Phase 2: Master Authentic Recalls & Slide Solutions (`02_Verified_Exam_Recalls/`)**  
   Study [41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.md](./02_Verified_Exam_Recalls/41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.md) to memorize verbatim slide phrasings, tricky word traps, and derivations for [05_Real_Exam_Recalled_Questions_60Q](./02_Verified_Exam_Recalls/05_HCIA-AI_V4.0_Real_Exam_Recalled_Questions_and_Verified_Answers_60Q.pdf).

3. **Phase 3: Interactive CBT Timed Simulations (`03_Interactive_Exam_Simulator/`)**  
   Launch the terminal simulator (`python take_exam.py`) and practice with **Mode 2: `[Verified Official & Recalled Questions Only]`** and **Mode 1: `[Official Real Exam Simulation]`**. Press **`S`** to verify tricky questions against official slides.

4. **Phase 4: Systematic Question Bank Practice & Code Drills (`04_AI_Generated_Summaries_Archive/`)**  
   Print the [02_Student_Answer_Sheets](./04_AI_Generated_Summaries_Archive/03_Code_Mastery_Guide/02_HCIA-AI_V4.0_Student_Answer_Sheets_Printable.pdf) and solve practice modules. Work through the [01_Code_Writing_Mastery_Guide](./04_AI_Generated_Summaries_Archive/03_Code_Mastery_Guide/01_HCIA-AI_V4.0_Code_Writing_Fill_in_the_Blank_Mastery_Guide.pdf) and run the notebooks in [05_Hands_on_Labs/](./05_Hands_on_Labs/).

5. **Phase 5: Final Rapid Review (24 Hours Prior to Exam)**  
   Review the [03_Master_Solved_Direct_Answers_Edition](./04_AI_Generated_Summaries_Archive/03_HCIA-AI_V4.0_Master_Question_Bank_Solved_Direct_Answers_900Q.pdf) and the [07_High_Yield_Exam_Focus_Summary](./04_AI_Generated_Summaries_Archive/07_HCIA-AI_V4.0_High_Yield_Exam_Focus_Summary.pdf) 24 hours prior to the official exam session.

---

## Disclaimer & Academic Honesty

- **Educational Purpose:** This repository is an independent study aid compiled to assist students and professionals in mastering AI fundamentals and preparing for the HCIA-AI V4.0 certification exam.
- **Huawei Trademarks:** Huawei, Huawei Certified ICT Associate, MindSpore, Ascend, and ModelArts are registered trademarks of Huawei Technologies Co., Ltd. This project is not officially affiliated with, endorsed by, or sponsored by Huawei.
- **Official Enrollment:** For official exam registration, vouchers, and authorized academy materials, please visit the [Huawei Talent Portal](https://e.huawei.com/en/talent/).

---

<a id="author"></a>
## Author & Connect

**Umed Jamal Nouri**  
Senior B.Sc. Electrical Engineering Student · Salahaddin University – Erbil  
Curator & Lead Maintainer

**Universal Social Handle:** [`@UmedJaMala`](https://github.com/UmedJaMala) *(same username across GitHub, LinkedIn, Telegram, and X)*

<p align="left">
  <a href="https://github.com/UmedJaMala"><img src="https://img.shields.io/badge/GitHub-UmedJaMala-181717?style=flat&logo=github&logoColor=white" alt="GitHub Profile" /></a>
  <a href="https://linkedin.com/in/UmedJaMala"><img src="https://img.shields.io/badge/LinkedIn-UmedJaMala-0A66C2?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn Profile" /></a>
  <a href="https://t.me/UmedJaMala"><img src="https://img.shields.io/badge/Telegram-UmedJaMala-26A5E4?style=flat&logo=telegram&logoColor=white" alt="Telegram Profile" /></a>
</p>
