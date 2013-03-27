from __future__ import print_function

import sys
import time
from IPython.parallel import Client
import numpy as np
from exposure import exposure
import Qfunction as qf
from pylab import show
print("Connecting to client")
c = Client(profile="pylon")

# A LoadBalancedView is an interface to the engines that provides dynamic load
# balancing at the expense of not knowing which engine will execute the code.
print("Creating load-balanced view")
view = c.load_balanced_view()

# Submit tasks:
print("Submitting tasks...")

t1 = time.time()
async_results = []
for i in range(400):
	ar = view.apply_async(exposure)
	async_results.append(ar)


print("Submitted tasks: ", len(async_results))

# Block until all tasks are completed.

c.wait(async_results)
t2 = time.time()
t = t2-t1

print("Parallel calculation completed, time = %s s" % t)

# Get the results using the `get` method:

results = [ar.get() for ar in async_results]

# Plot the value of the European call in (volatility, strike) space.

qfuncoutput = qf.qfuncimage(np.real(results),np.imag(results),30)
show()
