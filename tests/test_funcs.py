from metaparameters.metaparameters import get, Hs, dict_of_parameters


def test_get():
    assert get("hs") == Hs
    assert get("significant_wave_height") is None
    assert get("sea_surface_wave_significant_height") == Hs
    assert get("significant_height_of_wind_and_swell_waves") == Hs


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
