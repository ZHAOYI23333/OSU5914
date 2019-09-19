'''
NOTE: Run this from the top-level directory
'''

import os
from os.path import join

import sys
sys.path.insert(0, join(os.getcwd(), 'tweet_api_src'))

from get_interests_dict_from_disco import get_interests_from_discovery