# Huawei Certified ICT Associate - Artificial Intelligence (HCIA-AI V4.0)
### Official Exam Preparation Suite · Verified Pearson VUE Recalls · Interactive CBT Simulator · Single Source of Truth

<p align="left">
  <a href="https://e.huawei.com/en/talent/#/cert/product-details?target=qualification&badgeId=0&qualificationId=399"><img src="https://img.shields.io/badge/Certification-Huawei_HCIA--AI_V4.0-1F2937?style=flat&logo=huawei&logoColor=EF4444" alt="Certification: Huawei HCIA-AI V4.0" /></a>
  <a href="https://e.huawei.com/en/talent/"><img src="https://img.shields.io/badge/Exam_Code-H13--311_V4.0-1F2937?style=flat&logo=target&logoColor=38BDF8" alt="Exam Code: H13-311" /></a>
  <a href="./01_Official_Huawei_Materials/"><img src="https://img.shields.io/badge/Official_Courseware-473_Slides-1F2937?style=flat&logo=bookstack&logoColor=10B981" alt="Official Slides: 473 Slides" /></a>
  <a href="./02_Verified_Exam_Recalls/"><img src="https://img.shields.io/badge/Verified_Recalls-41Q_&_60Q-1F2937?style=flat&logo=gitbook&logoColor=F59E0B" alt="Verified Recalls: 41Q & 60Q" /></a>
  <a href="./03_Interactive_Exam_Simulator/"><img src="https://img.shields.io/badge/Exam_Simulator-Pearson_VUE_CBT-1F2937?style=flat&logo=terminal&logoColor=10B981" alt="Exam Simulator" /></a>
  <a href="./05_Hands_on_Labs/"><img src="https://img.shields.io/badge/Hands--on_Labs-PyTorch_&_ML-1F2937?style=flat&logo=pytorch&logoColor=EE4C2C" alt="Hands-on Labs" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-1F2937?style=flat&logo=opensourceinitiative&logoColor=94A3B8" alt="License: MIT" /></a>
</p>

---

