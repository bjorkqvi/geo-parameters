import geo_parameters as gp


def test_r():
    r = gp.atm.RelativeHumidity
    rel = gp.atm.RelativeHumidity('rel')

    assert r.name == 'r'
    assert rel.name == 'rel'

    assert r.standard_name() == 'relative_humidity'
    assert r.standard_name() == rel.standard_name()

    assert r.units() == '%'

def test_q():
    q = gp.atm.SpecificHumidity
    sp = gp.atm.SpecificHumidity('sp')

    assert q.name == 'q'
    assert sp.name == 'sp'

    assert q.standard_name() == 'specific_humidity'
    assert q.standard_name() == sp.standard_name()

    assert q.units() == '-'

def test_t():
    t = gp.atm.AirTemperature
    t2m = gp.atm.AirTemperature('t2m')

    assert t.name == 't'
    assert t2m.name == 't2m'

    assert t.standard_name() == 'air_temperature'
    assert t.standard_name() == t2m.standard_name()

    assert t.units() == 'K'

def test_mslp():
    mslp = gp.atm.MeanSeaLevelPressure
    pr = gp.atm.MeanSeaLevelPressure('pr')

    assert mslp.name == 'mslp'
    assert pr.name == 'pr'

    assert mslp.standard_name() == 'air_pressure_at_mean_sea_level'
    assert mslp.standard_name(alias=True) == 'air_pressure_at_sea_level'
    assert mslp.standard_name() == pr.standard_name()

    assert mslp.units() == 'N/m**2'
