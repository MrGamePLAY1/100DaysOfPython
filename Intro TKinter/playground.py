def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(5, 6, 7, 8))


def calculate(**kwargs):
    print(kwargs)


calculate(name='Craig', surname='Sheehy')


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.colour = kwargs.get('colour')


my_car = Car(make='Audi', model='R8')
print(my_car.colour)
