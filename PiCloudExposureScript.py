import exposure
#exposure.exposure()
import cloud
from pylab import show
from Qfunction import qfuncimage
from numpy import imag, real

N = 100 # number of times to run simulation
args = 1024
arglist = [1024]*N #each call uses the same argument in our case

jids = cloud.map(exposure.exposure, arglist)

all(item == 'done' for item in cloud.status(jids))

dataout = cloud.result(jids)

img = qfuncimage(real(dataout),imag(dataout),20)

show(img)

