from lab5.polynom.mon import Mon
from operator import inv
from sortedcontainers import SortedList


class Pol:
	"""
	Class that represents polinomials
	e.x. -8x^3 + 4x^2 - 0.12x + 4
	with implemented addition, multiplication and evaluation for value x
	"""
	def __init__(self, mons=None):
		if mons is None:
			mons = [Mon(0, 0)]
		self.mons = SortedList(mons, inv)
		self.short()

	def eval(self, x):
		if not isinstance(x, (int, float)):
			raise TypeError(f"Cannot evaluate polynom for '{x}'")
		return sum([mon.eval(x) for mon in self.mons])

	def short(self):
		shorten = SortedList(key=inv)
		i = 0
		while i < len(self.mons):
			mon = self.mons[i]
			while i + 1 < len(self.mons) and mon.get_degree() == self.mons[i + 1].get_degree():
				i += 1
				mon += self.mons[i]
			shorten.add(mon)
			i += 1
		self.mons = SortedList(filter(lambda m: not mon.is_zero(), shorten), inv)

	def __call__(self, *args, **kwargs):
		if len(args) > 1:
			raise TypeError(f"Cannot evaluate polynom for more than one argument")
		else:
			return self.eval(args[0])

	def __add__(self, other):
		if isinstance(other, (int, float)):
			return self + Mon(other)
		elif isinstance(other, Mon):
			return Pol(self.mons + [other])
		elif isinstance(other, Pol):
			return Pol(self.mons + other.mons)
		else:
			raise TypeError(f"Cannot add '{type(other)}' to pol")

	def __mul__(self, other):
		if isinstance(other, (int, float, Mon)):
			return Pol([mon * other for mon in self.mons])
		elif isinstance(other, Pol):
			mons = []
			for a in self.mons:
				for b in other.mons:
					mons.append(a * b)
			return Pol(mons)
		else:
			raise TypeError(f"Cannot multiply polynom by '{type(other)}'")

	def __truediv__(self, other):
		if isinstance(other, (int, float)):
			return self / Mon(other, 0)
		elif isinstance(other, Mon):
			for i in range(len(self.mons)):
				self.mons[i] = self.mons[i] / other
		else:
			raise TypeError(f"Cannot divide polynom by '{type(other)}'")

	def __len__(self):
		return len(self.mons)

	def __repr__(self):
		s = ''
		b = True
		for mon in self.mons:
			if b:
				s += str(mon)
				b = False
			else:
				s += mon.to_str(True, 2)
		return s

	def __str__(self):
		return self.__repr__()
