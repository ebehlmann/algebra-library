import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        result = []
        i = 0
        while i < len(self.coordinates):
            result.append(self.coordinates[i] + v.coordinates[i])
            i+=1
        return result

    def subtract(self, v):
        result = []
        i = 0
        while i < len(self.coordinates):
            result.append(self.coordinates[i] - v.coordinates[i])
            i+=1
        return result

    def multiply(self, scalar):
        result = []
        for coord in self.coordinates:
            result.append(coord * scalar)
        return result

    def find_magnitude(self):
        sum = 0
        for coord in self.coordinates:
            sum += coord ** 2
        return math.sqrt(sum)

    def normalize(self):
        try:
            return self.multiply(1/self.find_magnitude())
        except ZeroDivisionError:
            raise Exception('Cannot normalize zero vector')

    def is_zero(self, tolerance=1e-10):
        if self.find_magnitude() < tolerance:
            return True
        else:
            return False

    def find_dot_product(self, v):
        sum = 0
        i = 0
        while i < len(self.coordinates):
            sum += self.coordinates[i] * v.coordinates[i]
            i+=1
        return sum

    def find_angle(self, v, unit='radians'):
        try:
            result = math.acos(self.find_dot_product(v) / (self.find_magnitude() * v.find_magnitude()))
            if unit == 'degrees':
                return math.degrees(result)
            else:
                return result
        except ZeroVectorError:
            raise Exception('Cannot compute an angle with the zero vector')

    def is_parallel(self, v):
        if self.is_zero() or v.is_zero():
            return True
        elif self.find_angle(v) == 0 or self.find_angle(v) == math.pi:
            return True
        else:
            return False

    def is_orthogonal(self, v, tolerance=1e-10):
        result = abs(self.find_dot_product(v))
        if result < tolerance:
            return True
        else:
            return False

vector1 = Vector([-7.579, -7.88])
vector2 = Vector([22.737, 23.64])

vector3 = Vector([-2.029, 9.97, 4.172])
vector4 = Vector([-9.231, -6.639, -7.245])

vector5 = Vector([-2.328, -7.284, -1.214])
vector6 = Vector([-1.821, 1.072, -2.94])

vector7 = Vector([2.118, 4.827])
vector8 = Vector([0, 0])

print('is_orthogonal')
print vector1.is_orthogonal(vector2)
print vector3.is_orthogonal(vector4)
print vector5.is_orthogonal(vector6)
print vector7.is_orthogonal(vector8)
print('is_parallel')
print vector1.is_parallel(vector2)
print vector3.is_parallel(vector4)
print vector5.is_parallel(vector6)
print vector7.is_parallel(vector8)
