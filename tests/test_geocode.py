'''
NOTE: Run this from the top-level directory
'''

import os
from os.path import join

import sys
sys.path.insert(0, join(os.getcwd(), 'geo_service_src'))

from geocode import get_coordinate

def test_actual_location():
    assert get_coordinate('Wenzhou') == [120.6915792, 27.9958689]

def test_random_string():
    assert get_coordinate('ahsdfgkasdhgfkuasd') == None
