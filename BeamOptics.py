from numpy import sqrt, arctan, pi, exp, random, shape
I = 1.0j
# A package for beam optics in python
def spot_size (z, z0, w0):
    """Calculate spot size at z, given z0, and w0"""
    return w0 * sqrt(1 + (z/z0)*(z/z0) )

def radius_curvature (z, z0):
    """calculate R(z)"""
    # This could be smarter, just adding epsilon to avoid nan's
    if (z == 0): 
        z += 1e-31
    return z * ( 1 + (z0/z)*(z0/z) )

def guoy_phase (z, z0):
    """really just atan(z/z0"""
    return arctan(z/z0)

def rayleigh_range (w0, wavelambda):
    """Calculate rayleigh range"""
    return pi*w0*w0/wavelambda;

def gaussian_beam (x, y, z, E0, z0, w0, k):
    """full gaussian beam at x, y, z given the beam parameters\n
    k is a tuple of [kx,ky,kz]"""
    r = sqrt(x*x + y*y)
    w = spot_size(z,z0,w0)
    R = radius_curvature(z,z0)
    eta = guoy_phase(z,z0)
    return E0 * w0/w * exp(- r*r/(w*w)) * exp(-I*k[2]*z - I*k[2]*r*r/(2*R) + I*eta)*exp(I*k[0]*x + I*k[1]*y) + sqrt(E0)*random.random([max(shape(x)),max(shape(y))]);
    # The exp(ikz) term in this definition causes extra phase accumulation
    # compared to the BPM. I need to sort this out for sure. The following agrees with BPM:
    # return w0/w * exp(- r*r/(w*w)) * exp(- 1j*k*r*r/(2*R) + 1j*eta)

def plane_wave_beam (x, y, z, E0, k):
    """a simple plane wave mostly used for testing"""
#   return E0*exp(I*k[2]*z)*exp(I*k[0]*x + I*k[1]*y) + sqrt(E0)*random.random([max(shape(x)),max(shape(y))])
    return (E0 + 0.05*sqrt(E0)*(random.random([max(shape(x)),max(shape(y))]) - 0.5)) * exp(I*k[0]*x + I*k[1]*y + I*k[2]*z)
#    return E0*exp(I*k[0]*x + I*k[1]*y + I*k[2]*z)


    
