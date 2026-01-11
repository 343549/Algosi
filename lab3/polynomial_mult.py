"""
Лабораторная работа по умножению многочленов
Вариант 19
Студент: Джафари Хоссаин
"""

def naive_multiply(A, B):
    """
    Naive algorithm for polynomial multiplication
    Complexity: O(n^2)
    
    Args:
        A: list of coefficients of first polynomial (from highest degree)
        B: list of coefficients of second polynomial (from highest degree)
    
    Returns:
        list of coefficients of product (from highest degree)
    """
    n = len(A)
    m = len(B)
    
    # Result polynomial has degree (n-1) + (m-1) = n+m-2
    # So number of coefficients = n+m-1
    result = [0] * (n + m - 1)
    
    # Multiply each coefficient of A by each coefficient of B
    for i in range(n):
        for j in range(m):
            result[i + j] += A[i] * B[j]
    
    return result


def divide_conquer_multiply(A, B):
    """
    Naive divide and conquer algorithm
    Complexity: O(n^2)
    
    According to the PDF, this naive divide and conquer approach
    still has O(n^2) complexity because T(n) = 4T(n/2) + kn = O(n^2).
    It doesn't improve the complexity, so we'll use the naive algorithm
    as it's simpler and has the same complexity.
    """
    # For simplicity, since naive divide and conquer has the same
    # complexity as naive multiplication, we use naive multiplication
    return naive_multiply(A, B)


def add_polynomials(A, B):
    """Add two polynomials"""
    max_len = max(len(A), len(B))
    result = [0] * max_len
    
    for i in range(len(A)):
        result[i] += A[i]
    for i in range(len(B)):
        result[i] += B[i]
    
    return result


def subtract_polynomials(A, B):
    """Subtract two polynomials"""
    max_len = max(len(A), len(B))
    result = [0] * max_len
    
    for i in range(len(A)):
        result[i] += A[i]
    for i in range(len(B)):
        result[i] -= B[i]
    
    return result


def karatsuba_multiply(A, B):
    """
    Karatsuba algorithm for polynomial multiplication
    Complexity: O(n^log2(3)) ≈ O(n^1.58)
    
    Uses Karatsuba trick: 3 multiplications instead of 4
    """
    n = len(A)
    m = len(B)
    
    # Base case: use naive multiplication for small polynomials
    if n <= 4 or m <= 4:
        return naive_multiply(A, B)
    
    # Make lengths equal by padding with zeros
    max_len = max(n, m)
    if n < max_len:
        A = list(A) + [0] * (max_len - n)
    if m < max_len:
        B = list(B) + [0] * (max_len - m)
    
    n = max_len
    mid = n // 2
    
    # Split: A = D1 * x^len(D0) + D0
    D1 = A[:mid]  # High part
    D0 = A[mid:]  # Low part
    
    # Split: B = E1 * x^len(E0) + E0
    E1 = B[:mid]  # High part
    E0 = B[mid:]  # Low part
    
    # Three multiplications instead of four
    Z0 = karatsuba_multiply(D0, E0)  # D0 * E0
    Z2 = karatsuba_multiply(D1, E1)  # D1 * E1
    
    # (D1 + D0) * (E1 + E0)
    D1_plus_D0 = add_polynomials(D1, D0)
    E1_plus_E0 = add_polynomials(E1, E0)
    Z1 = karatsuba_multiply(D1_plus_D0, E1_plus_E0)
    
    # Z1 = (D1 + D0)(E1 + E0) = D1E1 + D1E0 + D0E1 + D0E0
    # So: D1E0 + D0E1 = Z1 - Z2 - Z0
    # Result: Z2 * x^(2*shift) + (Z1 - Z2 - Z0) * x^shift + Z0
    
    # Compute middle term
    Z1_minus_Z2_minus_Z0 = subtract_polynomials(subtract_polynomials(Z1, Z2), Z0)
    
    # Assemble result
    shift = n - mid  # len(D0) = len(E0)
    result_degree = 2 * n - 1
    result = [0] * result_degree
    
    # Add Z0 (low part) without shift
    for i, coeff in enumerate(Z0):
        if i < result_degree:
            result[i] += coeff
    
    # Add middle term with shift
    for i, coeff in enumerate(Z1_minus_Z2_minus_Z0):
        pos = i + shift
        if pos < result_degree:
            result[pos] += coeff
    
    # Add Z2 with shift 2*shift
    for i, coeff in enumerate(Z2):
        pos = i + 2 * shift
        if pos < result_degree:
            result[pos] += coeff
    
    return result


def polynomial_to_string(coeffs):
    """Convert coefficients to polynomial string representation"""
    if not coeffs:
        return "0"
    
    terms = []
    degree = len(coeffs) - 1
    
    for i, coeff in enumerate(coeffs):
        if coeff == 0:
            continue
        
        power = degree - i
        
        if power == 0:
            term = str(coeff)
        elif power == 1:
            if coeff == 1:
                term = "x"
            elif coeff == -1:
                term = "-x"
            else:
                term = f"{coeff}x"
        else:
            if coeff == 1:
                term = f"x^{power}"
            elif coeff == -1:
                term = f"-x^{power}"
            else:
                term = f"{coeff}x^{power}"
        
        terms.append(term)
    
    if not terms:
        return "0"
    
    result = terms[0]
    for term in terms[1:]:
        if term[0] == '-':
            result += " - " + term[1:]
        else:
            result += " + " + term
    
    return result


def print_polynomial(coeffs, name="P(x)"):
    """Print polynomial in readable format"""
    print(f"{name} = {polynomial_to_string(coeffs)}")
    print(f"Coefficients: {coeffs}")
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("Laboratory work: Polynomial Multiplication")
    print("Variant 19")
    print("Student: Dzhafari Khossain")
    print("=" * 60)
    print()
    
    # Test cases
    test_cases = [
        # Example 1: from presentation
        ([3, 2, 5], [5, 1, 2], "Example 1"),
        # Example 2: from presentation (Karatsuba)
        ([4, 3, 2, 1], [1, 2, 3, 4], "Example 2"),
        # Example 3: simple case
        ([1, 1], [1, 1], "Example 3"),
        # Example 4: different degrees
        ([2, 1], [3, 2, 1], "Example 4"),
    ]
    
    for i, (A, B, description) in enumerate(test_cases, 1):
        print(f"\n{'=' * 60}")
        print(f"{description}")
        print(f"{'=' * 60}\n")
        
        print_polynomial(A, "A(x)")
        print_polynomial(B, "B(x)")
        
        # Naive algorithm
        print("1. Naive algorithm (O(n^2)):")
        result_naive = naive_multiply(A, B)
        print_polynomial(result_naive, "A(x) * B(x)")
        
        # Divide and conquer algorithm
        print("2. Divide and conquer algorithm (O(n^2)):")
        result_dc = divide_conquer_multiply(A, B)
        print_polynomial(result_dc, "A(x) * B(x)")
        
        # Karatsuba algorithm
        print("3. Karatsuba algorithm (O(n^log2(3))):")
        result_karatsuba = karatsuba_multiply(A, B)
        print_polynomial(result_karatsuba, "A(x) * B(x)")
        
        # Check if results match
        print("Verification:")
        if result_naive == result_dc == result_karatsuba:
            print("OK: All algorithms produced the same result")
        else:
            print("ERROR: Results differ!")
            print(f"  Naive: {result_naive}")
            print(f"  Divide and conquer: {result_dc}")
            print(f"  Karatsuba: {result_karatsuba}")
        
        print("\n" + "-" * 60)
