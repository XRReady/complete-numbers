# # Complex Number Typical Usage Patterns
# z = 3 + 4j                # Create complex number
# z = complex(3, 4)         # Alternative construction
# z.real * 0  -> 0.0       # Real component times zero
# z.imag * 0  -> 0.0       # Imaginary component times zero
# z * 0       -> 0j        # Whole complex number times zero

# # Complete Number Usage Patterns Derived From Complex Usage Patterns
# cu = 3 + 4j               # Create complete number
# cu = CompleteNumber(3, 4) # Alternative construction
# cu.real * 0  -> 3u        # Real component times zero
# cu.imag * 0  -> 4uj       # Imaginary component times zero
# cu * 0      -> 3u + 4uj   # Whole complete number times zero

from typing import Union, Tuple
import numbers
import cmath

class CompleteComponent:
    """Drop-in replacement for float that maintains absorption into U"""
    def __init__(self, value, component_type):
        self._value = float(value)
        self._type = component_type    # 'real' or 'imag'
    
    def __mul__(self, other):
        if other == 0:
            if self._type == 'real':
                # Real component times zero -> just the absorbed value
                return f"{self._value}u"
            else:  # imaginary
                # Imaginary component times zero -> just the absorbed value
                return f"{self._value}uj"
        else:
            # Non-zero multiplication - return just the float value
            return self._value * other
 
    def __truediv__(self, other):
        """
        Component division should behave like regular float division,
        raising ZeroDivisionError when dividing by zero
        """
        if other == 0:
            raise ZeroDivisionError("float division by zero")
        return self._value / other
    
    def __rtruediv__(self, other):
        if self._value == 0:
            raise ZeroDivisionError("float division by zero")
        return other / self._value

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __rtruediv__(self, other):
        """Implement reverse division"""
        # This handles cases like 1 / CompleteNumber
        return NotImplemented  # For now, we'll implement if needed 

    def __repr__(self):
        return str(self._value)
    
    def __float__(self):
        return self._value

class CompleteNumber:
    def __init__(self, real, imag, u_real=0, u_imag=0):
        self._real = float(real)
        self._imag = float(imag)
        self._u_real = float(u_real)
        self._u_imag = float(u_imag)
    
    @property
    def real(self):
        return CompleteComponent(self._real, 'real')
    
    @property
    def imag(self):
        return CompleteComponent(self._imag, 'imag')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                # Whole number times zero -> both components go to U
                return CompleteNumber(0, 0, self._real, self._imag)
            else:
                # Regular multiplication
                return CompleteNumber(self._real * other, self._imag * other)
        return NotImplemented
    
    def __truediv__(self, other):
        """
        Complete number division. Raises ZeroDivisionError if any non-absorbed
        components would be divided by zero.
        """
        if isinstance(other, (int, float)):
            if other == 0:
                # If there are any non-absorbed components, division by zero is undefined
                if self._real != 0 or self._imag != 0:
                    raise ZeroDivisionError("division by zero")
                # Only absorbed components present
                return CompleteNumber(
                    self._u_real,
                    self._u_imag
                )
            else:
                # Regular division
                return CompleteNumber(
                    self._real / other, 
                    self._imag / other,
                    self._u_real / other,
                    self._u_imag / other
                )
        return NotImplemented

    def __rtruediv__(self, other):
        """Implement reverse division"""
        if self._value == 0:
            raise ZeroDivisionError("division by zero")
        return other / self._value

    def __rmul__(self, other):
        return self.__mul__(other)

    def __repr__(self):
        parts = []
        if self._real != 0 or (self._imag == 0 and self._u_real == 0 and self._u_imag == 0):
            parts.append(str(self._real))
        if self._imag != 0:
            parts.append(f"{self._imag}j")
        if self._u_real != 0:
            parts.append(f"{self._u_real}u")
        if self._u_imag != 0:
            parts.append(f"{self._u_imag}uj")
            
        return " + ".join(parts).replace(" + -", " - ")
    
