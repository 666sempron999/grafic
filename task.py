# -*- coding: utf-8 -*-

import random
import csv
import math
import matplotlib.pyplot as plt
import numpy as np


def GenerateRandomParametrs(number):
    """
    Генерация списка с произвольными числами.
    Входные параметры:
    number - число случайных элементов последовательности
    Возвращаемые значения:
    a - последовательность случайных элементов

    """

    a = []
    for i in range(0, number):
        a.append(random.randint(0, 500))

    return a


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


def CreateSpecialMassiveWithOverlapping(massiv, delitel):
    """
    формирование из одномерного массива двумерного с перекрытием.
    Входные параметры:
    massiv - входящая последовательность
    delitel - количество элементов в столбце
    Возвращаемые значения:
    result_massiv - последовательность с перекрытием участков

    """

    result_massiv = []
    inside_massiv = []
    wibdow_width = delitel

    mas_len = len(massiv)

    for i in range(0, mas_len):
        n = 0
        while wibdow_width > 0 and (mas_len > (i+n)):
            inside_massiv.append(massiv[i+n])
            wibdow_width -= 1
            n += 1

        wibdow_width = delitel
        if(len(inside_massiv) == delitel):
            result_massiv.append(inside_massiv)
        inside_massiv = []

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


def complexity_function(norman_array):
    """
    Данная функция из нормированной последовательности позволяет получить\
    функцию сложности
    Входные параметры:
    norman_array - входящая многомерная нормированная последовательность
    Возвращаемые значения:
    result_massiv - последовательность со значениями функции сложности

    """

    result_massiv = []
    first_part = norman_array[:2]
    last_part = norman_array[-2:]

    multiplay = 1

    last = 0.
    first = 0.

    index = 0

    while index < len(first_part[0]):

        multiplay = first_part[0][index] * first_part[1][index]
        first += multiplay
        multiplay = 1

        multiplay = last_part[0][index] * last_part[1][index]
        last += multiplay
        multiplay = 1

        index += 1

    result_massiv.append(first)

    multiplay = 1
    summa = 0

    for i in range(1, len(norman_array) - 1):
        left = norman_array[i - 1]
        center = norman_array[i]
        right = norman_array[i + 1]

        index = 0

        while index < len(left):
            summa += ((left[index] * center[index]) + (center[index] \
                                                    * right[index]))
            index += 1

        result_massiv.append(summa / 2)
        summa = 0

    result_massiv.append(last)

    return result_massiv


def special_trim(sequence):
    """
    Функция из необработанного списка возвращает список отрезков
    Принимает
    sequence - список координат по возрастанию
    Возвращает
    full - последовательность из отрезков

    """

    result_list = []
    inside_array = []

    #Добавить 0-й элемент
    result_list.append(sequence[0])

    total = len(sequence)
    i = 1

    #Это лайфхак, работает как попало...но главное что работает
    try:
        
        while (i < total):
            if sequence[i] - sequence[i-1] > 1:
                result_list.append(sequence[i])

            elif sequence[i] - sequence[i-1] == 1:
                inside_array.append(result_list[-1])
                del result_list[-1]
                while sequence[i] - sequence[i-1] == 1:
                    inside_array.append(sequence[i])
                    i += 1
                    
                result_list.append(inside_array)
                inside_array = []
                i = i-1

            i+=1

    except IndexError as e:
        result_list.append(inside_array)

    full = []

    for i in range(0, len(result_list)):
        if type(result_list[i]) != list:
            full.append(result_list[i])
        elif len(result_list[i]) > 1 and i % 2 != 0:
            
            full.append(max(result_list[i]))
        else:
            full.append(min(result_list[i]))
            full.append(max(result_list[i]))
        
    return full   



def draw_plot(chisla, complexity_array, parametr, number_of_point):
    """
    Функция для построения графика из функции сложности
    complexity_array - последовательность с функцие сложности 
    parametr - порог срабатывания
    number_of_point - количество точек в разбиении стартовой последовательности
    этот параметр только для выовда на экран
    Функция ничего не возвращает, только строит график
    """

    plt.subplot(211)
    plt.plot(complexity_array)
    plt.title('Функция сложности для ' + str(number_of_point) + ' точек в разбиении')
    indexes = [parametr] * len(complexity_array)
    porog = "Порог срабатывания " + str(parametr)
    plt.plot(indexes, 'r-', lw=2, label=porog)

    special_area_indexes = []

    print("Индексы для выделения!")

    for i in range(0, len(complexity_array)):
        if complexity_array[i] < parametr:
            special_area_indexes.append(i)
            print(i)

    plt.grid(True)
    plt.xlabel('Номер столбца')
    plt.ylabel('Значение функции сложности')
    plt.legend()


    plt.subplot(212)
    plt.title('Результирующий график')
    plt.plot(chisla)

    special_area_indexes = special_trim(special_area_indexes)

    for i in range(0, len(special_area_indexes),2):
        if i + 1 != len(special_area_indexes):
            plt.axvspan(special_area_indexes[i], special_area_indexes[i + 1], \
                color='red', alpha=0.3)

    plt.grid(True)
    plt.xlabel('Номер столбца')
    plt.ylabel('Значение функции сложности')

    plt.show()


if __name__ == "__main__":

    csv_path = "5000.csv" # Файл, который откроется в системе
    # with open(csv_path, "r") as f_obj:
    #     res = csv_reader(f_obj)

    res = csv_reader(csv_path)

    chisla = to_float(res)
    print("Считаный из файла массив")
    print(chisla)
    print("===========================================================")

    # number = int(input("Введите число для разбиение в последовательности (2,3...) - "))
    
    number = 5 # число для разбиения последовательности

    type_of_calculation = 2 # (1 - без перекрытия, 2 - с перекрытием)

    coeficient = 0.92 # тот самый коэфициент
    
    if type_of_calculation == 1:
        third_massiv = CreateSpecialMassive(chisla, number)
    else:
        third_massiv = CreateSpecialMassiveWithOverlapping(chisla, number)


    for idx, item in enumerate(third_massiv):
        print(idx + 1, "=>", third_massiv[idx])

    print("Длинна каждого участка")
    len_of_each_interval = LengthOfEachInterval(third_massiv)
    for idx, item in enumerate(len_of_each_interval):
        print(idx + 1, "=>", len_of_each_interval[idx])

    print("Нормированный по длинне массив")
    norman_array = NormateEachElements(third_massiv, len_of_each_interval)
    for idx, item in enumerate(norman_array):
        print(idx + 1, "=>", norman_array[idx])

    print("Функция сложности")
    complexity = complexity_function(norman_array)

    for idx, item in enumerate(complexity):
        print(idx + 1, "=>", complexity[idx])

    draw_plot(chisla, complexity, coeficient, number)
