#!/usr/bin/python

import codecs
import fileinput


def process(line):
    clean_line, _ = codecs.escape_decode(line)
    clean_line2 = codecs.escape_decode(clean_line)
    # return(clean_line2)
    #print(clean_line2)
    return(clean_line.decode('utf-8'))


def main():
    for line in fileinput.input():
        clean_line = process(line)
        print(clean_line)


if __name__ == "__main__":
    main()
