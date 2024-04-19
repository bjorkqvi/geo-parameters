import geo_parameters as gp


def test_is_gpi():
    assert gp.is_gp_instance(gp.wave.Hs())
    assert gp.is_gp_instance(gp.wave.Hs("test"))
    assert not gp.is_gp_instance(gp.wave.Hs)
    assert not gp.is_gp_instance("test")


def test_is_gpc():
    assert not gp.is_gp_class(gp.wave.Hs())
    assert not gp.is_gp_class(gp.wave.Hs("test"))
    assert gp.is_gp_class(gp.wave.Hs)
    assert not gp.is_gp_class("test")


def test_is_gp():
    assert gp.is_gp(gp.wave.Hs())
    assert gp.is_gp(gp.wave.Hs("test"))
    assert gp.is_gp(gp.wave.Hs)
    assert not gp.is_gp("test")
