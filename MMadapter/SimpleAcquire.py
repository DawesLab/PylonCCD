# Create a Micro-Manager core object:
import MMCorePy
mmc = MMCorePy.CMMCore()

#  Load and initialize the demo camera device:
mmc.loadDevice("cam","PrincetonInstruments","Camera-1")
mmc.initializeDevice("cam")

# Snap and retrieve an image:
mmc.snapImage()
im1 = mmc.getImage()

# Display the image:
from pylab import *
ion() # Activate interactive mode
figure()
imshow(im1,cmap = cm.gray)

