"""Task 1/2"""
import time


class Auto:
    """parent class  'Auto'"""

    def __init__(self,
                 brand: str, age: int, color: str,
                 mark: str, weight: int):
        # initializing Auto attributes

        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        """output of a message about the movement of a car"""

        print('move')

    def birthday(self):
        """increasing the age of the car by 1"""

        self.age += 1
        return self.age

    def stop(self):
        """output of a message about a car stop"""

        print('stop')


class Truck(Auto):
    """child class Auto"""

    def __init__(self,
                 brand: str, age: int, color: str, mark: str,
                 weight: int, max_load: int):
        # initializing parent attributes and adding an attribute 'max_load'

        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        """redefined the method 'move'"""

        print('attention')
        super().move()

    def load(self):
        """a method that makes a delay between output of 1 second"""

        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    """child class Auto"""

    def __init__(self,
                 brand: str, age: int, color: str, mark: str,
                 weight: int, max_speed: int):
        # initializing parent attributes and adding an attribute 'max_speed'

        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        """redefined the method 'move' and next 'max speed'"""

        super().move()
        print('max speed is ', self.max_speed, ' km/h')


# ------------------------------------------------------------------------------
str_0 = "=============TRUCK================="
str_1 = "==============CAR=================="
# ------------------------------------------------------------------------------

# TRUCK "IVECO"
truck_1 = Truck('IVECO', 1994, 'red', 'TRAKKER AD260T36', 5300, 20_000)

print(str_0)

print('Brand:' + truck_1.brand + '\n' +
      'Year of release: ' + str(truck_1.age) + '\n' +
      'Color: ' + truck_1.color + '\n' +
      'Mark: ' + truck_1.mark + '\n' +
      'Weight: ' + str(truck_1.weight) + '\n' +
      'Max. load: ' + str(truck_1.max_load))

truck_1.move()
truck_1.load()
print('Happy Birthday!!! <<', truck_1.birthday(), '>>', sep='')
truck_1.stop()
# ------------------------------------------------------------------------------

# TRUC "DAF"
truck_2 = Truck('DAF', 2013, 'Pink', 'XF 105', 4300, 15_000)

print(str_0)

print('Brand:' + truck_2.brand + '\n' +
      'Year of release: ' + str(truck_2.age) + '\n' +
      'Color: ' + truck_2.color + '\n' +
      'Mark: ' + truck_2.mark + '\n' +
      'Weight: ' + str(truck_2.weight) + '\n' +
      'Max. load: ' + str(truck_2.max_load))

truck_2.move()
truck_2.load()
print('Happy Birthday!!! <<', truck_2.birthday(), '>>', sep='')
truck_2.stop()
# ------------------------------------------------------------------------------

# CAR "BMW
car_1 = Car('BMW', 2003, 'black', '325i', 2100, 290)

print(str_1)

print('Brand:' + car_1.brand + '\n' +
      'Year of release: ' + str(car_1.age) + '\n' +
      'Color: ' + car_1.color + '\n' +
      'Mark: ' + car_1.mark + '\n' +
      'Weight: ' + str(car_1.weight))

car_1.move()
print('Happy Birthday!!! <<', car_1.birthday(), '>>', sep='')
car_1.stop()
# ------------------------------------------------------------------------------

# CAR MINI
car_2 = Car('MINI', 2019, 'black', 's300', 1800, 220)

print(str_1)

print('Brand:' + car_2.brand + '\n' +
      'Year of release: ' + str(car_2.age) + '\n' +
      'Color: ' + car_2.color + '\n' +
      'Mark: ' + car_2.mark + '\n' +
      'Weight: ' + str(car_2.weight))

car_2.move()
print('Happy Birthday!!! <<', car_2.birthday(), '>>', sep='')
car_2.stop()
