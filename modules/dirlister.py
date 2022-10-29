
import os

def run(**args):
    files = os.listdir('.')
    print('[*] In dirlister module.')
    return str(files)