import geo_parameters as gp
import pytest


def test_wrong_type():
    with pytest.raises(ValueError):
        gp.wave.Hs.my_family("ttt")
    with pytest.raises(ValueError):
        gp.wind.Wind.my_family("ttt")
    with pytest.raises(ValueError):
        gp.grid.Lon.my_family("ttt")
    with pytest.raises(ValueError):
        gp.ocean.Current.my_family("ttt")


def test_no_family():

    assert gp.wave.Hs.my_family() == {}
    assert gp.wave.SprPSea().my_family() == {}
    assert gp.wave.SprPSea().my_family("magnitude") is None


def test_wind_family():

    assert set(gp.wind.XWind().my_family().values()) == {
        gp.wind.XWind,
        gp.wind.YWind,
        gp.wind.Wind,
        gp.wind.WindDir,
        gp.wind.WindDirTo,
    }

    assert gp.wind.XWind().my_family().get("x") == gp.wind.XWind().my_family("x")

    assert set(gp.wind.XWind.my_family().values()) == {
        gp.wind.XWind,
        gp.wind.YWind,
        gp.wind.Wind,
        gp.wind.WindDir,
        gp.wind.WindDirTo,
    }
    assert (
        gp.wind.XWind.my_family().get("opposite_direction").is_same(gp.wind.WindDirTo)
    )


def test_stokes_family():
    assert set(gp.wave.XStokes().my_family().values()) == {
        gp.wave.XStokes,
        gp.wave.YStokes,
        gp.wave.Stokes,
        gp.wave.StokesDir,
        gp.wave.StokesDirFrom,
    }

    assert set(gp.wave.YStokes.my_family().values()) == {
        gp.wave.XStokes,
        gp.wave.YStokes,
        gp.wave.Stokes,
        gp.wave.StokesDir,
        gp.wave.StokesDirFrom,
    }

    assert (
        gp.wave.XStokes.my_family()
        .get("opposite_direction")
        .is_same(gp.wave.StokesDirFrom)
    )


def test_current_family():
    assert set(gp.ocean.XCurrent().my_family().values()) == {
        gp.ocean.XCurrent,
        gp.ocean.YCurrent,
        gp.ocean.Current,
        gp.ocean.CurrentDir,
        gp.ocean.CurrentDirFrom,
    }

    assert set(gp.ocean.YCurrent.my_family().values()) == {
        gp.ocean.XCurrent,
        gp.ocean.YCurrent,
        gp.ocean.Current,
        gp.ocean.CurrentDir,
        gp.ocean.CurrentDirFrom,
    }

    assert (
        gp.ocean.XCurrent.my_family()
        .get("opposite_direction")
        .is_same(gp.ocean.CurrentDirFrom)
    )


def test_periods():
    assert gp.wave.Tp.i_am() == "period"
    assert gp.wave.Tp.my_family().get("frequency").is_same(gp.wave.Fp)
    assert gp.wave.Tp.my_family().get("angular_frequency").is_same(gp.wave.Wp)
