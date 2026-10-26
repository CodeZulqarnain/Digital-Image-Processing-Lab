<!-- Header Banner with Animated Wave Effect -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,25,30,35&height=220&section=header&text=Digital%20Image%20Processing%20Lab&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38" width="100%" alt="Header Banner" />
</p>

<!-- Animated Typing Subtitle -->
<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3000&pause=1000&color=00F5D4&center=true&vCenter=true&multiline=false&width=650&height=45&lines=Welcome+to+the+DIP+Laboratory+Repository;Python+%E2%80%A2+NumPy+%E2%80%A2+Pillow+%E2%80%A2+Matplotlib+%E2%80%A2+OpenCV;University+of+Azad+Jammu+and+Kashmir;Department+of+Software+Engineering+(Session+2024-28)" alt="Typing SVG" />
  </a>
</p>

<!-- Badges Strip -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/NumPy-2.4+-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Pillow-12.1+-11557C?style=for-the-badge&logo=python&logoColor=white" alt="Pillow" />
  <img src="https://img.shields.io/badge/Matplotlib-3.11+-11557c?style=for-the-badge&logo=plotly&logoColor=white" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Semester-5th-8A2BE2?style=for-the-badge" alt="Semester" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" alt="Status" />
</p>

---

### 🌐 Academic Context

| Attribute | Details |
| :--- | :--- |
| 🏛️ **Institution** | **The University of Azad Jammu and Kashmir (UAJK)** |
| 🏢 **Department** | Department of Software Engineering |
| 🔬 **Course** | Digital Image Processing (DIP) Lab |
| 👨‍🏫 **Lab Instructor** | Engr. Fahad Nisar |
| 🎓 **Session / Term** | 2024–2028 \| 5th Semester |

---

### 🚀 Overview & Objectives

This repository contains all laboratory source code, practical implementations, algorithms, and documentation for the **Digital Image Processing (DIP)** course. The labs progress from foundational Python data structures and low-level image representations to advanced spatial and frequency domain image enhancements, filtering, segmentation, and feature extraction.

```
📁 DIP
├── 📄 README.md                 # Animated Repository Documentation
├── 📄 Lab Task 01.pdf           # Instructor Lab Manual & Rubric
├── 📄 LAB_REPORT_01.md          # Formatted Lab 1 Submission Report
├── 🐍 hello.py                  # Lab 01 - Verification Script
├── 🐍 basics.py                 # Lab 01 - Fundamental Exercises (1 - 6)
├── 🐍 lab01_imports.py          # Lab 01 - Essential DIP Library Imports
└── 📁 dip-lab-01/               # Lab 01 Workspace Folder
    ├── 🐍 hello.py
    ├── 🐍 basics.py
    └── 🐍 lab01_imports.py
```

---

### 🧪 Lab Syllabus & Progress Tracker

| # | Lab Title | Core Concepts | Status |
| :-: | :--- | :--- | :-: |
| **01** | **Python Setup, Fundamentals & Imports** | Variables, Control Flow, Loops, Functions, Collections, NumPy, Pillow, Matplotlib | Completed |
| **02** | **Image Representation & Basic Transformations** | Pixel Matrices, Color Channels (RGB/Grayscale), Brightness, Contrast & Inversion | In Progress |
| **03** | **Histogram Analysis & Equalization** | Pixel Frequency, Contrast Enhancement, Histogram Matching | Planned |
| **04** | **Spatial Filtering & Convolution** | Smoothing, Gaussian Blur, Median Filtering, Kernel Convolutions | Planned |
| **05** | **Edge Detection & Sharpening** | Sobel, Prewitt, Laplacian, Canny Edge Detection | Planned |
| **06** | **Frequency Domain Processing** | 2D Fourier Transform (FFT), Ideal & Butterworth High/Low Pass Filters | Planned |
| **07** | **Morphological Image Processing** | Dilation, Erosion, Opening, Closing, Boundary Extraction | Planned |
| **08** | **Image Segmentation & Thresholding** | Global Otsu Thresholding, Adaptive Thresholding, Watershed Algorithm | Planned |

---

### 💻 Deep Dive: Lab 01 Execution Details

<details open>
<summary><b>🔍 Click to view Lab 01 Exercises Breakdown</b></summary>
<br>

* **Exercise 1: Variables & Data Types**
  * Image dimensions (`640x480`), string filename, boolean color flag.
  * Calculation of total image pixels: $640 \times 480 = 307{,}200$.
* **Exercise 2: Conditional Statements**
  * Boundary verification: Intensity range checks for values $< 0$ or $> 255$ (`Invalid`), $\ge 128$ (`Bright pixel`), and $< 128$ (`Dark pixel`).
* **Exercise 3: Iterations & Control Loops**
  * Traversal of pixel arrays with threshold checks (`for` loop) alongside counter iteration (`while` loop).
* **Exercise 4: Functions & Modularity**
  * Parameterized thresholding function `is_bright(pixel, threshold=128)` returning boolean evaluation.
* **Exercise 5: Collections (Lists vs. Tuples)**
  * List operations: indexing, in-place modification, dynamic appending (`.append()`), and dimension tuple unpacking (`w, h = size`).
  * *Concept Check:* Mutability of dynamic lists vs. immutability of structural tuples.
* **Exercise 6: Hash Maps & Sets**
  * Dictionary metadata mapping (`width`, `height`, `mode: "RGB"`) and duplicate elimination using Hash Sets (`set()`).

</details>

---

### ⚡ Quickstart & Installation

#### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/DIP.git
cd DIP
```

#### 2. Verify Python & Pip
```bash
python --version
python -m pip --version
```

#### 3. Install Required Scientific Packages
```bash
python -m pip install numpy pillow matplotlib
```

#### 4. Run Scripts
```bash
# Test basic installation
python hello.py

# Run all fundamental exercises
python basics.py

# Verify DIP imports
python lab01_imports.py
```

---

<!-- Animated Footer Wave -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=0,2,25,30,35&height=120&section=footer" width="100%" alt="Footer Banner" />
</p>

<p align="center">
  <sub>Digital Image Processing Lab • Department of Software Engineering • UAJK</sub>
</p>
