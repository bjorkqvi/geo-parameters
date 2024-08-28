import geo_parameters as gp

import pytest


def test_decode():
    assert gp.decode("test") == ("test", None)
    assert gp.decode(gp.wave.Hs) == ("hs", gp.wave.Hs)
    ii = gp.wave.Hs()
    assert gp.decode(ii) == ("hs", ii)
    ii = gp.wave.Hs("hsig")
    assert gp.decode(ii) == ("hsig", ii)

    with pytest.raises(TypeError):
        gp.decode(1)


def test_decode_init():
    var, param = gp.decode(gp.wave.Hs)
    assert gp.is_gp_class(param)

    var, param = gp.decode(gp.wave.Hs, init=True)
    assert gp.is_gp_instance(param)
