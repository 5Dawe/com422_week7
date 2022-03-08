from Vehicle import Vehicle
import json

class Carpark:

    def __init__(self, capacity):
        self.spaces = self.load_data_from_file()
        self.capacity = capacity

    def load_data_from_file(self):
        cars = []
        try:
            with open("data/vehicles.json", "rt") as file:
                cp = json.loads(file.readlines()[0])
                for car in cp["spaces"]:
                    cars.append(Vehicle(car["reg"], car["type"]))
        except:
            pass

        return cars


    def save_to_file(self):
        with open("data/vehicles.json", "wt") as file:
            #for vehicle in self.spaces:
            #    file.write(json.dumps(vehicle.__dict__))
            file.write(json.dumps(self.__dict__, default=obj_dict))

    def add_car(self, car):
        if len(self.spaces) < self.capacity and (car.type == "Car" or car.type == "Emergency") and not self.is_duplicate(car.reg):
            self.spaces.append(car)
            return True
        return False

    def is_duplicate(self, reg_num):
        for car in self.spaces:
            if car.reg == reg_num:
                return True
        return False

    def remove_car(self, reg):
        for car in self.spaces:
            if car.reg == reg:
                self.spaces.remove(car)
                return True
        return False


def obj_dict(obj):
    return obj.__dict__
