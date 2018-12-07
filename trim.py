#!/usr/bin/env python

import argparse


def main():
    parser = argparse.ArgumentParser(description="""
                        Trim down XVG files by taking every n-th row
                        """, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-s', '--spacing', dest='s', help="spacing between to lines to keep",
                        default=0, type=int)
    parser.add_argument('-n', '--number', dest='n', help="Total number of lines",
                        default=0, type=int)
    parser.add_argument('-i', '--input', dest='i', help="Input file", type=str)
    parser.add_argument('-o', '--output', dest='o', help="Output file", type=str)
    args = parser.parse_args()

    inputfile = open(args.i, "r")
    outputfile = open(args.o, "w")

    # Spacing between lines
    s = args.s - 1

    # Total line count
    j = 1

    # Init Relative line count
    i = s
    for line in inputfile:

        # Check for total number of lines
        if j > args.n:
            break

        # Always write header
        if line[0] in ['#', '@']:
            outputfile.write(line)

        # Write line if i == s
        elif i == s:
            outputfile.write(line)
            j += 1
            i = 0
        else:
            i += 1

    inputfile.close()
    outputfile.close()


main()
