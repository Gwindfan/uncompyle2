# extendedPrint.py -- source test pattern for extended print statements
#
# This simple program is part of the decompyle test suite.
#
# decompyle is a Python byte-code decompiler
# See http://www.crazy-compilers.com/decompyle/ for
# for further information

import sys

print >> sys.stdout, "Hello World"
print >> sys.stdout, 1,2,3
print >> sys.stdout, 1,2,3,
print >> sys.stdout
