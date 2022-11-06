# -*- coding: UTF-8 -*-
'''
@Time: 2022/6/21 6:17 下午
@author: nicole1010
'''

import os

def getpath(filepath):
    """
    :param filepath:
    :return:返回绝对路径
    """
    PATH = lambda p: os.path.abspath(
        os.path.join(os.path.dirname(__file__), p)
    )
    fpath = PATH(filepath)
    print(fpath)
    return fpath

def whether_path_exists(path) -> object:
    """
    判断 path 是否存在，返回true or false
    """
    return os.path.exists(getpath(path))

def create_file(relative_path):
    """
    如果文件不存在，自动创建文件
    :param relative_path:
    :return:
    """
    filepath = getpath(relative_path)
    if not whether_path_exists(filepath):
        file = open(filepath, 'a+')
        file.close()

create_file("/logExe/uilog/uicaseLog.txt")
