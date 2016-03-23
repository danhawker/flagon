from random import sample
from string import digits, ascii_uppercase, ascii_lowercase
from tempfile import gettempdir
from os import path

def rand_fname(suffix, length=8):
    chars = ascii_lowercase + ascii_uppercase + digits

    fname = path.join(gettempdir(), 'tmp-'
                + ''.join(sample(chars, length)) + suffix)

    return fname if not path.exists(fname) \
                else rand_fname(suffix, length)