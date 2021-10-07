from car import Car
if __name__ == "__main__":
    print("Hola mundo")
    car = Car()
    car.license = "AMS234"
    car.drive = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "ASE546"
    car2.drive = "Adriana "
    print(vars(car2))