from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def qfunc3d(x,y,bins=4):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #x, y = np.random.rand(2, 100) * 4 # original x and y
    hist, xedges, yedges = np.histogram2d(x, y, bins)

    elements = (len(xedges) - 1) * (len(yedges) - 1)
    xpos, ypos = np.meshgrid(xedges[:-1]+0.25, yedges[:-1]+0.25)

    barsize = xedges[1] - xedges[0]

    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos = np.zeros(elements)
    dx = barsize * np.ones_like(zpos)
    dy = dx.copy()
    dz = hist.flatten()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

    return fig

def qfuncimage(array,bins=10,dolog=False):
    x = np.real(array)
    y = np.imag(array)

    H, xe, ye = np.histogram2d(x,y,bins)
    extent = [xe[0], xe[-1], ye[-1], ye[0]]
    #print extent
    fig = plt.figure()
    ax = plt.gca()
    ax.set_aspect('equal')
    if dolog:
        H = np.log(H+0.1)

    plt.imshow(H, extent=extent, interpolation='nearest', cmap='gray')
    plt.colorbar()
    return fig
