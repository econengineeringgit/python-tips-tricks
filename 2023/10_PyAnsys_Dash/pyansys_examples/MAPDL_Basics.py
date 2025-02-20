import pandas as pd
from ansys.mapdl.core import launch_mapdl

from pyAnsys_MAPDL_dash import make_sbc

mapdl = launch_mapdl(override=True, license_type="ansys", cleanup_on_exit=True)
mapdl.clear()
mapdl.prep7()
mapdl.units("BIN")
mapdl.csys(kcn=0)

# PV NSM (lb/in^2)
nsm = .002

# Faceseet material
tfs = 0.03
mid = 1
Ex = 10.0e6
nu_xy = 0.3
dens = 0.1 / 386.089
mapdl.mp('EX', mid, Ex)
mapdl.mp('PRXY', mid, nu_xy)
mapdl.mp('DENS', mid, dens)

# Core material
tc = 0.25
mid = 2
Ez = 75e3
Gxz = 45e3
Gyz = 22e3
dens = (3.1 / 12**3) / 386.089

mapdl.mp('EX', mid, 10)
mapdl.mp('EY', mid, 10)
mapdl.mp('EZ', mid, Ez)
mapdl.mp('GXY', mid, 10.)
mapdl.mp('GXZ', mid, Gxz)
mapdl.mp('GYZ', mid, Gyz)
mapdl.mp('PRXY', mid, 0.)
mapdl.mp('PRXZ', mid, 0.)
mapdl.mp('PRYZ', mid, 0.)
mapdl.mp('DENS', mid, dens)

# create shell property
mapdl.et(1, 181, kop1=0, kop3=2)
mapdl.sectype(secid=1, type_="SHELL")
mapdl.secdata(tfs, 1, 0, 3)
mapdl.secdata(tc, 2, 0, 3)
mapdl.secdata(tfs, 1, 0, 3)
mapdl.secoffset('MID')
mapdl.seccontrol(val4=nsm)

# create joint property
mid = 10
K_1 = 1e6
K_2 = 1e6
K_3 = 1e6
K_4 = 1e3
K_5 = 1e5
K_6 = 1e5
mapdl.et(mid,250,0)
mapdl.r(mid)
mapdl.rmore(K_1, K_2, K_3, K_4, K_5, K_6)

# create geometry (areas)
w = 20.
h = 20.
xc = 0.
yc = 0.
dx = 2.0

a1 = mapdl.blc4(xcorner=xc, ycorner=yc, width=w, height=h)
mapdl.agen(itime=2, na1='ALL', dx=w+dx)

# mesh
mapdl.allsel()
mid=1
mapdl.aatt(mat=mid, type_=mid, secn=mid)
mapdl.aesize('all', dx/2.)
mapdl.mshape(0, '2D')
mapdl.mopt('SPLIT', 'OFF')
mapdl.smrtsize(sizlvl=4)
mapdl.csys(kcn=0)
mapdl.amesh("all")

# base remote points
mapdl.lsel(type_='s', item='LOC', comp='X', vmin=0.)
mapdl.nsll(type_='s', nkey=1)
n_base_1, r_base = make_sbc(mapdl, 0., h/4., 0., pinb=dx)
mapdl.lsel(type_='s', item='LOC', comp='X', vmin=0.)
mapdl.nsll(type_='s', nkey=1)
n_base_2, r_base = make_sbc(mapdl, 0., 3*h/4., 0., pinb=dx)

# ref remote points
mapdl.lsel(type_='s', item='LOC', comp='X', vmin=w)
mapdl.nsll(type_='s', nkey=1)
nr1, rr1 = make_sbc(mapdl, w+dx/2., h/4., 0., pinb=dx)
mapdl.lsel(type_='s', item='LOC', comp='X', vmin=w)
mapdl.nsll(type_='s', nkey=1)
nr2, rr2 = make_sbc(mapdl, w+dx/2., 3*h/4., 0., pinb=dx)

# mob remote points
mapdl.lsel(type_='s', item='LOC', comp='X', vmin=w+dx)
mapdl.nsll(type_='s', nkey=1)
nm1, rm1 = make_sbc(mapdl, w+dx/2., h/4., 0., pinb=dx)
mapdl.lsel(type_='s', item='LOC', comp='X', vmin=w+dx)
mapdl.nsll(type_='s', nkey=1)
nm2, rm2 = make_sbc(mapdl, w+dx/2., 3*h/4., 0., pinb=dx)

# Add joints
mapdl.allsel()
mid = 10
mapdl.mat(mid)
mapdl.type(mid)
mapdl.real(mid)
mapdl.e(nr1,nm1)
mapdl.e(nr2,nm2)

# solving
mapdl.allsel()
mapdl.slashsolu()
mapdl.outres(item='ALL', freq='ALL')
mapdl.d(n_base_1, "ALL")
mapdl.d(n_base_2, "ALL")
mapdl.antype('MODAL')
mapdl.modopt('LANB', 10)
mapdl.mxpand(elcalc="YES")
o = mapdl.solve()

print(o)