#!/usr/bin/env python3

# Created by: Jason Grace
# Created on: October 12th, 2023
# This program calculates and displays the area and perimeter of a
# circle with radius 24 mm.

import math


def main():
    print("For a circle that has a radius")
    print("of 24 mm:")
    print("")
    print("Area = {:.2f} mm^2".format(math.pi * 24**2))
    print("Perimeter = {:.2f} mm".format(2 * math.pi * 24))


if __name__ == "__main__":
    main()
