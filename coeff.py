#定数
import const

def coeff_calc(D,L,M,v):
    CL = 2*L/(const.RHO*v*v*const.S)
    CD = 2*D/(const.RHO*v*v*const.S)
    Cm = 2*M/(const.RHO*v*v*const.S*const.MAC)

    print('\ncoeff:\nCD=%f\nCL=%f\nCm=%f' % (CD,CL,Cm))