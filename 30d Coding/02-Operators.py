#!/bin/python3

import math
import os
import random
import re
import sys

meal_cost = 0.0
tip_percent = 0
tax_percent = 0

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    if __name__ == '__main__':
        meal_cost = float(input())

        tip_percent = int(input())

        tax_percent = int(input())

        tip = meal_cost * (tip_percent / 100)
        tax = meal_cost * (tax_percent / 100)
        total_cost = round(meal_cost + tip + tax)

    print(total_cost)
    
solve(meal_cost, tip_percent, tax_percent)
