import geo_parameters as gp
import numpy as np
def test_tp_compute_from():
    compute_dict = gp.wave.Tp.compute_from()
    np.testing.assert_almost_equal(compute_dict.get(gp.wave.Fp)(0.1), 10)
    
    np.testing.assert_almost_equal(compute_dict.get(gp.wave.Wp)(2*np.pi*0.1), 10)

def test_fp_compute_from():
    compute_dict = gp.wave.Fp.compute_from()
    np.testing.assert_almost_equal(compute_dict.get(gp.wave.Tp)(10), 0.1)
    
    np.testing.assert_almost_equal(compute_dict.get(gp.wave.Wp)(2*np.pi*0.1), 0.1)


def test_wp_compute_from():
    compute_dict = gp.wave.Wp.compute_from()
    np.testing.assert_almost_equal(compute_dict.get(gp.wave.Tp)(10), 2*np.pi*0.1)
    
    np.testing.assert_almost_equal(compute_dict.get(gp.wave.Fp)(0.1), 2*np.pi*0.1)
