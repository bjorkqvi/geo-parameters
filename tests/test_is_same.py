import geo_parameters as gp


def test_trivial():
    assert gp.wave.Hs.is_same(gp.wave.Hs)


def test_initialized():
    assert gp.wave.Hs.is_same(gp.wave.Hs())
    assert gp.wave.Hs().is_same(gp.wave.Hs)
    assert gp.wave.Hs().is_same(gp.wave.Hs())


def test_initialized_with_name():
    assert gp.wave.Hs.is_same(gp.wave.Hs("hsig"))
    assert gp.wave.Hs("hsig").is_same(gp.wave.Hs("hsig"))
    assert gp.wave.Hs("swh").is_same(gp.wave.Hs("hsig"))
    assert gp.wave.Hs("hsig").is_same(gp.wave.Hs)


def test_not_same():
    assert not gp.wave.Hs.is_same(gp.wind.XWind)
    assert not gp.wave.Hs.is_same(gp.wave.Tp)
    assert not gp.wave.Hs.is_same("hs")
