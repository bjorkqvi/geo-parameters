from geo_parameters.geo_parameters import get, dict_of_parameters
from geo_parameters.geo_parameters.wave import Hs
from geo_parameters.geo_parameters.wind import XWind


def test_get_wave():
    assert get("hs") == Hs
    assert get("significant_wave_height") is None
    assert get("sea_surface_wave_significant_height") == Hs
    assert get("significant_height_of_wind_and_swell_waves") == Hs


def test_get_wind():
    assert get("x_wind") == XWind
    assert get("xwind") is None
    assert get("eastward_wind_component") is None
    assert get("x_wind") == XWind
    assert get("grid_eastward_wind") == XWind


def test_get_iteration_short_name():
    params = dict_of_parameters(short=True)
    for key, value in params.items():
        assert get(key) == value


def test_get_iteration_standard_name():
    params = dict_of_parameters()
    for key, value in params.items():
        assert get(key) == value


def test_get_iteration_alias():
    params = dict_of_parameters(alias=True)
    for key, value in params.items():
        assert get(key) == value
