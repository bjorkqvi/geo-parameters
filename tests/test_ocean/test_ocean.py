import geo_parameters as gp


def  test_sst():
    sst = gp.ocean.SeaSurfaceTemperature
    sstemp = gp.ocean.SeaSurfaceTemperature('sstemp')

    assert sst.name == 'sst'
    assert sstemp.name == 'sstemp'

    assert sst.standard_name() == 'sea_surface_temperature'
    assert sst.standard_name() == sstemp.standard_name()

    assert sst.units() == 'K'

def  test_sss():
    sss = gp.ocean.SeaSurfaceSalinity
    sal = gp.ocean.SeaSurfaceSalinity('sal')

    assert sss.name == 'sss'
    assert sal.name == 'sal'

    assert sss.standard_name() == 'sea_surface_salinity'
    assert sss.standard_name() == sal.standard_name()

    assert sss.units() == 'g/kg'


def  test_ssd():
    ssd = gp.ocean.SeaSurfaceDensity
    rhow = gp.ocean.SeaSurfaceDensity('rhow')

    assert ssd.name == 'ssd'
    assert rhow.name == 'rhow'

    assert ssd.standard_name() == 'sea_surface_density'
    assert ssd.standard_name() == rhow.standard_name()

    assert ssd.units() == 'kg/m**3'