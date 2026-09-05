"""
=============================================================================
PROJECT: Recursive Permutation Engine for Thesis (Images 1 & 2)
AUTHOR: Zabdiel
DESCRIPTION: 
    This script automates the symbolic algebraic expansion of the governing 
    recursive equation for numerical ODE methods. It handles initial 
    conditions, negative step constraints, and parses expanded polynomials 
    into structured permutation tables tracking coefficients (A0, A1, A2, A3).
=============================================================================
"""

import sympy as sp

# =============================================================================
# BLOCK 1: SYMBOLIC ENVIRONMENT INITIALIZATION
# =============================================================================
# Define the base symbolic coefficients used in the recursive equations
A0, A1, A2, A3 = sp.symbols('A0 A1 A2 A3')
A = [A0, A1, A2, A3]


# =============================================================================
# BLOCK 2: RECURSIVE GOVERNING EQUATION & BOUNDARY CONDITIONS FUNCTION
# =============================================================================
def Q(k, j):
    """
    Recursive function to evaluate Q_k(jh) based on the governing equation:
    Q_k(jh) = A0*Q_{k-1}(jh) + A1*Q_{k-1}((j-1)h) + ... + A3*Q_{k-1}((j-3)h)
    
    Parameters:
        k (int): Iteration order level
        j (int): Step index multiplier
        
    Returns:
        sympy.Expr: Simplified expanded algebraic polynomial expression
    """
    
    # Condition 1: Base state at k = 0
    if k == 0:
        if j == 0:
            return 1  # Q_0(0) = I (Identity matrix, represented as 1)
        else:
            return 0  # Q_0(jh) = 0 for all j != 0

    # Condition 2: Zero-step boundary condition
    if j == 0:
        return A0**k  # Q_k(0) = A_0^k
        
    # Condition 3: Negative step constraint (e.g., Q_1(-h) must be zero)
    if j < 0:
        return 0  

    # Condition 4: Core Governing Recursive Equation Loop
    # Accumulates terms across the 4 shift parameters (i from 0 to 3)
    result = 0
    for i in range(4):
        result += A[i] * Q(k - 1, j - i)

    # Return the fully expanded and grouped algebraic expression
    return sp.expand(result)


# =============================================================================
# BLOCK 3: PERMUTATION TABLE MATRIX PARSER FUNCTION
# =============================================================================
def generate_table(expression):
    """
    Parses the expanded algebraic expression to extract the exponents 
    of A0, A1, A2, A3, mapping them into matrix rows for the permutation table.
    
    Parameters:
        expression (sympy.Expr): The polynomial output from Q(k, j)
        
    Returns:
        list of lists: Matrix rows representing [r0, r1, r2, r3] counts
    """
    if expression == 0:
        return []

    # Separate multi-term polynomials into individual additive parts
    terms = expression.args if expression.is_Add else [expression]
    
    table_data = []
    for term in terms:
        # Extract algebraic powers map (ignoring scalar coefficients like '2')
        powers = term.as_powers_dict()
        
        # Build the row mapping for r0, r1, r2, r3 (casting to standard ints)
        row = [
            int(powers.get(A0, 0)),
            int(powers.get(A1, 0)),
            int(powers.get(A2, 0)),
            int(powers.get(A3, 0))
        ]
        table_data.append(row)
        
    return table_data


# =============================================================================
# BLOCK 4: TERMINAL FORMATTER & RENDERER FUNCTION
# =============================================================================
def print_permutation_table(k, j):
    """
    Evaluates the recursive equation, generates its table data, 
    and prints a cleanly formatted text grid to the terminal.
    """
    equation = Q(k, j)
    table = generate_table(equation)
    
    print(f"\n--- Permutation Table for Q_{k}({j}h) ---")
    print(f"Polynomial: {equation}")
    print(f"{'r0':^4} | {'r1':^4} | {'r2':^4} | {'r3':^4}")
    print("-" * 25)
    
    if not table:
        print(f"{0:^4} | {0:^4} | {0:^4} | {0:^4}")
    else:
        for row in table:
            print(f"{row[0]:^4} | {row[1]:^4} | {row[2]:^4} | {row[3]:^4}")


# =============================================================================
# BLOCK 5: EXECUTION ENTRY POINT (TEST CASES FROM MANUSCRIPT)
# =============================================================================
if __name__ == "__main__":
    print("Running Permutation Table Calculations for Images 1 & 2...")
    
    # Test Base Cases (k = 1)
    print_permutation_table(k=1, j=1)
    print_permutation_table(k=1, j=2)
    print_permutation_table(k=1, j=3)
    
    # Test Higher Order Case (k = 2)
    print_permutation_table(k=2, j=2)