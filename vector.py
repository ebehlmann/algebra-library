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

vector1 = Vector([8.218, -9.341])
vector2 = Vector([-1.129, 2.111])
print vector1.add(vector2)

vector3 = Vector([7.119, 8.215])
vector4 = Vector([-8.223, 0.878])
print vector3.subtract(vector4)

vector5 = Vector([1.671, -1.012, -0.318])
print vector5.multiply(7.41)