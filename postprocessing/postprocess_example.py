# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:08:47 2021

@author: V.E. Zemskova
Sample code to open Nek5000 output file, read in velocity, grid, and buoyancy fields,
compute total kinetic energy dissipation at every grid point, and then horizontally
average in height-above-the-bottom vertical coordinates.
"""

import numpy as np
import neksuite
import exadata
import ExtractData
import z_average
import calc_dke

def HAB(Zpos, Xpos,J, chi, U, N):
    k = chi*N/U
    h = J*U/N
    height = h*((np.sin(k*Xpos/2.))**2.)
    hab = Zpos-height
    return hab

#define physical parameters of the simulation:
U = 0.125 #background velocity
N = 10. #stratification
chi = 0.16 #chi=Uk/N (k is topographic wavenumber)
J = 0.6 #J = hN/U (h is topographic height)


#Read in the data files
data2 = neksuite.readnek('strat0.f00001')
lr1 = data2.lr1
#simulation time
time = data2.time

#Extract x, y, z grid position
Xpos = ExtractData.reshapeNek(data2.elems.pos[0,:,:,:],lr1)
Ypos = ExtractData.reshapeNek(data2.elems.pos[1,:,:,:],lr1)
Zpos = ExtractData.reshapeNek(data2.elems.pos[2,:,:,:],lr1)

#Find height-above-bottom vertical coordinates (ex. chi=0.16, J=0.6)
hab = HAB(Zpos,Xpos,J, chi,U, N)

#Extract u,v,w velocities and buoyancy
u = ExtractData.reshapeNek(data2.elems.vel[0,:,:,:],lr1)
v = ExtractData.reshapeNek(data2.elems.vel[1,:,:,:],lr1)
w = ExtractData.reshapeNek(data2.elems.vel[2,:,:,:],lr1)
b = ExtractData.reshapeNek(data2.elems.temp[0,:,:,:],lr1)

#Calculate total kinetic energy dissipation over the entire volume
dke = calc_dke(u-U,v,w,Xpos,Ypos,Zpos,hab,lr1)

#Average kinetic energy dissipation horizontally in HAB coordinates
AvDKEhab = z_average.z_av(dke,hab,lr1,1)