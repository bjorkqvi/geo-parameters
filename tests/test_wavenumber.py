import geo_parameters as gp


def test_wavenumber():
    km = gp.wave.Km()
    assert km.name == "km"
    assert (
        km.standard_name()
        == "sea_surface_wave_mean_wavenumber_from_variance_spectral_density_first_wavenumber_moment"
    )
    km = gp.wave.Km("mean_k")
    assert km.name == "mean_k"
    assert (
        km.standard_name()
        == "sea_surface_wave_mean_wavenumber_from_variance_spectral_density_first_wavenumber_moment"
    )


def test_wavelength():
    lm = gp.wave.Lm_10()
    assert lm.name == "lm_10"
    assert (
        lm.standard_name()
        == "sea_surface_wave_mean_wavelength_from_variance_spectral_density_inverse_wavenumber_moment"
    )
    lm = gp.wave.Lm_10("mean_l")
    assert lm.name == "mean_l"
    assert (
        lm.standard_name()
        == "sea_surface_wave_mean_wavelength_from_variance_spectral_density_inverse_wavenumber_moment"
    )
