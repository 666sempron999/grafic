# -*- coding: utf-8 -*-

def from_vectors_to_segments(sequence):
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


sequence1 = [11, 16, 22, 34, 35, 36, 37, 38, 39, 44, 45, 46, 47, 48]

sequence2 = [0,1,2,3,4,5,6,8,9,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,53,54,55,56,57,58,59,60,61,62,63,64,65,66,69,70,72,73,74,75,76,77,78,79,80,81,82,83,85,86,87,88,89,90,92,93,94,96,97,98,101,102,103,104,105,106,107,109,110,111,112]

print(from_vectors_to_segments(sequence1))

print("------------------------------------")
print(from_vectors_to_segments(sequence2))