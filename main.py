termek = [[112, 45, 36], [113, 49, 38], [114, 47, 39], [115, 50, 30], [116, 20, 12], [117, 36, 25], [118, 44, 36], [119, 30, 28], [120, 41, 34]] ## [Tanterem szam, alapterulet, ferohely]


def task_1():
    array = [i[2] for i in termek]
    return sum(array)

def task_2():
    array = [i[0] for i in termek if i[2] >= 36]
    return array

def task_3():
    array = [i[1] for i in termek]
    return max(array)

def task_4():
    return [i for i in termek if i not in task_2()]

def task_5():
    b = False
    for i in termek:
       b = not(i[1] < 30)
    return b