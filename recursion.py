def fibonacci(n):
  # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    """
    Find greatest common divisor using Euclid's algorithm.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Greatest common divisor of a and b
    """
    # Base case
    if b == 0:
        return abs(a)
    
    # Recursive case
    return gcd(b, a % b)


def compareTo(s1, s2):
    """
    Compare two strings recursively.
    
    Args:
        s1: First string
        s2: Second string
        
    Returns:
        Negative if s1 < s2, 0 if equal, positive if s1 > s2
    """
    # Base cases
    if not s1 and not s2:  # Both empty
        return 0
    if not s1:  # First is empty
        return -1
    if not s2:  # Second is empty
        return 1
    
    # Compare first characters
    if s1[0] < s2[0]:
        return -1
    if s1[0] > s2[0]:
        return 1
    
    # First characters match, check rest of string
    return compareTo(s1[1:], s2[1:])


# Simple test cases
if __name__ == "__main__":
    # Test fibonacci
    print("Fibonacci tests:")
    for i in range(7):
        print(f"fibonacci({i}) = {fibonacci(i)}")
    
    # Test gcd
    print("\nGCD tests:")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print(f"gcd(54, 24) = {gcd(54, 24)}")
    
    # Test compareTo
    print("\nString comparison tests:")
    print(f"'apple' vs 'apple': {compareTo('apple', 'apple')}")
    print(f"'apple' vs 'banana': {compareTo('apple', 'banana')}")
    print(f"'banana' vs 'apple': {compareTo('banana', 'apple')}")
