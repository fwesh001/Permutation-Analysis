# Thesis Permutation Analysis Engine

This repository contains a suite of Python scripts designed to automate the complex algebraic bookkeeping required for numerical analysis thesis proofs. Specifically, it calculates, simplifies, and exports the error constants and permutation matrices for custom block methods and Linear Multistep Methods (LMMs) used in solving Ordinary Differential Equations (ODEs).

By automating the recursive step-functions using the `SymPy` library, this tool eliminates tedious manual calculations, prevents human error in cubic/higher-order expansions, and formats the output directly into academic-ready tables.

## 📂 File Breakdown & Architecture

Here is a guide to what each script in this repository does:

**1. `recursive_permutation_engine.py` (The Core Engine)**
*   **What it does:** This is the foundation of the project. It houses the main mathematical formula (the governing recursive equation).
*   **How it works:** It takes the starting rules ($Q(0) = I$, negative step constraints) and automatically multiplies the base variables ($A_0, A_1, A_2, A_3$) through a recursive loop. It then groups identical algebraic terms together and extracts the exponents into a clean matrix grid ($r_0, r_1, r_2, r_3$).

**2. `piecewise_step_mapper.py` (The Grid Logic)**
*   **What it does:** This script handles the dynamic rules for when grid step-sizes vary.
*   **How it works:** It implements the specific conditional boundaries for the method, utilizing floor division ratios ($\lfloor h_j / h_i \rfloor$) and signum functions (`sgn`) to ensure the matrix elements map correctly across non-uniform step intervals.

**3. `higher_order_tester.py` (The Scalability Tester)**
*   **What it does:** This script is designed to push the core engine to higher iteration levels ($k \ge 3$).
*   **How it works:** While the base engine is great for $k=1$ or $k=2$, this file specifically evaluates deeper recursive states. It is used to prove that the equations scale accurately when dealing with massive polynomial expansions (like cubic terms).

**4. `export_module.py` (The Publisher)**
*   **What it does:** Packages the raw terminal data into formatted files you can drop straight into a thesis document.
*   **How it works:** It loops through predefined test cases, runs the algebra, and saves the final permutation matrices into two formats:
    *   `permutation_tables_output.csv`: A raw, flat data table.
    *   `thesis_permutation_analysis.xlsx`: A polished, multi-sheet Excel workbook.

## 🚀 Installation & Setup

To run these scripts locally, ensure you have Python 3.11+ installed along with the required mathematical and data-processing libraries.

Activate your virtual environment and run:
```bash
pip install sympy pandas openpyxl