import numpy as np


def pad(data):
    bad_indexes = np.isnan(data)
    good_indexes = np.logical_not(bad_indexes)
    good_data = data[good_indexes]
    interpolated = np.interp(bad_indexes.nonzero()[0], good_indexes.nonzero()[0], good_data)
    data[bad_indexes] = interpolated
    return data

def get_gradient(var,Xpos,Ypos,Zpos,Nx,Ny,Nz):
    ux = np.zeros((Nx,Ny,Nz))
    uy = np.zeros((Nx,Ny,Nz))
    uz = np.zeros((Nx,Ny,Nz))
    for j in range(Nz):
        ux[:,:,j] = np.gradient(var[:,:,j],Xpos[:,10,j],axis=0)
    for j in range(Ny):
        uy[:,:,j] = np.gradient(var[:,:,j],Ypos[10,:,j],axis=1)    
    for j in range(Nx):
        uz[j,:,:] = np.gradient(var[j,:,:],Zpos[j,10,:],axis=1)    
    return ux, uy,uz

def calc_dke(U,V,W,Xpos,Ypos,Zpos,hab,lr1):
     
    [Ux,Uy,Uz] = get_gradient(U,Xpos,Ypos,Zpos)
    [Vx,Vy,Vz] = get_gradient(V,Xpos,Ypos,Zpos)
    [Wx,Wy,Wz] = get_gradient(W,Xpos,Ypos,Zpos)
     
    Ux = np.apply_along_axis(pad, 0, Ux)
    Uy = np.apply_along_axis(pad, 1, Uy)
    Uz = np.apply_along_axis(pad, 2, Uz)
    dke = Ux**2 + Uy**2 + Uz**2
    del Ux,Uy,Uz
     
    Vx = np.apply_along_axis(pad, 0, Vx)
    Vy = np.apply_along_axis(pad, 1, Vy)
    Vz = np.apply_along_axis(pad, 2, Vz)
    dke = dke+Vx**2 + Vy**2 + Vz**2
    del Vx,Vy,Vz
     
    Wx = np.apply_along_axis(pad, 0, Wx)
    Wy = np.apply_along_axis(pad, 1, Wy)
    Wz = np.apply_along_axis(pad, 2, Wz)
    dke = dke+Wx**2 + Wy**2 + Wz**2
    del Wx,Wy,Wz
     
    return dke
     
     
     
     
     
     
     
     
     
     
     
     
     