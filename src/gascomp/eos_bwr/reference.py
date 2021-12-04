# This file is part of GasComp.

"""
.. module:: reference
   :synopsis: This module contains reference gasmixtures and properties
              from literature.

.. moduleauthor:: Michael Fischer
"""


# Gasmixtures
gasmixture_russian = {"methane": 98.156,
                      "ethane": 0.728,
                      "propane": 0.212,
                      "isobutane": 0.039,
                      "butane": 0.035,
                      "isopentane": 0.007,
                      "pentane": 0.006,
                      "hexane": 0.001,
                      "nitrogen": 0.786,
                      "carbon dioxide": 0.030}

normprop_russian = {"molmass": 16.3462,
                    "rho": 0.7311,
                    "K": 1.0,
                    "KT": 0.0082,
                    "Kp": -0.0025,
                    "cv": 1648.7930,
                    "cp": 2163.3224,
                    "kappa": 1.3088}

gasmixture_north = {"methane": 86.048,
                    "ethane": 8.861,
                    "propane": 1.907,
                    "isobutane": 0.144,
                    "butane": 0.216,
                    "isopentane": 0.023,
                    "pentane": 0.019,
                    "hexane": 0.007,
                    "nitrogen": 0.827,
                    "carbon dioxide": 1.949}

normprop_north = {"molmass": 18.6448,
                  "rho": 0.8345,
                  "K": 1.0,
                  "KT": 0.0105,
                  "Kp": -0.0032,
                  "cv": 1552.5456,
                  "cp": 2005.0503,
                  "kappa": 1.2873}

gasmixture_air = {"argon": 0.930,
                  "oxygen": 20.960,
                  "nitrogen": 78.070,
                  "carbon dioxide": 0.040}

normprop_air = {"molmass": 28.9661,
                "rho": 1.2938,
                "K": 1.0,
                "KT": 0.0043,
                "Kp": -0.0012,
                "cv": 785.4974,
                "cp": 1074.315,
                "kappa": 1.3660}

gasmixture_Lgas = {"methane": 82.0,
                   "ethane": 3.300,
                   "propane": 0.600,
                   "isobutane": 0.300,
                   "nitrogen": 12.600,
                   "carbon dioxide": 1.200}

normprop_Lgas = {"molmass": 18.6443,
                 "rho": 0.8338,
                 "K": 1.0,
                 "KT": 0.0083,
                 "Kp": -0.0024,
                 "cv": 1441.7762,
                 "cp": 1892.9533,
                 "kappa": 1.3097}

gasmixture_Hgas = {"methane": 85.400,
                   "ethane": 8.0,
                   "propane": 2.900,
                   "isobutane": 1.0,
                   "nitrogen": 0.700,
                   "carbon dioxide": 2.0}

normprop_Hgas = {"molmass": 19.0425,
                 "rho": 0.8524,
                 "K": 1.0,
                 "KT": 0.0110,
                 "Kp": -0.0034,
                 "cv": 1548.0658,
                 "cp": 1991.4259,
                 "kappa": 1.2821}

gasmixture_biogas = {"methane": 62.0,
                     "hydrogen": 0.5,
                     "oxygen": 0.5,
                     "nitrogen": 1.0,
                     "carbon dioxide": 36.0}

normprop_biogas = {"molmass": 26.2405,
                   "rho": 1.1749,
                   "K": 1.0,
                   "KT": 0.0122,
                   "Kp": -0.0036,
                   "cv": 1032.1642,
                   "cp": 1354.5107,
                   "kappa": 1.3076}
