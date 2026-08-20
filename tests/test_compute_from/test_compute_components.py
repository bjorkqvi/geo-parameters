import geo_parameters as gp
import numpy as np
import pytest

COMPONENTS = [(gp.wind.EastWind, gp.wind.NorthWind), 
              (gp.wind.EastFrictionVelocity, gp.wind.NorthFrictionVelocity), 
              (gp.wind.YWind, gp.wind.XWind)]
MAG_DIRS = [(gp.wind.Wind,  gp.wind.WindDir)]


u = np.array([2,2,0,-3,-1,4,0,5])
v = np.array([0,2,3,3,0,4,-1,-5])
wind_to = np.array([90,45,0,315,270,225,180,135])
wind_from = np.array([270,225,180,135,90,45,0,315])
mag = np.sqrt(u**2+v**2)
        


def test_compute_mag_from_components():
    for uv, magdir in zip(COMPONENTS, MAG_DIRS):
        func = magdir[0].compute_from(uv[0], uv[1])
        
        np.testing.assert_almost_equal(func(u,v), mag)


        func = magdir[0].compute_from(uv[1], uv[0])
        
        np.testing.assert_almost_equal(func(v,u), mag)



def test_no_func():
    assert gp.wind.WindDir.compute_from(gp.wind.Wind) is None

    assert gp.wind.Wind.compute_from(gp.wind.WindDir) is None