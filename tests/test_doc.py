import xarray as xr
import numpy as np
from geo_parameters.geo_parameters.wave import Hs, Tp
from geo_parameters.geo_parameters import get as gpget
from geo_parameters.geo_parameters import dict_of_parameters


def test_names():
    assert Hs.standard_name() == "sea_surface_wave_significant_height"
    assert Hs.short_name() == "hs"
    hsig = Hs()
    assert hsig.name() == "hs"

    hsig = Hs(name="hsig")
    assert hsig.name() == "hsig"

    assert hsig.standard_name() == "sea_surface_wave_significant_height"
    assert hsig.long_name() == "significant_wave_height"

    assert (
        hsig.standard_name(alias=True) == "significant_height_of_wind_and_swell_waves"
    )

    assert (
        Tp.standard_name(alias=True)
        == "sea_surface_wave_period_at_variance_spectral_density_maximum"
    )

    assert (
        Tp.standard_name()
        == "sea_surface_wave_period_at_variance_spectral_density_maximum"
    )


def test_get():
    assert gpget("sea_surface_wave_significant_height") == Hs
    # <class 'geo_parameters.geo_parameters.wave.Hs'>


def test_dicts():
    dict_of_parameters()
    dict_of_parameters(short=True)
    dict_of_parameters(alias=True)


def test_ds_find_me():
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
    breakpoint()
    assert Hs.find_me_in_ds(ds) == "interesting_hs_name"
    assert Tp.find_me_in_ds(ds) == "peak_period"
