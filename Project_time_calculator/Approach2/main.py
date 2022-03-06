# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 19:32:10 2022

@author: e^(j·2pi)
"""

# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(module='test_module', exit=False)