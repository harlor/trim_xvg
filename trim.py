#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(description="""
                        Trim down XVG files by taking every n-th row
                        """, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n', '--nth', dest='n', help="spacing between to lines to keep",
                        default=0, type=int)
    parser.add_argument('-i', '--input', dest='i', help="Input file", type=str)
    parser.add_argument('-o', '--output', dest='o', help="Output file", type=str)
    args = parser.parse_args()

    inputfile = open(args.i, "r")
    outputfile = open(args.o, "w")

    i = args.n
    for line in inputfile:
        if line[0] in ['#', '@']:
            outputfile.write(line)
        elif i == args.n:
            outputfile.write(line)
            i = 0
        else:
            i += 1

    inputfile.close()
    outputfile.close()


main()
