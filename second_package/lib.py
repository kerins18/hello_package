# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for second_package Project
"""


def hello(text):
    return (f'Hello {text}')
 


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    result = hello('Ian')
    print(result)
