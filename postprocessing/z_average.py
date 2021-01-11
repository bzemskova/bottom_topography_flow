# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:08:47 2021

@author: V.E. Zemskova
Sample code to open Nek5000 output file, read in velocity, grid, and buoyancy fields,
compute total kinetic energy dissipation at every grid point, and then horizontally
average in height-above-the-bottom vertical coordinates.
"""
#-----------------------------------------------------------------------------
# Find z-average of a field with topography
#-----------------------------------------------------------------------------

import numpy as np

def z_av(U,Zpos2,lr1,case,Nx,Ny,Nz):
    
    #Step 1: define regular grid in depth z for averaging
    z = np.linspace(0,1,Nz*lr1[0])
    Uav = np.zeros(shape=(Nz*lr1[0],))
    #Step 2: iterate over all z-intervals to find elements of Zpos2 that are within
    #these intervals. Then average over these corresponding elements for value of 
    #Var2 
    
    #uslice = U[:,20,:]
    if case==0:
        uslice=U
        zslice=Zpos2
    else:
        uslice = np.mean(U,axis=1)
        zslice = np.mean(Zpos2,axis=1)
        
    for ind in range(Nz*lr1[0]-1):
        res = np.where((zslice < z[ind+1]) & (zslice >= z[ind]))
        uu = uslice[res[0],res[1]]
        Uav[ind] = np.mean(uu)
    
    res = np.where((zslice < z[Nz-1]) & (zslice >= z[Nz-2]))
    uu = uslice[res[0],res[1]]
    Uav[Nz-1] = np.mean(uu)
    return Uav