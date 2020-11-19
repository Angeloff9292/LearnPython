import math

def calc_sqeare(ab, ac, bc):
    if ab <= 0 or ac <= 0 or bc <= 0:
        raise InvalidTriangelError("One of the sides is less or eqal to zero.")
    else:
        p = (ab + ac + bc)/2
        s = math.sqrt(p* (p - ab) * (p - ac) * (p - bc))
        return s
    print(f'Not correct sides number')

my_numbers = int(input("Enter number:"))
    

print(calc_sqeare(my_numbers, 8, 8))


class InvalidTriangelError(Exception):
    """Raised when a triangle has invalid sides"""