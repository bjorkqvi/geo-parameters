import geo_parameters as gp


def test_docstring():
    assert gp.wave.Hs.find_me_in([gp.wave.Hs, gp.wave.Tp]) == gp.wave.Hs
    assert gp.wave.Hs.find_me_in([gp.wave.Dirp, gp.wave.Tp]) is None
    assert gp.wave.Hs.find_me_in([]) is None
    assert gp.wave.Hs.find_me_in(["hs"]) is None
    hs = gp.wave.Hs("swh")
    assert gp.wave.Hs.find_me_in([hs, "hs"]) == hs
