import math

# All intervals are considered closed.
class interval:
    def __init__(self, end1, end2):
        end1 = float(end1)
        end2 = float(end2)
        # The arguments can be given out of order. This saves a bunch of repeated code to put the arguments in order when constructing intervals.
        self.min = min(end1, end2)
        self.max = max(end1, end2)
    def __eq__(self, other):
        return self.min == other.min and self.max == other.max
    def __pos__(self):
        return interval(self.min, self.max)
    def __neg__(self):
        return interval(-self.max, -self.min)
    def __abs__(self):
        if 0 <= self.min:
            return +self
        elif self.max <= 0:
            return -self
        else:
            return interval(0, max(abs(self.min), self.max))
    def __add__(self, other):
        return interval(self.min + other.min, self.max + other.max)
    def __sub__(self, other):
        return interval(self.min - other.max, self.max - other.min)
    def __mul__(self, other):
        corners = self.min * other.min, self.min * other.max, self.max * other.min, self.max * other.max
        return interval(min(corners), max(corners))
    def __truediv__(self, other):
        if other.min <= 0 and 0 <= other.max:
            # The divisor interval contains zero.
            raise ValueError("division by zero is undefined")
        corners = self.min / other.min, self.min / other.max, self.max / other.min, self.max / other.max
        return interval(min(corners), max(corners))
    # As exponents in the sciences are usually constants, this power method takes an integer as the exponent.
    def __pow__(self, other):
        if other < 0 and self.min <= 0 and 0 <= self.max:
            raise ValueError("negative power of zero is undefined")
        return interval(self.min ** other, self.max ** other) # This relies on the constructor being able to deal with arguments out of order.
    def sin(self):
        if (self.min + math.pi / 2) // (2 * math.pi)  < (self.max + math.pi / 2) // (2 * math.pi):
            # The interval crosses a trough.
            _min = -1
        else:
            _min = min(math.sin(self.min), math.sin(self.max))
        if (self.min - math.pi / 2) // (2 * math.pi)  < (self.max - math.pi / 2) // (2 * math.pi):
            # The interval crosses a peak.
            _max = 1
        else:
            _max = max(math.sin(self.min), math.sin(self.max))
        return interval(_min, _max)
    def cos(self):
        if (self.min + math.pi) // (2 * math.pi)  < (self.max + math.pi) // (2 * math.pi):
            # The interval crosses a trough.
            _min = -1
        else:
            _min = min(math.cos(self.min), math.cos(self.max))
        if self.min // (2 * math.pi)  < self.max // (2 * math.pi):
            # The interval crosses a peak.
            _max = 1
        else:
            _max = max(math.cos(self.min), math.cos(self.max))
        return interval(_min, _max)
    def tan(self):
        if (self.min - math.pi / 2) // math.pi < (self.max - math.pi / 2) // math.pi:
            # The interval crosses a vertical asymptote.
            raise ValueError("tangent of zero is undefined")
        return interval(math.tan(self.min), math.tan(self.max))
    # As bases are usually constants in the natural sciences, this logarithm function takesan integer as the base, with math.e as the default (just like math.log).
    def log(*args):
        if args[0].min <= 0:
            # The interval contains non-positive numbers.
            raise ValueError("natural logarithm of non-positive number is undefined")
        # This relies on the constructor being able to deal with arguments out of order.
        return interval(math.log(args[0].min, *args[1:]), math.log(args[0].max, *args[1:]))
    def __str__(self):
        return f"[{self.min}, {self.max}]"
    def __repr__(self):
        return f"interval({self.min}, {self.max})"

def sin(interval):
    return interval.sin()

def cos(interval):
    return interval.cos()

def tan(interval):
    return interval.tan()

def log(*args):
    return interval.log(*args)
