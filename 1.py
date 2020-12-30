from math import pi
class TCircle:
    def __init__(self,r):
        self.r = r

    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self,value):
        value = int(value)
        if value <= 0:
            raise Exception('error')
        else:
            self.__r = value

    def s(self):
        return self.r * pi ** 2

    def p(self):
        return 2*pi*self.r

    def __add__(self, other):
        return TCircle(self.r + other.r)

    def __sub__(self, other):
        return TCircle(self.r - other.r)

    def __mul__(self, other):
        return self.r * other

    def da(self,value):
        value -= 1
        return value

    def __gt__(self, other):
        return self.r > other.r

    def __lt__(self, other):
        return self.r < other.r


c1 = TCircle(3)
print(c1.p())
