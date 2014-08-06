#
# Plot gaussian SCF iterations
#
# Gonzalo Aguirre <gaguirre@gmail.com>
# Version: 0.1
#

import time
import numpy as np
import matplotlib.pyplot as plt
import sys, getopt

def usage():
	print >> sys.stderr, "Options:"
    	print >> sys.stderr, "    -h                Show help"
    	print >> sys.stderr, "    -i <input_file>   Input file"
    	print >> sys.stderr, "Syntax: $ python2 plot-orca.py -i <input-file>"
    	sys.exit(1)

def plot(f):
	# initialize variables
	i = 0		# iteration accumulator
	E = []		# energy vector
	
	plt.ion()
	plt.show()
	
	fig = plt.figure()
	for line in f:
		if line.find("E=")>0 and line.find("Delta-E=")>0:
			lline = line.split()
			E.append(float(lline[1]))
			print i, lline[1] # points to plot (It Energy(Eh))
			plt.axis([max([i-10,0]),i,min(E),max(E)])
			plt.scatter(float(i),float(lline[1]))
			plt.draw()
			time.sleep(.1)
			i += 1 # increment iteration


def main(argv):
	inputfile=''
	
	try:
		opts, args = getopt.getopt(argv,"hi:")
	except getopt.GetoptError:
		usage()
		sys.exit(1)

	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit(0)
		elif opt == '-i':
			inputfile = arg
	
	if inputfile == '':
		usage()
		sys.exit(3)

	try:
		f = open(inputfile,'r')
    	except IOError:
        	print >> sys.stderr, "File "+ inputfile +" not found"
        	sys.exit(2)

	plot(f)


if __name__ == "__main__":
	main(sys.argv[1:])
