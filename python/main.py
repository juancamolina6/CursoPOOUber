from car import Car
from acoount import Account
if __name__ == "__main__":
    print("Hola mundo")
    car = Car("AMS234", Account("Adry Ardila", "AND876"))
    print(vars(car))
    print(vars(car.drive))