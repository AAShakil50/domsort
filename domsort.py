#!/usr/bin/python3

import optparse

# parser = optparse.OptionParser("\n%prog [options] target_domain\n%prog -p target_domain")
#     parser.add_option("-s", "--subs", dest = "subs", default = os.path.join(base_path, "names.txt"),
#               type = "string", help = "(optional) A list of subdomains, accepts a single file, or a directory of files. default = 'names.txt'")
#     parser.add_option("-r", "--resolvers", dest = "resolvers", default = "resolvers.txt",
#               type = "string", help = "(optional) A list of DNS resolvers, if this list is empty it will OS's internal resolver default = 'resolvers.txt'")
#     parser.add_option("-t", "--targets_file", dest = "targets", default = "",
#               type = "string", help = "(optional) A file containing a newline delimited list of domains to brute force.")
#     parser.add_option("-p", "-P", action = 'store_true', dest = "print_data", default = False,
#               help = "(optional) Print data from found DNS records (default = off).")
#     parser.add_option("-o", "--output", dest = "output",  default = False, help = "(optional) Output to file (Greppable Format)")
#     parser.add_option("-j", "--json", dest="json", default = False, help="(optional) Output to file (JSON Format)")
#     parser.add_option("--type", dest = "type", default = False,
#               type = "string", help = "(optional) Print all reponses for an arbitrary DNS record type (CNAME, AAAA, TXT, SOA, MX...)")                  
#     parser.add_option("-c", "--process_count", dest = "process_count",
#               default = 8, type = "int",
#               help = "(optional) Number of lookup theads to run. default = 8")
#     parser.add_option("-v", "--verbose", action = 'store_true', dest = "verbose", default = False,
#               help = "(optional) Print debug information.")
#     (options, args) = parser.parse_args()

helpstr = """-------------------------------- DomSorter --------------------------------
----------------------------- by N1r0b 4h34n ------------------------------
-----------------github/aashakil50 || twitter/aashakil50--------------------

A tool that will sort all subdomains from different files and save it into a file
Note : subdomains must be separated by new lines.

"""

parser = optparse.OptionParser(usage=" prog [options]", version="1.0.0", description=helpstr)
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

# Set to str variable
ostr = ""
for sub in subdoms:
    ostr+=sub+"\n"

# Output to a file
ofile = options.f_output
open(ofile, "w").write(ostr)
