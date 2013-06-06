PylonCCD
========

Code for simulating beam detection with a LN-cooled CCD camera

The major files included here are:
 - the Qfunction routines used to plot the results
 - exposure.py simulates a single exposure of the CCD array, takes the FFT, and finds the real and imaginary part of the relevent array element.
 - PiCloudExposureScript.py is a script file that runs 100 instances of exposure.py on the PiCloud (hosted cloud computing)

Most other files are old data, old versions of stuff, and other cruft. I will clean it up soon.

To use these, execute exposure.py many times and plot the data using one of the Qfunction routines.

A barebones example is:

```python
from exposure import exposure
from Qfunction import qfuncimage
from numpy import real,imag
from pylab import show

output = []
for i in range(10):
  output.append(exposure())
  
qfuncimage(real(output),imag(output))
show()
```
