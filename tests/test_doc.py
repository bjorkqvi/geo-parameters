import geo_parameters as gp

# import xarray as xr
import numpy as np
import sys


def test_names():
    assert gp.wave.Hs.standard_name() == "sea_surface_wave_significant_height"
    assert gp.wave.Hs.name == "hs"
    hsig = gp.wave.Hs()
    assert hsig.name == "hs"

    hsig = gp.wave.Hs(name="hsig")
    assert hsig.name == "hsig"

    assert hsig.standard_name() == "sea_surface_wave_significant_height"
    assert hsig.long_name() == "significant_wave_height"

    assert (
        hsig.standard_name(alias=True) == "significant_height_of_wind_and_swell_waves"
    )

    assert (
        gp.wave.Tp.standard_name(alias=True)
        == "sea_surface_wave_period_at_variance_spectral_density_maximum"
    )

    assert (
        gp.wave.Tp.standard_name()
        == "sea_surface_wave_period_at_variance_spectral_density_maximum"
    )


def test_get():
    assert gp.get("sea_surface_wave_significant_height") == gp.wave.Hs
    assert gp.get("significant_height_of_wind_and_swell_waves") == gp.wave.Hs
    assert gp.get("hs") is None
    assert gp.shortget("hs") == gp.wave.Hs

    # <class 'geo_parameters.geo_parameters.wave.Hs'>


def test_dicts():
    gp.dict_of_parameters()
    gp.dict_of_parameters(short=True)
    gp.dict_of_parameters(alias=True)


def test_ds_find_me():
    if "xr" in sys.modules:
        ds = xr.Dataset(
            data_vars=dict(
                interesting_hs_name=(["lat", "lon"], np.zeros((11, 6))),
                peak_period=(["lat", "lon"], np.ones((11, 6))),
            ),
            coords=dict(
                lon=(["lon"], np.linspace(5, 10, 6)),
                lat=(["lat"], np.linspace(50, 60, 11)),
            ),
        )
        ds.interesting_hs_name.attrs = {
            "standard_name": "sea_surface_wave_significant_height"
        }

        ds.peak_period.attrs = {
            "standard_name": "sea_surface_wave_period_at_variance_spectral_density_maximum"
        }
        assert gp.wave.Hs.find_me_in_ds(ds) == "interesting_hs_name"
        assert gp.wave.Tp.find_me_in_ds(ds) == "peak_period"