> [!IMPORTANT]
> ### 🚨 CRITICAL NOTICE FOR RETAKE CANDIDATES (V4.0 Pearson VUE Syllabus Scope)
> If you previously studied using generic AI dumps or older HCIA-AI materials (V3.0/V3.5), be aware of the official **2025 HCIA-AI V4.0 syllabus changes**:
> 
> 1. **Framework Shift to PyTorch:** The primary deep learning framework in HCIA-AI V4.0 is **PyTorch** (34 slides in Chapter 4). Legacy Huawei hardware topics (Ascend 310/910 DaVinci Core units [Cube/Vector/Scalar], CANN TBE/ATC operator compilers, and MindSpore architecture) **have zero slides in the official training deck and are non-testable in V4.0**.
> 2. **Foundation Models & DeepSeek:** V4.0 officially introduced **DeepSeek** (19 slides in Chapter 1) and extensive coverage of Large Language Models (LLMs).
> 3. **AI Business Process & Prompt Engineering (Chapter 5):** Heavily tests Parameter-Efficient Fine-Tuning (**LoRA**, Prefix Tuning), **RLHF** (SFT $\to$ Reward Model RM $\to$ PPO), and Prompt Engineering (**Zero-Shot-CoT**, *"Let's think step by step"*).
> 4. **AI for Science (Chapter 6):** Focuses on 2024 Nobel Prize in Chemistry (**AlphaFold** by DeepMind), **FermiNet**, **GNoME**, and **DeePMD-kit** (Slides 467–470).
>
> **The single authoritative Source of Truth is [01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf](file:///c:/Users/HC/Desktop/HCIA-AI/01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf).**

---

## Repository Structure

The repository is organized into clearly defined, role-separated directories:

```text
HCIA-AI/
│
├── 01_Official_Huawei_Materials/            <- 🏛️ Untouched Official Huawei PDFs (Single Source of Truth)
│   ├── 01_HCIA-AI_V4.0_Exam_Outline.pdf    (Exam objectives, Pearson VUE scoring rules & weights)
│   ├── 02_HCIA-AI_V4.0_Training_Material.pdf (Official 473-slide core training deck)
│   ├── 08_HCIA-AI_V4.0_Official_Lab_Guide.pdf (Official hands-on lab experiments guide)
│   ├── HCIA-AI_V4.0_Official_Slide_Summary_Guide.md (Strict V4.0 curriculum synthesis)
│   └── HCIA-AI_V4.0_Official_Slide_Summary_Guide.pdf (Professional printable summary guide)
│
├── 02_Verified_Exam_Recalls/                <- 🎯 Authentic Pearson VUE Recalls & Master Slide Proofs
│   ├── 41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.md (Master study guide: verbatim slide quotes & trap analysis)
│   ├── 41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.pdf (Printable master solutions PDF with slide proofs)
│   ├── 05_HCIA-AI_V4.0_Real_Exam_Recalled_Questions_and_Verified_Answers_60Q.pdf (Full 60Q recall exam)
│   └── 06_HCIA-AI_V4.0_Real_Exam_Recalled_Questions_and_Verified_Answers_41Q.pdf (41Q candidate recall)
│
├── 03_Interactive_Exam_Simulator/           <- 🚀 Authentic Pearson VUE Terminal Simulator (CBT)
│   ├── take_exam.py                         (Interactive CBT test engine with [S] slide shortcut)
│   └── exam_database.json                   (Pure V4.0 847-question bank with verified slide citations)
│
├── 04_AI_Generated_Summaries_Archive/       <- ⚠️ Archived AI Summaries & Regenerated V4.0 Question Banks
│   ├── README.md                            (Explicit warning disclaimer regarding AI hallucinations)
│   ├── legacy_v3_questions_backup.json      (57 removed V3.0 Ascend/CANN/MindSpore questions)
│   ├── 01_HCIA-AI_V4.0_Master_Question_Bank_Questions_Only_900Q.pdf (847 questions unsolved for practice)
│   ├── 02_HCIA-AI_V4.0_Master_Question_Bank_900Q.pdf (847 questions with answers & slide references)
│   ├── 03_HCIA-AI_V4.0_Master_Question_Bank_Solved_Direct_Answers_900Q.pdf (Direct answer key table)
│   ├── 03_HCIA-AI_V4.0_Comprehensive_Exam_Focus_Study_Guide.pdf (V4.0 slide summary guide)
│   ├── 04_HCIA-AI_V4.0_Onsite_Masterclass_Core_Concepts_and_Exam_Tips.pdf (V4.0 exam tips guide)
│   ├── 07_HCIA-AI_V4.0_High_Yield_Exam_Focus_Summary.pdf (V4.0 high yield summary)
│   ├── 09_HCIA-AI_V4.0_Mock_Exam_66_Questions_and_Answers.pdf
│   ├── 03_Code_Mastery_Guide/               (Fill-in-the-blank code guides & printable answer sheets)
│   └── Individual_Modules_100Q/             (Modules 01 to 09, 100% regenerated with slide citations)
│
├── 05_Hands_on_Labs/                        <- 🧪 Practical Hands-on Labs & Jupyter Notebooks
│   ├── 01_Linear_Regression.ipynb
│   ├── 02_Linear_Regression_Expansion_Experiment.ipynb
│   ├── 03_Logistic_Regression.ipynb
│   ├── 04_Decision_Tree.ipynb
│   ├── 05_K-means_Clustering.ipynb
│   ├── 06_Deep_Learning_Lab_Guide.docx
│   └── Dataset/                             (MNIST, TextCNN, flower datasets, ResNet-50 weights)
│
└── take_exam.py                             <- Root launcher pointing to 03_Interactive_Exam_Simulator
```

---

## 🚀 Pearson VUE Interactive Exam Simulator

A full-featured Computer-Based Testing (CBT) terminal simulator replicating the authentic Pearson VUE examination environment:

```bash
python take_exam.py
```
*(or run directly from `03_Interactive_Exam_Simulator/take_exam.py`)*

### Key Features:
* **Mode 2: `[Verified Official & Recalled Questions Only]` (Recommended for Retake):**
  Practices exclusively on the 60 authentic recall questions verified 100% against the official 473 slides, eliminating AI filler and outdated V3.0 questions.
* **`[S]` Instant Slide Reference Shortcut:**
  Press **`S`** at any point during question answering or review to toggle an inline box displaying the exact Chapter, Slide Number, verbatim official Huawei quote, and Pearson VUE trap notes.
* **Pearson VUE Review Screen & Interleaving:**
  Interleaves question types Pearson VUE style (Single-Choice $\to$ True/False $\to$ Multiple-Choice) with flagging (`F`), direct jump navigation, and unanswered question detection (`U`).
* **Multi-Answer Audited Grading:**
  Corrects previous AI answer truncation bugs (where multiple-answer questions were erroneously marked as just `A`), ensuring rigorous grading of `ABCD`, `ABC`, `AB`, and `ABD` combinations.
* **100% Pure V4.0 Question Bank:**
  Contains 847 active questions with **zero empty explanations** and **zero outdated V3.0 questions**. Every single question includes its exact Chapter and Slide citation.
* **Diagnostic Report Export:**
  Generates a full diagnostic score report broken down by curriculum module, difficulty level, and missed questions with official slide references.

---

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

## Recommended Retake Strategy

1. **Step 1:** Read [02_Verified_Exam_Recalls/41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.md](file:///c:/Users/HC/Desktop/HCIA-AI/02_Verified_Exam_Recalls/41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.md) or [02_Verified_Exam_Recalls/41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.pdf](file:///c:/Users/HC/Desktop/HCIA-AI/02_Verified_Exam_Recalls/41Q_60Q_OFFICIAL_SLIDE_SOLUTIONS.pdf) to memorize the exact verbatim Huawei slide phrasings and word traps.
2. **Step 2:** Read [01_Official_Huawei_Materials/HCIA-AI_V4.0_Official_Slide_Summary_Guide.md](file:///c:/Users/HC/Desktop/HCIA-AI/01_Official_Huawei_Materials/HCIA-AI_V4.0_Official_Slide_Summary_Guide.md) for a condensed 6-chapter technical review with exact slide numbers.
3. **Step 3:** Run `python take_exam.py` and select **Mode 2: `[Verified Official & Recalled Questions Only]`**. Repeat until achieving 1000/1000 consistently.
4. **Step 4:** Open [01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf](file:///c:/Users/HC/Desktop/HCIA-AI/01_Official_Huawei_Materials/02_HCIA-AI_V4.0_Training_Material.pdf) and review **Chapter 3 (Deep Learning)** and **Chapter 5 (AI Business Process / LLMs)** end-to-end to close the final 83-point gap.
5. **Step 5:** Review the built-in quizzes on **Slides 92, 187, 299–302, 376, 439, and 471**, which mirror real Pearson VUE question stems.
