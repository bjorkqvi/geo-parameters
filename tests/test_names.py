import geo_parameters as gp


def test_name_of_class():
    assert gp.wave.Hs.name == "hs"
    assert gp.wave.Hs.long_name() == "significant_wave_height"
    assert gp.wave.Hs.standard_name() == "sea_surface_wave_significant_height"
    assert (
        gp.wave.Hs.standard_name(alias=True)
        == "significant_height_of_wind_and_swell_waves"
    )
    assert gp.wave.Efth_max.name == "efth_max"
    assert (
        gp.wave.Efth_max.standard_name()
        == "sea_surface_wave_energy_at_variance_spectral_density_maximum"
    )
    assert gp.wave.Ef_max.name == "emax"
    assert (
        gp.wave.Ef_max.standard_name()
        == "sea_surface_wave_energy_at_variance_spectral_density_maximum"
    )


def test_units_of_class():
    assert str(gp.wave.Hs.units()) == "m"
    assert str(gp.wave.Efth_max.units()) == "m**2*s/rad"
    assert str(gp.wave.Ef_max.units()) == "m**2*s"


def test_name_of_instance():
    assert gp.wave.Hs().name == "hs"
    assert gp.wave.Hs(name="hs").name == "hs"
    assert gp.wave.Hs("hs").name == "hs"
    assert gp.wave.Hs().long_name() == "significant_wave_height"
    assert gp.wave.Hs().standard_name() == "sea_surface_wave_significant_height"
    assert (
        gp.wave.Hs().standard_name(alias=True)
        == "significant_height_of_wind_and_swell_waves"
    )


def test_units_of_instance():
    assert str(gp.wave.Hs().units()) == "m"
