import geo_parameters as gp
import numpy as np
import pytest

FROM_DIRS = [gp.wind.WindDir, gp.wind.FrictionVelocityDir,
             gp.wave.Dirm, gp.wave.Dirp,
           gp.wave.DirmSwell, gp.wave.DirmSwell1, gp.wave.DirmSwell2, gp.wave.DirmSwell3, gp.wave.DirmSea, 
           gp.wave.DirpSwell, gp.wave.DirpSwell1, gp.wave.DirpSwell2, gp.wave.DirpSwell3, gp.wave.DirpSea, 
           gp.wave.StokesDirFrom, 
           gp.ocean.CurrentDirFrom]

TO_DIRS = [gp.wind.WindDirTo,  gp.wind.FrictionVelocityDirTo,
           gp.wave.DirmTo, gp.wave.DirpTo, 
           gp.wave.DirmSwellTo, gp.wave.DirmSwell1To, gp.wave.DirmSwell2To, gp.wave.DirmSwell3To, gp.wave.DirmSeaTo, 
           gp.wave.DirpSwellTo, gp.wave.DirpSwell1To, gp.wave.DirpSwell2To, gp.wave.DirpSwell3To, gp.wave.DirpSeaTo, 
           gp.wave.StokesDir,
           gp.ocean.CurrentDir]


wind_from = np.array([0,90,180,270])
wind_to = np.array([180,270,0,90])


def test_compute_dir_from():
    for param, to_param in zip(FROM_DIRS, TO_DIRS):
        func = param.compute_from(param)
        np.testing.assert_almost_equal(func(wind_to), wind_to)
        
        func = param.compute_from(to_param)
        np.testing.assert_almost_equal(func(wind_to), wind_from)
        func = param.compute_from(to_param)
        np.testing.assert_almost_equal(func(wind_from), wind_to)


def test_raises_error():
    assert gp.wind.WindDir.compute_from(gp.wind.Wind) is None

    assert gp.wind.Wind.compute_from(gp.wind.WindDir) is None