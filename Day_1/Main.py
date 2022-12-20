import re
import os
import sys

def LoadData():
    input_val = []
    accumulator = []
    with open('input.txt') as inputFile:
        for line in inputFile:
            data = line.strip()
            if len(data) > 0:
                accumulator.append(int(data))
            else:
                input_val.append(accumulator)
                accumulator = []
        if len(accumulator) > 0:
            input_val.append(accumulator)
    return input_val

def RunTest1(input_number):
    print("Test 1")
    sum_array = list(map(sum, input_number))
    print("Solution: {0}".format(max(sum_array)))

def RunTest2(input_number):
    print("Test 2")
    sum_array = list(map(sum, input_number))
    sum_array.sort()
    top_3 = sum_array[-3:]
    print("Solution: {0}".format(sum(top_3)))

if __name__ == "__main__":
    data = LoadData()
    RunTest1(data)
    RunTest2(data)
