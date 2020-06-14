from Class.SortClass import *
from numpy import random


def sortFunction():
    array = []

    for i in range(0, 100):
        array.append(random.randint(-200, 200))

    sort_obj = SortClass(array)
    print("Origin array:")
    sort_obj.printResult()
    sort_obj.quickSort()
    print("Sorted array:")
    sort_obj.printResult()


sortFunction()
