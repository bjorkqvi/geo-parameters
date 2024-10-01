import geo_parameters as gp


def test_no_dir_type():
    assert gp.wave.Hs.dir_type() is None
    assert gp.ocean.SeaLevel.dir_type() is None
    param = gp.wave.Hs()
    param2 = gp.ocean.SeaLevel()

    assert param.dir_type() is None
    assert param2.dir_type() is None


def test_dir_type_from():
    assert gp.wave.Dirp.dir_type() == "from"
    assert gp.wave.StokesDirFrom.dir_type() == "from"
    assert gp.ocean.CurrentDirFrom.dir_type() == "from"
    assert gp.wind.WindDir.dir_type() == "from"

    param = gp.wave.Dirp()
    param2 = gp.wave.StokesDirFrom()
    param3 = gp.ocean.CurrentDirFrom()
    param4 = gp.wind.WindDir()

    assert param.dir_type() == "from"
    assert param2.dir_type() == "from"
    assert param3.dir_type() == "from"
    assert param4.dir_type() == "from"


def test_dir_type_to():
    assert gp.wave.DirpTo.dir_type() == "to"
    assert gp.wave.StokesDir.dir_type() == "to"
    assert gp.ocean.CurrentDir.dir_type() == "to"
    assert gp.wind.WindDirTo.dir_type() == "to"

    param = gp.wave.DirpTo()
    param2 = gp.wave.StokesDir()
    param3 = gp.ocean.CurrentDir()
    param4 = gp.wind.WindDirTo()

    assert param.dir_type() == "to"
    assert param2.dir_type() == "to"
    assert param3.dir_type() == "to"
    assert param4.dir_type() == "to"
