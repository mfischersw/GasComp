from src.gascomp.eos_bwr.calc import Gas


class TestEosBwr:

    def setup(self):
        self.gas = Gas()

    def test_calc_realGasFactor_Z(self):
        assert 2.0 == self.gas.calc_realGasFactor_Z(0.0, 0.0)
