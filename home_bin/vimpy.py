#!/usr/bin/python
#
# open the source file for a python module by module name
#
# Usage: vimpy MODULE_NAME
#
# for ex, httplib
# $ vimpy httplib
# will open /usr/lib64/python2.7/httplib.py
#
# Note: Doesn't understand c modules/.so's
import sys
import os

def main(args):

    module_names = args
    found_modules = []

    for module_name in module_names:
        try:
            mod = __import__(module_name)
        except ImportError:
            continue
        if hasattr(mod, '__file__'):
            found_modules.append(mod.__file__)

    exec_args = ['vim', '-o']
    for found_module in found_modules:
        if found_module.endswith('.pyc'):
            py_file = found_module[:-1]
            exec_args.append(py_file)

    os.execvp('vim', exec_args)

if __name__ == "__main__":
    ret = main(sys.argv[1:])
    sys.exit(ret)
