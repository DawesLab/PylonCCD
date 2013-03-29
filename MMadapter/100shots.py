from pylab import * 
ion() 
import MMCorePy 
mmc = MMCorePy.CMMCore() 
mmc.loadDevice("cam","DemoCamera","DCam") 
mmc.initializeDevice("cam") 
print "Test acquire and display of monochrome images." 
figure() 
mmc.setCameraDevice("cam") 
mmc.snapImage() 
im1 = mmc.getImage() 
imshow(im1,cmap = cm.gray) 
width=mmc.getImageWidth() 
height=mmc.getImageHeight() 
BufferSize=width*height*2*100/1048576 
mmc.setCircularBufferMemoryFootprint(BufferSize) 
mmc.startSequenceAcquisition(100,100,False) 
while(mmc.isSequenceRunning()): 
    pass 
for i in range(100): 
    img = mmc.popNextImage() 
    imshow(im1,cmap = cm.gray) 