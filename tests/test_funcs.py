import geo_parameters as gp


def test_get_wave():
    assert gp.shortget("hs") == gp.wave.Hs
    assert gp.get("significant_wave_height") is None
    assert gp.get("sea_surface_wave_significant_height") == gp.wave.Hs
    assert gp.get("significant_height_of_wind_and_swell_waves") == gp.wave.Hs


def test_get_wind():
    assert gp.shortget("x_wind") == gp.wind.XWind
    assert gp.get("xwind") is None
    assert gp.get("eastward_wind_component") is None
    assert gp.get("x_wind") == gp.wind.XWind
    assert gp.get("grid_eastward_wind") == gp.wind.XWind


def test_get_iteration_short_name():
    params = gp.dict_of_parameters(short=True)
    for key, value in params.items():
        assert gp.shortget(key) == value


def test_get_iteration_standard_name():
    params = gp.dict_of_parameters()
    for key, value in params.items():
        assert gp.get(key) == value


def test_get_iteration_alias():
    params = gp.dict_of_parameters(alias=True)
    for key, value in params.items():
        assert gp.get(key) == value
