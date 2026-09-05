"""
=============================================================================
PROJECT: Piecewise Step-Size & Signum Mapping Engine for Thesis (Image 3)
AUTHOR: Zabdiel
DESCRIPTION: 
    This script implements the piecewise grid logic, floor division ratios 
    (floor(hj / hi)), and signum boundary constraints outlined on the final 
    page of the manuscript notes.
=============================================================================
"""

import math

# =============================================================================
# BLOCK 1: PIECEWISE STEP RATIO EVALUATION FUNCTION
# =============================================================================
def evaluate_piecewise_qi(i, j, hi, hj):
    """
    Evaluates the piecewise condition from Image 3:
    Q_i(jh) = A_i if j = floor(hj / hi), else 0
    
    Parameters:
        i (int): Index value for component A_i (0 to 3)
        j (int): Target step index multiplier
        hi (float/int): Base grid step size
        hj (float/int): Comparative grid step size
        
    Returns:
        str or int: Returns variable name string if condition matches, else 0
    """
    if hi == 0:
        return 0
        
    # Calculate step-size ratio and apply floor division
    ratio = hj / hi
    floor_val = math.floor(ratio)
    
    # Check conditional boundaries
    if j == floor_val and i in [0, 1, 2, 3]:
        return f"A_{i}"
    else:
        return 0


# =============================================================================
# BLOCK 2: SIGNUM BOUNDARY CONSTRAINT FUNCTION
# =============================================================================
def evaluate_signum_bound(i):
    """
    Evaluates the signum boundary constraint: sgn(max(0, 4 - i))
    Ensures truncation limits remain within bounds for higher index elements.
    """
    inner_val = max(0, 4 - i)
    # Python equivalent of signum function (-1, 0, or 1)
    if inner_val > 0:
        return 1
    elif inner_val < 0:
        return -1
    else:
        return 0


# =============================================================================
# BLOCK 3: EXECUTION ENTRY POINT (TEST CASES FOR IMAGE 3 LOGIC)
# =============================================================================
if __name__ == "__main__":
    print("Running Piecewise Step-Size & Signum Tests for Image 3...")
    
    # Test sample step sizes (e.g., hi = 1, hj = 3)
    test_hi = 1
    test_hj = 3
    
    print(f"Testing step configuration: hi = {test_hi}, hj = {test_hj}")
    for index in range(4):
        result = evaluate_piecewise_qi(i=index, j=3, hi=test_hi, hj=test_hj)
        signum_res = evaluate_signum_bound(index)
        print(f"Index i={index} -> Piecewise Match: {result} | Signum Bound: {signum_res}")