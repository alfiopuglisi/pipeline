
# Replace the sequence inside a generator object
#
# Inspired by https://pydev.blogspot.com/2014/02/changing-locals-of-frame-frameflocals.html

import ctypes

def replace_generator_sequence(gen, seq):

    # 1. load into dict
    gen.gi_frame.f_locals['.0'] = iter(seq)

    # 2. Store from dict into C structure
    ctypes.pythonapi.PyFrame_LocalsToFast(ctypes.py_object(gen.gi_frame), ctypes.c_int(0))

