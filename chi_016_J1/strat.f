c-----------------------------------------------------------------------
c  nek5000 user-file template
c
c  user specified routines:
c     - uservp  : variable properties
c     - userf   : local acceleration term for fluid
c     - userq   : local source term for scalars
c     - userbc  : boundary conditions
c     - useric  : initial conditions
c     - userchk : general purpose routine for checking errors etc.
c     - userqtl : thermal divergence for lowMach number flows 
c     - usrdat  : modify element vertices 
c     - usrdat2 : modify mesh coordinates
c     - usrdat3 : general purpose routine for initialization
c     
c-----------------------------------------------------------------------
      subroutine uservp(ix,iy,iz,eg) ! set variable properties

c      implicit none

      integer ix,iy,iz,eg
     
      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

      integer e
c     e = gllel(eg)

      udiff  = 0.0
      utrans = 0.0

      return
      end
c-----------------------------------------------------------------------
      subroutine userf(ix,iy,iz,eg) ! set acceleration term
c
c     Note: this is an acceleration term, NOT a force!
c     Thus, ffx will subsequently be multiplied by rho(x,t).
c
c      implicit none

      integer ix,iy,iz,eg

      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

      integer e
c     e = gllel(eg)
      
      Fr2 = 0.01
      U = 0.125
      f = -1.
      ffx = f*uy
      ffy = -f*ux + f*U 
      ffz = temp/Fr2

      return
      end
c-----------------------------------------------------------------------
      subroutine userq(ix,iy,iz,eg) ! set source term

c      implicit none

      integer ix,iy,iz,eg

      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

      integer e
c     e = gllel(eg)

c If no stratification restoration
      qvol   = 0.0

c If include stratification restoration
c      qvol = -(1.0/(6.0*pi))*(temp-z)

      return
      end
c-----------------------------------------------------------------------
      subroutine userbc(ix,iy,iz,iside,eg) ! set up boundary conditions
c
c     NOTE ::: This subroutine MAY NOT be called by every process
c
c      implicit none

      integer ix,iy,iz,iside,eg

      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

c      if (cbc(iside,gllel(eg),ifield).eq.'v01')

      ux   = 0.0
      uy   = 0.0
      uz   = 0.0
      temp = 0.0

      return
      end
c-----------------------------------------------------------------------
      subroutine useric(ix,iy,iz,eg) ! set up initial conditions

c      implicit none

      integer ix,iy,iz,eg

      include 'SIZE'
      include 'TOTAL'
      include 'NEKUSE'

      U = 0.125

      ux   = U
      uy   = 0.0
      uz   = 0.0
      temp = z

      return
      end
c-----------------------------------------------------------------------
      subroutine userchk()

c      implicit none

      include 'SIZE'
      include 'TOTAL'
      include 'RESTART'
      include 'ZPER'
      

      return
      end
c-----------------------------------------------------------------------
      subroutine userqtl ! Set thermal divergence

      call userqtl_scig 

      return
      end
c-----------------------------------------------------------------------
      subroutine usrdat()   ! This routine to modify element vertices

c      implicit none

      include 'SIZE'
      include 'TOTAL'

      return
      end
c-----------------------------------------------------------------------
      subroutine usrdat2()  ! This routine to modify mesh coordinates

c      implicit none

      include 'SIZE'
      include 'TOTAL'
      
      ntot = nx1*ny1*nz1*nelt


      J = 0.6
      chi = 0.16
      U = 0.125
      N = 10.
      f = 1.

      k = N*chi/U
      h = J*U/N
      
      
      do i=1,ntot
         xx = xm1(i,1,1,1)
         argx = k*xm1(i,1,1,1)/2.
         argsin = sin(argx)
         zm1(i,1,1,1) = zm1(i,1,1,1) + (1.0-zm1(i,1,1,1))*h*(argsin**2)
      enddo


      return
      end
c-----------------------------------------------------------------------
      subroutine usrdat3()

c      implicit none

      include 'SIZE'
      include 'TOTAL'

      return
      end

c automatically added by makenek
      subroutine usrsetvert(glo_num,nel,nx,ny,nz) ! to modify glo_num
      integer*8 glo_num(1)

      return
      end