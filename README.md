description
===========

plot SCF energy iterations from orca output file

download
========

$ git clone https://github.com/graguirre/plot.git PlotOrca

$ cd PlotOrca

see examples

examples
========

$ python2 orca-plot.py -i orca-output.out

$ ssh yourName@remoteOrcaServer 'cat path/to/orca/orca-output.out' | python2 orca-plot.py -i /dev/stdin
