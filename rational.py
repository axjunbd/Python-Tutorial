class Rational:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
            
        # Reduce the fraction by finding the greatest common divisor using Euclid's Algorithm
        common = self._gcd(abs(numerator), abs(denominator))
        
        self._numerator = numerator // common
        self._denominator = denominator // common
        
        # Ensure the negative sign is attached to the numerator
        if self._denominator < 0:
            self._numerator = -self._numerator
            self._denominator = -self._denominator

    @staticmethod
    def _gcd(a, b):
        """Euclid's Algorithm for calculating GCD."""
        while b != 0:
            a, b = b, a % b
        return a

    # Accessors
    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self._denominator

    def __str__(self):
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"

    # Overloading arithmetic operators
    def __add__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_num = self._numerator * other.get_denominator() + other.get_numerator() * self._denominator
        new_den = self._denominator * other.get_denominator()
        return Rational(new_num, new_den)

    def __sub__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_num = self._numerator * other.get_denominator() - other.get_numerator() * self._denominator
        new_den = self._denominator * other.get_denominator()
        return Rational(new_num, new_den)

    def __mul__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        new_num = self._numerator * other.get_numerator()
        new_den = self._denominator * other.get_denominator()
        return Rational(new_num, new_den)

    # Overloading relational operators
    def __eq__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self._numerator == other.get_numerator() and self._denominator == other.get_denominator()

    def __lt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self._numerator * other.get_denominator() < other.get_numerator() * self._denominator

    def __gt__(self, other):
        if not isinstance(other, Rational):
            return NotImplemented
        return self._numerator * other.get_denominator() > other.get_numerator() * self._denominator

# Testing the Rational class
if __name__ == "__main__":
    r1 = Rational(1, 4)
    r2 = Rational(1, 2)
    
    print(f"r1 = {r1}")
    print(f"r2 = {r2}")
    
    # Adding
    print(f"r1 + r2 = {r1 + r2}")
    
    # Subtracting
    print(f"r1 - r2 = {r1 - r2}")
    
    # Multiplying
    print(f"r1 * r2 = {r1 * r2}")
    
    # Relational Tests
    print(f"r1 == r2 : {r1 == r2}")
    print(f"r1 < r2  : {r1 < r2}")
    print(f"r1 > r2  : {r1 > r2}")
