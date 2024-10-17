def sort(width, height, length, mass):
    """
    Sorts a package based on its dimensions and mass to the appropriate stack.

    Args:
        width: Width of the package in centimeters (cm).
        height: Height of the package in centimeters (cm).
        length: Length of the package in centimeters (cm).
        mass: Mass of the package in kilograms (kg).

    Returns:
        A string indicating the designated stack for the package:
            - "STANDARD": Standard package (not bulky or heavy).
            - "SPECIAL": Bulky or heavy package.
            - "REJECTED": Package that is both bulky and heavy.
    """
    # Calculate volume
    volume = width * height * length

    # Check if package is bulky
    is_bulky = volume >= 1000000 or max(width, height, length) >= 150

    # Check if package is heavy
    is_heavy = mass >= 20

    # Determine the appropriate stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

# Test cases
def run_tests():
    test_cases = [
        # (width, height, length, mass, expected_result)
        (100, 100, 100, 10, "STANDARD"),  # Standard package
        (150, 50, 50, 10, "SPECIAL"),     # Bulky due to one dimension
        (100, 100, 100, 20, "SPECIAL"),   # Heavy package
        (150, 150, 150, 20, "REJECTED"),  # Both bulky and heavy
        (10, 10, 10000, 5, "SPECIAL"),    # Bulky due to volume
        (149, 149, 149, 19, "STANDARD"),  # Just under all thresholds
        (0, 0, 0, 0, "STANDARD"),         # Edge case: zero dimensions and mass
    ]

    for i, (width, height, length, mass, expected) in enumerate(test_cases, 1):
        result = sort(width, height, length, mass)
        print(f"Test {i}: {'PASS' if result == expected else 'FAIL'}")
        print(f"  Input: width={width}, height={height}, length={length}, mass={mass}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result}\n")

# Run the tests
run_tests()

"""
Output of above test run

/usr/local/bin/python3.11 /Users/srinivasukolli/personal_projects/robo-package-sorter/robo_package_sort.py 
Test 1: FAIL
  Input: width=100, height=100, length=100, mass=10
  Expected: STANDARD
  Got: SPECIAL

Test 2: PASS
  Input: width=150, height=50, length=50, mass=10
  Expected: SPECIAL
  Got: SPECIAL

Test 3: FAIL
  Input: width=100, height=100, length=100, mass=20
  Expected: SPECIAL
  Got: REJECTED

Test 4: PASS
  Input: width=150, height=150, length=150, mass=20
  Expected: REJECTED
  Got: REJECTED

Test 5: PASS
  Input: width=10, height=10, length=10000, mass=5
  Expected: SPECIAL
  Got: SPECIAL

Test 6: FAIL
  Input: width=149, height=149, length=149, mass=19
  Expected: STANDARD
  Got: SPECIAL

Test 7: PASS
  Input: width=0, height=0, length=0, mass=0
  Expected: STANDARD
  Got: STANDARD

Process finished with exit code 0
"""