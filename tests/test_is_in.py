import geo_parameters as gp


def test_docstring():
    assert gp.wave.Hs.is_in([gp.wave.Hs, gp.wave.Tp])
    assert not gp.wave.Hs.is_in([gp.wave.Dirp, gp.wave.Tp])
    assert not gp.wave.Hs.is_in([])
    assert not gp.wave.Hs.is_in(["hs"])
    assert gp.wave.Hs.is_in([gp.wave.Hs(), "hs"])
