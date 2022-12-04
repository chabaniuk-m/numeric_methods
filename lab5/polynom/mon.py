class Mon:
    """
    Class that represents monomial
    like 4x or -8.4 or 0.03x^34
    """

    def __init__(self, coeff: float = 0, degree: float = 0):
        self._coeff = coeff
        self._degree = degree

    def get_coeff(self) -> float:
        return self._coeff

    def get_degree(self) -> float:
        return self._degree

    def is_zero(self) -> bool:
        return self._coeff == 0

    def eval(self, x) -> float:
        if isinstance(x, int) or isinstance(x, float):
            return self._coeff * x ** self._degree
        else:
            raise TypeError(f'Cannot calculate value of {self.to_str()} for input type {type(x)}')

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Mon(self._coeff * other, self._degree)
        elif isinstance(other, Mon):
            return Mon(self._coeff * other.get_coeff(), self._degree + other.get_degree())
        else:
            raise ValueError

    def __add__(self, other):
        if isinstance(other, Mon) and other._degree == self._degree:
            return Mon(self._coeff + other._coeff, self._degree)
        else:
            raise ValueError("Incompatible types for addition")

    def to_str(self, with_plus: bool = False, rnd: int = 2) -> str:
        c = (round(self._coeff, rnd) if rnd != 0 else round(self._coeff)) if rnd != 100 else self._coeff
        d = self._degree
        if c == 0:
            return " + 0" if with_plus else "0"
        elif d == 0:
            if c < 0:
                return f" - {abs(c)}" if with_plus else str(c)
            else:
                return f" + {c}" if with_plus else str(c)
        elif d == 1:
            if c == -1:
                return f' - x' if with_plus else '-x'
            elif c < 0:
                return f" - {abs(c)}x" if with_plus else str(c) + 'x'
            elif c == 1:
                return f' + x' if with_plus else 'x'
            else:
                return f" + {c}x" if with_plus else str(c) + 'x'
        else:
            if c == -1:
                return f' - x^{d}' if with_plus else f'-x^{d}'
            elif c < 0:
                return f" - {abs(c)}x^{d}" if with_plus else f"-{abs(c)}x^{d}"
            elif c == 1:
                return f' + x^{d}' if with_plus else f'x^{d}'
            else:
                return f" + {c}x^{d}" if with_plus else f"{c}x^{d}"

    def __str__(self):
        return self.to_str()

    def __repr__(self):
        return self.to_str()

    def __lt__(self, other):
        if isinstance(other, Mon):
            return self._degree < other._degree
        elif isinstance(other, int) or isinstance(other, float):
            return self._degree < 0
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, Mon):
            return self._degree > other._degree
        elif isinstance(other, int) or isinstance(other, float):
            return self._degree > 0
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Mon):
            return self._degree == other._degree
        elif isinstance(other, int) or isinstance(other, float):
            return self._degree == 0
        else:
            raise TypeError

    def __hash__(self):
        return int(self._coeff + 31 * self._degree)

    def __invert__(self):
        return Mon(1 / self._coeff, -self._degree) if self._coeff != 0 else Mon(float('inf'), -self._degree)
