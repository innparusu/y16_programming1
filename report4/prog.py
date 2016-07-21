#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

def parm(ary, r, element=None, out=None):
    if (element is None):
        element = []

    if (out is None):
        out = []

    if (len(element) == r):
        out.append(element[:])
        return

    for i in range(len(ary)):
        ary_copy = ary[:]
        element_copy = element[:]
        element_copy.append(ary_copy[i])
        del ary_copy[i]
        parm(ary_copy, r, element_copy, out)
    return out

def permutation(ary, r):
    """ 順列を出す
    >>> permutation([1,2,3,4], 2)
    [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
    """
    if (r > len(ary)):
        return False
    return parm(ary, r)

def distance(x1, y1, x2, y2):
    """ 距離を求める
    >>> distance(0, 0, 1 , 0)
    1.0
    >>> distance(0, 0, 0 , 1)
    1.0
    >>> distance(2, 4, 4 , 8)
    4.47213595499958
    """
    return math.sqrt((x2-x1)**2 + (y2 - y1) **2)

def read_city_file(filename):
    """ ファイルを読み込んで, 都市の数とその座標を返す
    >>> read_city_file('input1.txt')
    (8, [[20, 20], [120, 20], [220, 20], [70, 120], [170, 120], [270, 120], [20, 220], [120, 220]])
    """
    with open(filename, 'r') as file:
        city_num = int(file.readline().strip())
        city_list = []
        for line in file.readlines():
            city_point = list(map(int, line.strip().split(' ')))
            city_list.append(city_point)
    return (city_num, city_list)

def calc_path_distance(path, city_list):
    """ 渡されたpathの距離を計算するよ!
    """
    dist = 0
    for i in range(len(path) - 1):
        city_point = city_list[path[i]]
        next_city_point = city_list[path[i+1]]
        dist += distance(*city_point, *next_city_point)

    return dist

def calc_min_path_distance(path_list, city_list):
    """ 与えられたpath_listとcity_listから最小の距離に成るものを求めるよ！
    """
    path_list = list(map(lambda path: [0]+path+[0], path_list))
    path_distances = [(calc_path_distance(path, city_list), path) for path in path_list]
    return min(path_distances, key=(lambda tumple: tumple[0]))
 
def test(filename):
    city_num, city_list = read_city_file(filename)
    path_list = permutation(list(range(city_num))[1:], city_num - 1)
    min_distance, min_path = calc_min_path_distance(path_list, city_list)
    print("city_num = {0}".format(city_num))
    print(city_list)
    print("min_dist = {0}, min_path = {1}".format(min_distance, min_path))

if (__name__ == "__main__"):
    import doctest
    doctest.testmod()
    if (len(sys.argv) != 2):
        print("invalid arguments")
        print("./prog.py input_file")
        sys.exit(1)
    filename = sys.argv[1].strip()
    test(filename)
