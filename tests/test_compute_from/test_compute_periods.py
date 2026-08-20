import geo_parameters as gp
import numpy as np
def test_tp_compute_from():
    func = gp.wave.Tp.compute_from(gp.wave.Fp)
    np.testing.assert_almost_equal(func(0.1), 10)

    func = gp.wave.Tp.compute_from(gp.wave.Wp)
    np.testing.assert_almost_equal(func(2*np.pi*0.1), 10)

def test_fp_compute_from():
    func = gp.wave.Fp.compute_from(gp.wave.Tp)
    np.testing.assert_almost_equal(func(10), 0.1)

    func = gp.wave.Fp.compute_from(gp.wave.Wp)
    np.testing.assert_almost_equal(func(2*np.pi*0.1), 0.1)


def test_wp_compute_from():
    func = gp.wave.Wp.compute_from(gp.wave.Tp)
    np.testing.assert_almost_equal(func(10), 2*np.pi*0.1)
    func = gp.wave.Wp.compute_from(gp.wave.Fp)
    np.testing.assert_almost_equal(func(0.1), 2*np.pi*0.1)


def test_Fp_swell_compute_from():
    func = gp.wave.FpSwell.compute_from(gp.wave.TpSwell)
    np.testing.assert_almost_equal(func(10), 0.1)
    func = gp.wave.FpSwell.compute_from(gp.wave.FpSwell)
    np.testing.assert_almost_equal(func(0.1), 0.1)