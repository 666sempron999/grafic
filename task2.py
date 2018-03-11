# -*- coding: utf-8 -*-

import random
import csv
import math
import matplotlib.pyplot as plt
import numpy as np


import time
 
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()
         
    def __exit__(self, type, value, traceback):
        print("Executing time: {:.3f} sec".format(time.time() - self._startTime))


def to_float(result_list):
    """
    Преобразование строковых представлений в вещественно числовые\
    для расчётов
    Входные параметры:
    result_list - список строковых параметров
    Возвращаемые значения:
    float_list - преобразованый в вещественные числа список

    """

    float_list = list()
    for i in range(0, len(result_list)):
        float_list.append(float(result_list[i]))

    return float_list


def csv_reader(variables_file):
    """
    Чтение данных их csv файла
    Входные параметры:
    file_obj - дескриптор на файл
    Возвращаемые значения:
    result_list[0] - список значений, считанных из файла

    """

    reader = csv.reader(open(variables_file, 'r'))
    dict_list = []

    for line in reader:
        dict_list.append(line)

    dict_list = dict_list[0][0]
    dict_list = dict_list.split(";")

    return dict_list

def CreateSpecialMassive(massiv, delitel):
    """
    Формирование из одномерного массива двумерный, с заданым
    колличеством элементов
    Входные параметры:
    massiv - входящая последовательность
    delitel - количество элементов в столбце
    Возвращаемые значения:
    result_massiv - последовательность со столбцами

    """

    result_massiv = []
    inside_massiv = []

    inside_massiv = massiv[0:delitel]
    result_massiv.append(inside_massiv)

    inside_massiv = []

    for i in range(delitel - 1, len(massiv)):

        inside_massiv.append(massiv[i])

        if len(inside_massiv) == delitel:
            result_massiv.append(inside_massiv)
            inside_massiv = []
            inside_massiv.append(massiv[i])

    return result_massiv

def LengthOfEachInterval(massiv):
    """
    Подсчёт длинны каждого участка (корень из суммы квадратов каждого \
    элемента участка)
    Входные параметры:
    massiv - входящая многомерная последовательность
    Возвращаемые значения:
    len_massive - последовательность с длинами каждого участка

    """

    len_massive = []

    for i in range(0, len(massiv)):
        summ = 0
        for j in range(0, len(massiv[i])):
            summ += massiv[i][j] ** 2

        len_massive.append(math.sqrt(summ))

    return len_massive


def NormateEachElements(massiv, len_massive):
    """
    Нормирование каждого элемента на длину участка
    Входные параметры:
    massiv - входящая многомерная последовательность
    len_massive - последовательность с длинами каждого участка
    Возвращаемые значения:
    result_massiv - последовательность нормированными величинами

    """

    result_massiv = []
    inside_massiv = []

    for i in range(0, len(massiv)):
        delitel = len_massive[i]
        for j in range(0, len(massiv[i])):
            inside_massiv.append(massiv[i][j] / delitel)

        result_massiv.append(inside_massiv)
        inside_massiv = []
        delitel = 0

    return result_massiv

def create_c_parametr(norman_array):
    '''
    '''
    n = len(norman_array[0])
    c0 = (norman_array[0][0] + norman_array[0][1]) / 2

    fullArray = []
    fullArray.append(c0)
    inside_massiv = []

    for i in range(1, len(norman_array)):
        inside_massiv.append((1 / 2) * norman_array[i][0] * math.cos((2 * math.pi) / 2))
        inside_massiv.append((1 / 2) * norman_array[i][0] * math.sin((2 * math.pi) / 2))
        inside_massiv.append((1 / 2) * norman_array[i][1] * math.cos((4 * math.pi) / 2))
        inside_massiv.append((1 / 2) * norman_array[i][1] * math.sin((4 * math.pi) / 2))

        fullArray.append(inside_massiv)
        inside_massiv = []

    return fullArray

def create_psi_massive(norman_array, cArray):
    '''
    '''

    c0 = cArray[0]
    counter = len(norman_array)

    psiArray = []

    for i in range(1, counter):

        x1 = norman_array[i][0]
        x2 = norman_array[i][1]

        c11 = cArray[i][0]
        c12 = cArray[i][1]
        c21 = cArray[i][2]
        c22 = cArray[i][3]

        psi1 = ( x1 - (
                        (c0 / 2) + 
                        (
                            c11 * math.cos(2 * math.pi * 0.5) + 
                            c21 * math.cos(2 * math.pi)
                        ) + 
                        (
                            c12 * math.sin(2 * math.pi * 0.5) + 
                            c22 * math.sin(2 * math.pi)
                        )
                    )
                )**2

        psi2 = ( x2 - (
                        (c0 / 2) + 
                        (
                            c11 * math.cos(2 * math.pi) + 
                            c21 * math.cos(2 * math.pi * 2)
                        ) + 
                        (
                            c12 * math.sin(2 * math.pi) + 
                            c22 * math.sin(2 * math.pi * 2)
                        )
                    )
                )**2
        psiArray.append(psi1 + psi2)

    return psiArray


with Profiler() as p:

    if __name__ == "__main__":

        csv_path = "5000.csv" 

        res = csv_reader(csv_path)

        chisla = to_float(res)

        special_massive = CreateSpecialMassive(chisla, 2)

        len_of_each_interval = LengthOfEachInterval(special_massive)
        norman_array = NormateEachElements(special_massive, len_of_each_interval)

        cArray = create_c_parametr(norman_array)

        psiArray = create_psi_massive(norman_array, cArray)

        print(math.sqrt(sum(psiArray)))