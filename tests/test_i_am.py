import geo_parameters as gp


def test_no_role():
    assert gp.wave.Hs.i_am() is None
    assert gp.wave.SprPSwell.i_am() is None


def test_period():
    assert gp.wave.Tp().i_am() == "period"
    assert gp.wave.Fp().i_am() == "frequency"
    assert gp.wave.Wp().i_am() == "angular_frequency"


def test_is_x():
    assert gp.wind.XWind.i_am() == "x"
    assert gp.wind.XGust().i_am() == "x"
    assert gp.wave.XStokes().i_am() == "x"
    assert gp.ocean.XCurrent().i_am() == "x"


def test_is_y():
    assert gp.wind.YWind.i_am() == "y"
    assert gp.wind.YGust().i_am() == "y"
    assert gp.wave.YStokes().i_am() == "y"
    assert gp.ocean.YCurrent().i_am() == "y"


def test_is_mag():
    assert gp.wind.Wind.i_am() == "magnitude"
    assert gp.wind.Gust().i_am() == "magnitude"
    assert gp.wave.Stokes().i_am() == "magnitude"
    assert gp.ocean.Current().i_am() == "magnitude"


def test_is_dir():
    assert gp.wind.WindDir.i_am() == "direction"
    assert gp.wind.GustDir().i_am() == "direction"
    assert gp.wave.StokesDir().i_am() == "direction"
    assert gp.ocean.CurrentDir().i_am() == "direction"


def test_get_components_of_self():
    param = gp.wind.XWind
    assert param.my_family().get("x") == param
    assert param.my_family().get("y") == gp.wind.YWind
    assert param.my_family().get("magnitude") == gp.wind.Wind
    assert param.my_family().get("direction") == gp.wind.WindDir
