import geo_parameters as gp


def test_docstring():
    assert gp.wave.Hs.find_me_in([gp.wave.Hs, gp.wave.Tp]) == [gp.wave.Hs]
    assert (
        gp.wave.Hs.find_me_in([gp.wave.Hs, gp.wave.Tp], return_first=True) == gp.wave.Hs
    )
    assert gp.wave.Hs.find_me_in([gp.wave.Dirp, gp.wave.Tp]) == []
    assert gp.wave.Hs.find_me_in([], return_first=True) is None
    assert gp.wave.Hs.find_me_in(["hs"]) == []
    hs = gp.wave.Hs("swh")
    assert gp.wave.Hs.find_me_in([hs, "hs"])[0] == hs
