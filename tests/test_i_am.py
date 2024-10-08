import geo_parameters as gp


def test_no_role():
    assert gp.wave.Hs.i_am() is None
    assert gp.wave.Tp().i_am() is None


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
    assert gp.wind.Wind.i_am() == "mag"
    assert gp.wind.Gust().i_am() == "mag"
    assert gp.wave.Stokes().i_am() == "mag"
    assert gp.ocean.Current().i_am() == "mag"


def test_is_dir():
    assert gp.wind.WindDir.i_am() == "dir"
    assert gp.wind.GustDir().i_am() == "dir"
    assert gp.wave.StokesDir().i_am() == "dir"
    assert gp.ocean.CurrentDir().i_am() == "dir"


def test_get_components_of_self():
    param = gp.wind.XWind
    assert param.my_family().get("x") == param
    assert param.my_family().get("y") == gp.wind.YWind
    assert param.my_family().get("mag") == gp.wind.Wind
    assert param.my_family().get("dir") == gp.wind.WindDir
