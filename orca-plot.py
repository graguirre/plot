#
# Plot ORCA SCF iterations
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
    	print >> sys.stderr, "    -d                Dump mode, don't plot"
    	print >> sys.stderr, "    -i <input_file>   Input file"
    	print >> sys.stderr, "    -t <seconds>      Step time (default 0.1)"
    	print >> sys.stderr, "    -l <number>       Iterations to show (default 10)"
    	print >> sys.stderr, "Syntax: $ python2 plot-orca.py -i <input-file>"
    	sys.exit(1)

def plot(f,t,L,d):
	# initialize variables
	i = 0		# iteration accumulator
	E = []		# energy vector
	read_on = 0	# flag SCF iterations 
	
        if not d:
	    plt.ion()
	    plt.show()
	
	    fig = plt.figure()

	for line in f:
		# inicio iteraciones
		if line.find('ITERATIONS') > 0:  
			read_on = 1
		# final iteraciones
		elif line.find('SUCCESS') > 0:
			read_on = 0
		elif read_on == 1:
			lline = line.split()
			if len(lline)>0 and lline[0].isdigit() :
				E.append(float(lline[1]))
                                if d:
				    print i, lline[0], lline[1] # points to plot (It Energy(Eh))
                                else:
				    plt.axis([max([i-L,0]),i,min(E),max(E)])
				    plt.scatter(float(i),float(lline[1]))
				    plt.draw()
				    time.sleep(float(t))
				i += 1 # increment iteration


def main(argv):
	inputfile=''
        sleeptime=0.1
        showlast=10
        dumpmode=0
	
	try:
            opts, args = getopt.getopt(argv,"hdi:t:l:")
	except getopt.GetoptError:
	    usage()
	    sys.exit(1)

	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit(0)
		elif opt == '-i':
			inputfile = arg	
		elif opt == '-t':
			sleeptime = arg
		elif opt == '-l':
			showlast = int(arg)
		elif opt == '-d':
			dumpmode = 1

	if inputfile == '':
		usage()
		sys.exit(3)

	try:
		f = open(inputfile,'r')
    	except IOError:
        	print >> sys.stderr, "File "+ inputfile +" not found"
        	sys.exit(2)

	plot(f,sleeptime,showlast,dumpmode)


if __name__ == "__main__":
	main(sys.argv[1:])
