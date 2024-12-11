import argparse
class Car:
    def __init__(self, license_plate: str, make: str, year:int):
        self.license_plate = license_plate
        self.make = make
        self.year=year

    def __str__(self) -> str:
        print(f"{self.license_plate}, {self.make}, {self.year}")


parser = argparse.ArgumentParser()
parser.add_argument('-add', nargs=3, help="Argument to add new car in car list")
parser.add_argument('-view', help="Argument see car info")
args = parser.parse_args()

cars=[]
if args.add:
    license_plate,make,year=args.add
    cars.append(Car(license_plate,make,year))
if args.view:
    license_plate=args.view
    for car in cars:
        if car.license_plate==license_plate:
            print(car)
            break
