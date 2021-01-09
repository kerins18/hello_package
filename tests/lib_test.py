# -*- coding: UTF-8 -*-

# Import from standard library
from second_package.lib import hello



def test_hello():

    assert hello('Ian') == 'Hello Ian'
    assert hello('') == 'Hello '
    assert hello(0) == 'Hello 0'

