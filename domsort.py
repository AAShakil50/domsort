#!/usr/bin/python3

import optparse

helpstr = """-------------------------------- DomSorter --------------------------------
----------------------------- by N1r0b 4h34n ------------------------------
-----------------github/aashakil50 || twitter/aashakil50--------------------

A tool that will sort all subdomains from different files and save it into a file
Note : subdomains must be separated by new lines.

"""

parser = optparse.OptionParser(usage=" prog [options]", version="1.1", description=helpstr)
parser.add_option("-i", "--input", dest="f_input", type="string", help="Input files of subdomains. Comma(,) separated.")
parser.add_option("-o", "--output", dest="f_output", type="string", help="Out file where to keep all sorted subdomains")
(options, args) = parser.parse_args()

if(options.f_input == None or options.f_output == None):
    parser.error("Input files and Output file is required")

# Combine all subdomains(files) in one variable
ifiles = options.f_input.split(",")
combstr = ""
for ifile in ifiles:
    ifl = open(ifile, "r")
    combstr+=ifl.read()

# Separate by new line in a set and keep in set by triming spaces
subdomst = combstr.splitlines()
subdoms = set()
for doms in subdomst:
    subdoms.add(doms.strip())

# Sort subdomains
subdoms = sorted(subdoms)

# Set to str variable
ostr = ""
for sub in subdoms:
    ostr+=sub+"\n"

# Output to a file
ofile = options.f_output
open(ofile, "w").write(ostr)
