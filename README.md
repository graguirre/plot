plot
====

plot SCF energy iterations from orca output file

examples
========

$ python2 orca-plot.py -i orca-output.out

$ ssh yourName@remoteOrcaServer 'cat path/to/orca/orca-output.out' | python2 orca-plot.py -i /dev/stdin
