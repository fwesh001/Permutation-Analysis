"""
=============================================================================
PROJECT: Higher-Order Iteration Testing Engine for Thesis (k >= 3)
AUTHOR: Zabdiel
DESCRIPTION: 
    This script tests the scalability of the recursive permutation engine 
    for advanced iteration levels (k = 3 and higher). It evaluates deeper 
    recursive states, prints the expanded polynomials, and outputs the 
    resulting matrix tables to verify complex thesis proofs.
=============================================================================
"""

import sympy as sp

# =============================================================================
# BLOCK 1: SYMBOLIC ENVIRONMENT INITIALIZATION
# =============================================================================
A0, A1, A2, A3 = sp.symbols('A0 A1 A2 A3')
A = [A0, A1, A2, A3]


# =============================================================================
# BLOCK 2: RECURSIVE GOVERNING EQUATION FUNCTION (CORE ENGINE)
# =============================================================================
def Q(k, j):
    """
    Recursive function to evaluate Q_k(jh) for higher-order levels.
    """
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


# =============================================================================
# BLOCK 3: PERMUTATION TABLE MATRIX PARSER FUNCTION
# =============================================================================
def generate_table(expression):
    """
    Parses expanded polynomial into matrix rows [r0, r1, r2, r3].
    """
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
# BLOCK 4: TERMINAL FORMATTER & RENDERER FUNCTION
# =============================================================================
def print_permutation_table(k, j):
    """
    Evaluates higher-order equations and prints formatted grid outputs.
    """
    equation = Q(k, j)
    table = generate_table(equation)
    
    print(f"\n--- Higher-Order Permutation Table for Q_{k}({j}h) ---")
    print(f"Polynomial: {equation}")
    print(f"{'r0':^4} | {'r1':^4} | {'r2':^4} | {'r3':^4}")
    print("-" * 35)
    
    if not table:
        print(f"{0:^4} | {0:^4} | {0:^4} | {0:^4}")
    else:
        for row in table:
            print(f"{row[0]:^4} | {row[1]:^4} | {row[2]:^4} | {row[3]:^4}")


# =============================================================================
# BLOCK 5: EXECUTION ENTRY POINT (ADVANCED HIGHER-ORDER TESTS)
# =============================================================================
if __name__ == "__main__":
    print("Running Advanced Higher-Order Iteration Tests (k = 3)...")
    
    # Test third-order iterations across multiple steps
    print_permutation_table(k=3, j=1)
    print_permutation_table(k=3, j=2)
    print_permutation_table(k=3, j=3)