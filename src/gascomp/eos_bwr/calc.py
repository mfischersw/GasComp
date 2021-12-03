# This file is part of GasComp.

"""
.. module:: calc
   :synopsis: This module contains the thermodynamic BWR EOS calculation.

.. moduleauthor:: Michael Fischer
"""


# Python modules

# Own modules


class Gas():
    """Gas class

       This class contains several methods for the calculation of gas
       properties as well as state changes according to the BWR equation
       of state.
       It takes a gas mixture given as dictionary as input.
    """

    def __init__(self):#, gasmixture

        # Input
        pass
        #self.gasmixture = gasmixture
        #self.Nmix = len(gasmixture)

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
