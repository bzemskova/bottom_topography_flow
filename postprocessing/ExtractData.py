# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:08:47 2021

@author: V.E. Zemskova

"""
#----------------------------------------------------------------------------
# This part converts Var1 that is of shape (Nx*Ny*Nz,lz,ly,lx)
# as resulting from exadata.py to Var2 that is of shape (Nx*lx,Ny*ly,Nz*lz)
#----------------------------------------------------------------------------
import numpy as np

def reshapeNek(Var1,lr1,Nx,Ny,Nz):

    Var2 = np.zeros(shape=(Nx*lr1[2],Ny*lr1[1],Nz*lr1[0]))
    for iz in range(Nz):
     for iy in range(Ny):    
        for ix in range(Nx):
            x2 = np.transpose(Var1[ix+iy*32+iz*32*32,:,:,:],(2,1,0))
            Var2[ix*lr1[2]:(ix+1)*lr1[2],iy*lr1[1]:(iy+1)*lr1[1],iz*lr1[0]:
                (iz+1)*lr1[0]] = x2
                
    return Var2


