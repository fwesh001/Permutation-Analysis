"""
=============================================================================
PROJECT: Thesis Data Export Module (CSV & Excel Formats)
AUTHOR: Zabdiel
DESCRIPTION: 
    This script handles the export pipeline for the recursive permutation 
    tables. It compiles calculated polynomial expressions and matrix 
    coefficients into clean CSV flat files and multi-sheet Excel workbooks 
    for academic journal publishing.
=============================================================================
"""

import sympy as sp
import pandas as pd
import os

# =============================================================================
# BLOCK 1: SYMBOLIC ENVIRONMENT & CORE ENGINE (From Images 1 & 2)
# =============================================================================
A0, A1, A2, A3 = sp.symbols('A0 A1 A2 A3')
A = [A0, A1, A2, A3]

def Q(k, j):
    """Recursive function to evaluate Q_k(jh) based on the governing equation."""
    if k == 0:
        if j == 0:
            return 1
        else:
            return 0
    if j == 0:
        return A0**k
    if j < 0:
        return 0  

    result = 0
    for i in range(4):
        result += A[i] * Q(k - 1, j - i)

    return sp.expand(result)

def generate_table(expression):
    """Parses expanded algebraic expression into matrix rows [r0, r1, r2, r3]."""
    if expression == 0:
        return []

    terms = expression.args if expression.is_Add else [expression]
    
    table_data = []
    for term in terms:
        powers = term.as_powers_dict()
        row = [
            int(powers.get(A0, 0)),
            int(powers.get(A1, 0)),
            int(powers.get(A2, 0)),
            int(powers.get(A3, 0))
        ]
        table_data.append(row)
        
    return table_data


# =============================================================================
# BLOCK 2: DATA COMPILER FUNCTION
# =============================================================================
def compile_permutation_data(test_cases):
    """
    Runs calculations for a list of (k, j) tuples and compiles 
    them into a structured format suitable for dataframes.
    
    Parameters:
        test_cases (list of tuples): Pairs of (k, j) values to evaluate
        
    Returns:
        list of dicts: Compiled data records
    """
    compiled_records = []
    
    for k, j in test_cases:
        equation = Q(k, j)
        table = generate_table(equation)
        
        # Format polynomial as a clean string for storage
        poly_str = str(equation)
        
        if not table:
            compiled_records.append({
                "Iteration_k": k,
                "Step_j": j,
                "Polynomial_Expression": poly_str,
                "r0": 0, "r1": 0, "r2": 0, "r3": 0
            })
        else:
            for row in table:
                compiled_records.append({
                    "Iteration_k": k,
                    "Step_j": j,
                    "Polynomial_Expression": poly_str,
                    "r0": row[0],
                    "r1": row[1],
                    "r2": row[2],
                    "r3": row[3]
                })
                
    return compiled_records


# =============================================================================
# BLOCK 3: DUAL-FORMAT EXPORT FUNCTIONS (CSV & EXCEL)
# =============================================================================
def export_to_csv(data_records, filename="permutation_tables_output.csv"):
    """
    Exports compiled permutation records to a flat CSV file structure.
    """
    df = pd.DataFrame(data_records)
    df.to_csv(filename, index=False)
    print(f"[SUCCESS] Data successfully exported to CSV: {os.path.abspath(filename)}")

def export_to_excel(data_records, filename="thesis_permutation_analysis.xlsx"):
    """
    Exports compiled records into a multi-format Excel workbook (.xlsx) 
    with a summary sheet and clean tabular layout.
    """
    df = pd.DataFrame(data_records)
    
    # Write to Excel using openpyxl engine
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        # Sheet 1: Full structured dataset
        df.to_excel(writer, sheet_name='Permutation_Summary', index=False)
        
    print(f"[SUCCESS] Data successfully exported to Excel Workbook: {os.path.abspath(filename)}")


# =============================================================================
# BLOCK 4: EXECUTION ENTRY POINT
# =============================================================================
if __name__ == "__main__":
    print("Initializing Thesis Export Pipeline...")
    
    # Define test suite matching manuscript cases
    # (k, j) pairs to compute and export
    cases_to_export = [
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 2)
    ]
    
    # Compile records
    records = compile_permutation_data(cases_to_export)
    
    # Execute exports
    export_to_csv(records)
    export_to_excel(records)