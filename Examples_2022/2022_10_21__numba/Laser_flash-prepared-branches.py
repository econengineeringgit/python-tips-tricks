
import numpy as np

from numba import jit
from numba import njit

import time

import gc



@njit   #A decorator for speeding uo the calculations
def _Solver_real_yesBranch(initial: np.ndarray, steps: int,
            sigma1: float, sigma2: float,
            c_bc: float, taumax: float, dt: float,
            c1: float, c2: float,
            contact_id: int):
    """
    Solver with realistic laser characteristics.

    Inputs:
        initial: a numpy array containing the initial state of the modell,
        steps: the numper of time steps to evaluate,
        sigma1: the sigma value of the first specimen,
        sigma2: the sigma value of the second specimen,
        c_bc: a constant used for boundary condition calculations,
        taumax: the time of maximum LASER power [s],
        dt: the time step size for the simultaon [s],
        c1: constant one used at the contact of the specimens,
        c2: constant two used at the contact of the specimens, 
        contact_id: the index of the cell, where the two specimen contact each other.

    Return:
        Tmat: the solution matrix.
    """
    
    #Setting up the solution matrix
    nodes = len(initial)
    Tmat = np.empty((steps, nodes))
    Tmat[0, :] = initial

    #e (Euler's number) used for calculations
    e = np.math.e

    for t in range(steps-1):
        for x in range(1, nodes-1):
            
            if x == contact_id:

                Tmat[t+1, x] = c1*Tmat[t, x-1] - (c1 + c2 - 1)*Tmat[t, x] + c2*Tmat[t, x+1]

            else:

                if x < contact_id:
                    sigma = sigma1

                else:
                    sigma = sigma2

                Tmat[t+1, x] = sigma*(Tmat[t, x-1] + Tmat[t, x+1]) + (1 - 2*sigma)*Tmat[t, x]



        #Setting boundary conditions
        Tmat[t+1, 0] = c_bc*((dt*(t+1))/taumax)*e**(1-(dt*(t+1))/taumax) + Tmat[t+1, 2]
        Tmat[t+1, nodes-1] = Tmat[t+1, nodes-3]

    return Tmat

    
@njit   #A decorator for speeding uo the calculations
def _Solver_real_noBranch(initial: np.ndarray, steps: int,
            sigma1: float, sigma2: float,
            c_bc: float, taumax: float, dt: float,
            c1: float, c2: float,
            contact_id: int):
    """
    Solver with realistic laser characteristics.

    Inputs:
        initial: a numpy array containing the initial state of the modell,
        steps: the numper of time steps to evaluate,
        sigma1: the sigma value of the first specimen,
        sigma2: the sigma value of the second specimen,
        c_bc: a constant used for boundary condition calculations,
        taumax: the time of maximum LASER power [s],
        dt: the time step size for the simultaon [s],
        c1: constant one used at the contact of the specimens,
        c2: constant two used at the contact of the specimens, 
        contact_id: the index of the cell, where the two specimen contact each other.

    Return:
        Tmat: the solution matrix.
    """
    
    #Setting up the solution matrix
    nodes = len(initial)
    Tmat = np.empty((steps, nodes))
    Tmat[0, :] = initial

    #e (Euler's number) used for calculations
    e = np.math.e

    for t in range(steps-1):
        for x in range(1, nodes-1):
            
            #Some fancy branchless programming for sigma
            sigma = sigma1*(x < contact_id) + sigma2*(x >= contact_id)
            
            #Branchless mode for calculating the T values
            Tmat[t+1, x] = (sigma*(Tmat[t, x-1] + Tmat[t, x+1]) + (1 - 2*sigma)*Tmat[t, x])*(x!=contact_id) + \
                            (c1*Tmat[t, x-1] - (c1 + c2 - 1)*Tmat[t, x] + c2*Tmat[t, x+1])*(x==contact_id)

        #Setting boundary conditions
        Tmat[t+1, 0] = c_bc*((dt*(t+1))/taumax)*e**(1-(dt*(t+1))/taumax) + Tmat[t+1, 2]
        Tmat[t+1, nodes-1] = Tmat[t+1, nodes-3]

    return Tmat



if __name__ == "__main__":

    tSteps = 10_000

    iniVec = np.empty((223))
    iniVec.fill(20.)


    func_data = {
        'initial'       :   iniVec,
        'steps'         :   tSteps,
        'sigma1'        :   0.1909448818897638,
        'sigma2'        :   0.25,
        'c_bc'          :   168.00335910325487,
        'taumax'        :   5e-5,
        'dt'            :   1.968503937007874e-07,
        'c1'            :   0.08248854719393173,
        'c2'            :   0.10526937474486915,
        'contact_id'    :   21,
    }

    start = time.perf_counter()


    if False:

        _Solver_real_yesBranch(
            initial=    func_data['initial'],
            steps=      func_data['steps'],
            sigma1=     func_data['sigma1'],
            sigma2=     func_data['sigma2'],
            c_bc=       func_data['c_bc'],
            taumax=     func_data['taumax'],
            dt=         func_data['dt'],
            c1=         func_data['c1'],
            c2=         func_data['c2'],
            contact_id= func_data['contact_id']
        )
        

    else:

        _Solver_real_noBranch(
            initial=    func_data['initial'],
            steps=      func_data['steps'],
            sigma1=     func_data['sigma1'],
            sigma2=     func_data['sigma2'],
            c_bc=       func_data['c_bc'],
            taumax=     func_data['taumax'],
            dt=         func_data['dt'],
            c1=         func_data['c1'],
            c2=         func_data['c2'],
            contact_id= func_data['contact_id']
        )


    end = time.perf_counter()


    print(end - start)

    #Clearing memory
    gc.collect()