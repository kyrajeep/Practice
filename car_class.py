import math
import os
import random
import re
import sys


class Car:
    def __init__(self, max_speed, unit):
        self.max_speed = max_speed
        self.unit = unit
    def getter(self, max_speed, unit):
        print("Car with the maximum speed of {0} {1}".format(max_speed, unit))
        return
class Boat:
    def __init__(self, max_speed_knots):
        self.max_s = max_speed_knots
    def maxspeed(self, max_s):
        print("Boat with the maximum speed of {} knots".format(max_s))
        return


if __name__ == '__main__':
    #car = Car(max_speed, unit)
    #car.getter(max_speed,unit)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        args = input().split()
        vehicle_type, params = args[0], args[1:]
        if vehicle_type == "car":
            max_speed, speed_unit = int(params[0]), params[1]
            vehicle = Car(max_speed, speed_unit)
            vehicle.getter(max_speed, speed_unit)
        elif vehicle_type == "boat":
            max_speed = int(params[0])
            vehicle = Boat(max_speed)
            vehicle.maxspeed(max_speed)
        else:
            raise ValueError("invalid vehicle type")
        fptr.write("%s\n" % vehicle)
    fptr.close()
