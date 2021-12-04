# This file is part of GasComp.

"""
.. module:: calc
   :synopsis: This module contains the thermodynamic BWR EOS calculation.

.. moduleauthor:: Michael Fischer
"""


# Python modules
# import numpy
# from scipy import optimize

# Own modules
# from . import data

# Physical Constants
R_UNI = 0.08206     # Universal gas constant [atm*m^3/kmol*K]
TNORM = 273.15      # normal temperature [K]
PNORM = 101325.0    # normal pressure [Pa]

# Numerical Constants
NEWTON1D_TOL = 1.0e-10


class Gas():
    """Gas class

       This class contains several methods for the calculation of gas
       properties as well as state changes according to the BWR equation
       of state.
       It takes a gas mixture given as dictionary as input.
    """

    def __init__(self):

        # Input
        pass

    def calc_realGasFactor_Z(self, p, T):
        """Calculate Real gas factor Z.

        Parameters
        ----------
        p : float
            Pressure [Pa].
        T : float
            Temperature [K].

        Returns
        -------
        out : float
            Real gas factor Z.
        """

        p_atm = 2.0

        return p_atm
