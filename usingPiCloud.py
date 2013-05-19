# IPython log file

import exposure
exposure()
exposure.exposure()
import cloud
jid = cloud.call(exposure)
jid = cloud.call(exposure.exposure)
print jid
cloud.status()
cloud.status(jid)
cloud.result(jid)
exposure.exposure()
exposure.exposure(1024)
exposure.exposure(512)
exposure.exposure(1024)
args = 1024
N = 100
zip([args]*N)
jids = cloud.map(exposure.exposure, *zip(*([args]*N)))
zip(args*N)
zip([args]*N)
jids = cloud.map(exposure.exposure, zip(([args]*N)))
jids.status()
jids
cloud.status(jids)
cloud.result(jids)
jids = cloud.map(exposure.exposure, *zip(([args]*N)))
cloud.status(jids)
cloud.result(jids)
jids = cloud.map(exposure.exposure, *zip(*([args]*N)))
jids = cloud.map(exposure.exposure, [1024,1024,1024])
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.result(jids)
ones()
numpy.ones(10)
from numpy import ones
ones(10)
zip(1*10)
zip([1]*N)
zip(*[1]*N)
zip(*[1,]*N)
zip([1,]*N)
zip([1]*N)
zip((1)*N)
zip((1024)*N)
zip([1024]*N)
arglist = zip([1024],10)
arglist = zip([1024],N)
zip([1024],N)
arglist = zip([1024]*N)
arglist
jids = cloud.map(exposure.exposure, arglist)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.result(jids)
arglist = [1024,1024,1024,1024]
jids = cloud.map(exposure.exposure, arglist)
cloud.status(jids)
cloud.result(jids)
[1024]*10
arglist = [1024]*100
jids = cloud.map(exposure.exposure, arglist)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids)
cloud.status(jids) = 'done'
cloud.status(jids) == 'done'
all(item == 'done' for item in cloud.status(jids))
cloud.status(jids) == 'done'
cloud.status(jids)
cloud.result(jids)
get_ipython().magic(u'logstart')
dataout = cloud.result(jids)
dataout
get_ipython().system(u'ls -F ')
from Qfunction import qfunc3d
qfunc3d
qfunc3d()
qfunc3d.__doc__
get_ipython().system(u'less Qfunction')
get_ipython().system(u'less qfunc3d')
dataout
dataout[1]
real(dataout)
from numpy import real
real(dataout)
from Qfunction import qfuncimage
from numpy import imag
img = qfuncimage(real(dataout),imag(dataout),20)
show(img)
from pylab import show
show(img)
exit()