def test_basic_multiplication():
    """
    Test both complete number and complex number behaviors with multiplication.
    """
    print("\nBasic Multiplication Tests:")
    
    # Create a complete number
    cu = CompleteNumber(3, 4)  # 3 + 4j
    print(f"Initial number: {cu}")
    
    # Test 1: Whole number multiplication by 0
    result1 = cu * 0
    print(f"\nCase 1 - Whole number * 0:")
    print(f"({cu}) * 0 = {result1}")  # Should be 3u + 4uj
    
    # Test 2: Real component multiplication by 0
    result2 = cu.real * 0
    print(f"\nCase 2 - Real component * 0:")
    print(f"({cu}).real * 0 = {result2}")  # Should be 3u + 4j
    
    # Test 3: Imaginary component multiplication by 0
    result3 = cu.imag * 0
    print(f"\nCase 3 - Imaginary component * 0:")
    print(f"({cu}).imag * 0 = {result3}")  # Should be 3 + 4uj
    
    # Test 4: Verify normal multiplication still works
    print(f"\nVerification of normal multiplication:")
    print(f"Initial number: {cu}")
    result4 = cu * 1
    print(f"({cu}) * 1 = {result4}")  # Should be 3 + 4j
    result5 = cu.real * 1
    print(f"({cu}).real * 1 = {result5}")  # Should be 3
    result6 = cu.imag * 1
    print(f"({cu}).imag * 1 = {result6}")  # Should be 4
    
    return result1, result2, result3, result4, result5, result6

def test_basic_division():
    """
    Test division behavior, particularly division by zero cases.
    """
    print("\nBasic Division Tests:")
    
    # Create a complete number
    cu = CompleteNumber(3, 4)  # 3 + 4j
    print(f"Initial number: {cu}")
    
    # Test 1: Whole number after absorption divided by 0
    cu_absorbed = cu * 0  # First absorb into U
    try:
        result1 = cu_absorbed / 0
        print(f"\nCase 1 - Complete absorbed number / 0:")
        print(f"({cu_absorbed}) / 0 = {result1}")
    except ZeroDivisionError as e:
        print(f"({cu_absorbed}) / 0 -> ZeroDivisionError: {e}")
    
    # Test 2: Real component division by 0 (should raise exception)
    print(f"\nCase 2 - Real component / 0:")
    try:
        result2 = cu.real / 0
        print(f"({cu}).real / 0 = {result2}")
    except ZeroDivisionError as e:
        print(f"({cu}).real / 0 -> ZeroDivisionError: {e}")
    
    # Test 3: Imaginary component division by 0 (should raise exception)
    print(f"\nCase 3 - Imaginary component / 0:")
    try:
        result3 = cu.imag / 0
        print(f"({cu}).imag / 0 = {result3}")
    except ZeroDivisionError as e:
        print(f"({cu}).imag / 0 -> ZeroDivisionError: {e}")
    
    # Test 4: Pure absorbed components divided by 0
    cu_absorbed_only = CompleteNumber(0, 0, 3, 4)  # 3u + 4uj
    result4 = cu_absorbed_only / 0
    print(f"\nCase 4 - Pure absorbed components / 0:")
    print(f"({cu_absorbed_only}) / 0 = {result4}")  # Should recover original values

    return cu_absorbed, result4

def demonstrate_vanishing_summation():
    """
    Demonstrates how multiplication by zero represents the vanishing of the summation
    structure itself, not the removal of quantities. The complete number system
    preserves this structural information that would otherwise be lost.
    """
    print("\nVanishing Summation Structure Demonstration:")
    
    # Create complete numbers for our quantities
    box_quantity = CompleteNumber(5, 0)    # 5 as a quantity
    crate_quantity = CompleteNumber(3, 0)  # 3 as a quantity
    print(f"Initial quantities:")
    print(f"Box:   {box_quantity}")
    print(f"Crate: {crate_quantity}")
    
    # Demonstrate multiplication by zero (vanishing of summation structure)
    box_vanished = box_quantity * 0
    crate_vanished = crate_quantity * 0
    print(f"\nAfter multiplication by zero (vanishing of summation structure):")
    print(f"Box:   {box_vanished}")    # Should be 5u - preserving the vanished structure
    print(f"Crate: {crate_vanished}")  # Should be 3u - preserving the vanished structure
    
    # Add the vanished quantities (combining our structural information)
    total_vanished = CompleteNumber(
        0, 0, 
        box_vanished._u_real + crate_vanished._u_real,
        box_vanished._u_imag + crate_vanished._u_imag
    )
    print(f"\nCombined vanished structures:")
    print(f"Total: {total_vanished}")  # Should be 8u
    
    # Recover the original total through division by zero
    try:
        total = total_vanished / 0
        print(f"\nRecovered quantity from vanished structure:")
        print(f"Total: {total}")  # Should be 8
    except ZeroDivisionError as e:
        print(f"Error recovering total: {e}")
    
    return box_vanished, crate_vanished, total_vanished

def test_complete_number_system():
    """
    Comprehensive test suite for the complete number system implementation.
    """
    # First run multiplication tests
    print("\n=== Complete Number System Tests ===")
    results_mult = test_basic_multiplication()
    results_div = test_basic_division()
    results_vanishing = demonstrate_vanishing_summation()

if __name__ == "__main__":
    test_complete_number_system()
