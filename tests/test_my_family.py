import geo_parameters as gp


def test_no_family():

    assert gp.wave.Hs.my_family() is None
    assert gp.wave.Tp().my_family() is None


def test_wind_family():
    assert set(gp.wind.XWind().my_family().values()) == {
        gp.wind.XWind,
        gp.wind.YWind,
        gp.wind.Wind,
        gp.wind.WindDir,
    }

    assert set(gp.wind.XWind.my_family().values()) == {
        gp.wind.XWind,
        gp.wind.YWind,
        gp.wind.Wind,
        gp.wind.WindDir,
    }
