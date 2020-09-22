#!/usr/bin/env python

from collections import defaultdict
import fileinput
import re

FUNCNAME = r'''@@.*@@\sdef\s(.*)\(.*\)|@@.*@@\sclass\s(.*)\(.*\)'''
funcname_re = re.compile(FUNCNAME)

FILENAME_PATTERN = r'''^\+\+\+\s(.*)'''
filename_re = re.compile(FILENAME_PATTERN)


def process(line, filename):
    filename_match = filename_re.match(line)

    if filename_match:
        filename = filename_match.group(1)

    res = funcname_re.match(line)
    method_name = ''

    if res:
        method_name = res.group(0)

    if method_name:
        return filename, method_name

    return filename, None


def main():
    filename = 'N/A'
    file_methods_map = defaultdict(list)
    for line in fileinput.input():
        filename, method_name = process(line, filename)
        # if method_name:
        # print('%s: %s' % (filename, method_name or ''))
        # file_methods_map[(filename, method_name)] = None
        file_methods_map[filename].append(method_name)
        #if method_name is None or filename not in file_methods_map:
        #    file_methods_map[filename].append(method_name)

    import pprint
    pprint.pprint(file_methods_map)

    for filename in sorted(file_methods_map):
        methods = [x for x in file_methods_map[filename] if x is not None] or [None]
        for meth in methods:
            print('%s: %s' % (filename, meth or ''))


if __name__ == "__main__":
    main()
