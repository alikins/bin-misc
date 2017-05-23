#!/usr/bin/python

import codecs
import fileinput


def comma_to_comma_newline(line):
    comma_lines = line.split(',')
    return ',\n'.join(comma_lines)


def process(line):
    clean_line = comma_to_comma_newline(line)
    #clean_line2 = codecs.escape_decode(clean_line)
    #print clean_line2
    return clean_line


def main():
    for line in fileinput.input():
        clean_line = process(line)
        print clean_line


if __name__ == "__main__":
    main()
