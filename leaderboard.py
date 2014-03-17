#! /usr/bin/env python

h11e_best  = "000000000000f06dd167005dcfbaba43a087ba02e48a37136752485c433ea0fab2a6be59d160978d9e139f0c9229618f655689578591d1499df31e7289a630c3"
h11e_worst = "00000000000e68201e7bd4c56e4ba02b91055011c67f9b02e9758e4d7d1ba534f3b9c56c8f63c0e2213c1d61b3871df3f01c617eef01a71d7a7befb984b8f582"

hashrate = 62.3e6 # MHashes/sec

email = "sidney@jigsaw.nl"

import re, time, os

def present(solutions, malformed_lines):

    os.system("clear")

    print
    print "=== LEADERBOARD ==="
    print

    print "Number of solutions: %d" % len(solutions)

    print

    for (idx, hstring, hvalue) in solutions[:20]:

        frequency = 1.0 / (float(int(hvalue, 16)) / 2**512) / hashrate / 86400.0

        hvalue = hvalue[:20] + " ..."

        print "%5d \"%s\" %s    [1 / %6.3f days]" % (idx, hstring, hvalue, frequency)

    if malformed_lines != 0:
        print
        print "malformed lines (%d):" % len(malformed_lines)
        print
        for ml in malformed_lines:
            print "<%s>" % ml.rstrip("\r\n")

def main():

    filename = "SidneyCadot.txt"

    re_solution = re.compile("sha512\(\"(.*)\"\) = ([0-9a-f]{128})$")

    malformed_lines = []

    changed = False

    hstring_set = set()

    with open(filename) as f:

        solutions = []

        while True:

            line = f.readline()

            if line == "":

                if changed:

                    solutions.sort(key = lambda x : x[2])
                    changed = False
                    present(solutions, malformed_lines)

                time.sleep(0.5)

            else:

                assert line.endswith("\n")

                if not line.startswith("#"):

                    match = re_solution.match(line)

                    if match is None:

                        # the line we're trying to parse is malformed
                        malformed_lines.append(line)

                    else:

                        (hstring, hvalue) = (match.group(1), match.group(2))

                        # Verify that the hash string is new
                        if hstring not in hstring_set:

                            hstring_set.add(hstring)

                            solutions.append((len(solutions) + 1, hstring, hvalue))
                            changed = True

if __name__ == "__main__":
    main()
