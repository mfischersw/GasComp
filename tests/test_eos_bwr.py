# This file is part of GasComp.

"""
.. module:: test_eos_bwr
   :synopsis: This test module contains tests the thermodynamic BWR EOS
              calculation.

.. moduleauthor:: Michael Fischer
"""


from src.gascomp.eos_bwr.calc import Gas
from src.gascomp.eos_bwr.data import metaGenProp
from src.gascomp.eos_bwr.reference import gasmixture_Hgas


class TestEosBwr:

    def setup(self):
        self.gas = Gas(gasmixture_Hgas)

        self.genProp_Hgas = {"molmass": 19.043,
                             "normdensity": 0.854,
                             "criticalT": 208.965,
                             "criticalp": 4653.379,
                             "netcalorific":	885.171,
                             "grosscalorific": 978.226
                             }

        self.normProp_Hgas = {"ZN": 0.997,
                              "KN": 1.0,
                              "KTN": 0.011,
                              "KpN": -0.0034,
                              "rhoN": 0.852,
                              "cvN": 1548.066,
                              "cpN": 1991.426,
                              "kappaN": 1.282
                              }

        self.p_test = 50.0*1.0e5     # 50 bar
        self.T_test = 273.15 + 75.0  # 75 °C
        self.etap_test = 0.5

        self.testProp = {"Z": 0.934,
                         "K": 0.937,
                         "KT": 0.293,
                         "Kp": -0.0637,
                         "rho": 35.222,
                         "cv": 1751.858,
                         "cp": 2392.409,
                         "kappa": 1.284,
                         "n": 1.790,
                         }

    def test_genProp(self):
        genPropMix = self.gas.generalProps
        for prop in metaGenProp.keys():
            assert round(genPropMix[metaGenProp[prop]], 3) == \
                   round(self.genProp_Hgas[prop], 3)

    def test_normProp(self):
        assert round(self.gas.normProp_ZN, 3) == \
               round(self.normProp_Hgas["ZN"], 3)
        assert round(self.gas.normProp_KN, 3) == \
               round(self.normProp_Hgas["KN"], 3)
        assert round(self.gas.normProp_KTN, 3) == \
               round(self.normProp_Hgas["KTN"], 3)
        assert round(self.gas.normProp_KpN, 4) == \
               round(self.normProp_Hgas["KpN"], 4)
        assert round(self.gas.normProp_rhoN, 3) == \
               round(self.normProp_Hgas["rhoN"], 3)
        assert round(self.gas.normProp_cpN, 3) == \
               round(self.normProp_Hgas["cpN"], 3)
        assert round(self.gas.normProp_cvN, 3) == \
               round(self.normProp_Hgas["cvN"], 3)
        assert round(self.gas.normProp_kappaN, 3) == \
               round(self.normProp_Hgas["kappaN"], 3)

    def test_calc_realGasFactor_Z(self):
        Z = self.gas.calc_realGasFactor_Z(self.p_test, self.T_test)
        assert round(Z, 3) == round(self.testProp["Z"], 3)

    def test_calc_compressibility_K(self):
        K = self.gas.calc_compressibility_K(self.p_test, self.T_test)
        assert round(K, 3) == round(self.testProp["K"], 3)

    def test_calc_compressibility_KT(self):
        KT = self.gas.calc_compressibility_KT(self.p_test, self.T_test)
        assert round(KT, 3) == round(self.testProp["KT"], 3)

    def test_calc_compressibility_Kp(self):
        Kp = self.gas.calc_compressibility_Kp(self.p_test, self.T_test)
        assert round(Kp, 4) == round(self.testProp["Kp"], 4)

    def test_calc_rho(self):
        rho = self.gas.calc_rho(self.p_test, self.T_test)
        assert round(rho, 3) == round(self.testProp["rho"], 3)

    def test_calc_cv(self):
        cv = self.gas.calc_cv(self.p_test, self.T_test)
        assert round(cv, 3) == round(self.testProp["cv"], 3)

    def test_calc_cp(self):
        cp = self.gas.calc_cp(self.p_test, self.T_test)
        assert round(cp, 3) == round(self.testProp["cp"], 3)

    def test_calc_expPolytropic_n(self):
        n = self.gas.calc_expPolytropic_n(self.p_test, self.T_test,
                                          self.etap_test)
        assert round(n, 3) == round(self.testProp["n"], 3)

    def test_calc_expIsentropic_n(self):
        kappa = self.gas.calc_expIsentropic_n(self.p_test, self.T_test)
        assert round(kappa, 3) == round(self.testProp["kappa"], 3)

    def test_changeOfState_polytropic(self):

        T1_ref = 15.0
        p1_ref = 50.0

        T2_ref = 82.16
        p2_ref = 103.00
        etap_ref = 0.76
        yp_ref = 88.70

        T1 = T1_ref + 273.15
        p1 = p1_ref*1.0e5

        T2_x = T2_ref + 273.15
        p2_x = p2_ref*1.0e5
        etap_x = etap_ref
        yp_x = yp_ref*1.0e3

        T2_a, p2_a = self.gas.changeOfState_polytropic(T1, p1,
                                                       etap_x, yp_x,
                                                       "etapyp_to_T2p2")

        assert round(T2_a-273.15, 1) == round(T2_ref, 1)
        assert round(p2_a/1.0e5, 1) == round(p2_ref, 1)

        etap_b, yp_b = self.gas.changeOfState_polytropic(T1, p1,
                                                         T2_x, p2_x,
                                                         "T2p2_to_etapyp")

        assert round(etap_b, 1) == round(etap_ref, 1)
        assert round(yp_b/1.0e3, 1) == round(yp_ref, 1)

        T2_c, etap_c = self.gas.changeOfState_polytropic(T1, p1,
                                                         p2_x, yp_x,
                                                         "p2yp_to_T2etap")

        assert round(T2_c-273.15, 1) == round(T2_ref, 1)
        assert round(etap_c, 1) == round(etap_ref, 1)

        T2_d, yp_d = self.gas.changeOfState_polytropic(T1, p1,
                                                       p2_x, etap_x,
                                                       "p2etap_to_T2yp")

        assert round(T2_d-273.15, 1) == round(T2_ref, 1)
        assert round(yp_d/1.0e3, 1) == round(yp_ref, 1)

    def test_changeOfState_isentropic(self):

        T1_ref = 15.0
        p1_ref = 50.0

        T2_ref = 72.51
        p2_ref = 104.79
        yp_ref = 88.70

        T1 = T1_ref + 273.15
        p1 = p1_ref*1.0e5

        p2_x = p2_ref*1.0e5
        yp_x = yp_ref*1.0e3

        T2_a, p2_a = self.gas.changeOfState_isentropic(T1, p1,
                                                       yp_x,
                                                       "yp_to_T2p2")

        assert round(T2_a-273.15, 1) == round(T2_ref, 1)
        assert round(p2_a/1.0e5, 1) == round(p2_ref, 1)

        T2_b, yp_b = self.gas.changeOfState_isentropic(T1, p1,
                                                       p2_x,
                                                       "p2_to_T2yp")

        assert round(T2_b-273.15, 1) == round(T2_ref, 1)
        assert round(yp_b/1.0e3, 1) == round(yp_ref, 1)
