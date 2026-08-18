from .wave import WaveParameter

class Fp(WaveParameter):
    name = "fp"
    _long_name = "peak_wave_frequency"
    _standard_name = "sea_surface_wave_frequency_at_variance_spectral_density_maximum"
    _unit = 'Hz'


class FpSea(WaveParameter):
    name = "fp_sea"
    _long_name = "peak_wave_frequency_of_wind_sea"
    _standard_name = (
        "sea_surface_wind_wave_frequency_at_variance_spectral_density_maximum"
    )
    _unit = 'Hz'
    _cf = False


class FpSwell(WaveParameter):
    name = "fp_swell"
    _long_name = "peak_wave_frequency_of_swell"
    _standard_name = (
        "sea_surface_swell_wave_frequency_at_variance_spectral_density_maximum"
    )
    _unit = 'Hz'
    _cf = False


class FpSwell1(WaveParameter):
    name = "fp_swell1"
    _long_name = "peak_wave_frequency_of_primary_swell"
    _standard_name = (
        "sea_surface_primary_swell_wave_frequency_at_variance_spectral_density_maximum"
    )
    _unit = 'Hz'
    _cf = False


class FpSwell2(WaveParameter):
    name = "fp_swell2"
    _long_name = "peak_wave_frequency_of_secondary_swell"
    _standard_name = "sea_surface_secondary_swell_wave_frequency_at_variance_spectral_density_maximum"
    _unit = 'Hz'
    _cf = False


class FpSwell3(WaveParameter):
    name = "fp_swell3"
    _long_name = "peak_wave_frequency_of_tertiary_swell"
    _standard_name = (
        "sea_surface_tertiary_swell_wave_frequency_at_variance_spectral_density_maximum"
    )
    _unit = 'Hz'
    _cf = False


class Fm(WaveParameter):
    name = "fm"
    _long_name = "mean_wave_frequency"
    _standard_name = "sea_surface_wave_mean_frequency"
    _unit = 'Hz'
    _cf = False


class FmSea(WaveParameter):
    name = "fm_sea"
    _long_name = "mean_wave_frequency_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_wave_frequency"
    _unit = 'Hz'
    _cf = False


class FmSwell(WaveParameter):
    name = "fm_swell"
    _long_name = "mean_wave_frequency_of_swell"
    _standard_name = "sea_surface_swell_wave_frequency"
    _unit = 'Hz'
    _cf = False


class FmSwell1(WaveParameter):
    name = "fm_swell1"
    _long_name = "mean_wave_frequency_of_primary_swell"
    _standard_name = "sea_surface_primary_swell_wave_frequency"
    _unit = 'Hz'
    _cf = False


class FmSwell2(WaveParameter):
    name = "fm_swell2"
    _long_name = "mean_wave_frequency_of_secondary_swell"
    _standard_name = "sea_surface_secondary_swell_wave_frequency"
    _unit = 'Hz'
    _cf = False


class FmSwell3(WaveParameter):
    name = "fm_swell3"
    _long_name = "mean_wave_frequency_of_tertiary_swell"
    _standard_name = "sea_surface_tertiary_swell_wave_frequency"
    _unit = 'Hz'
    _cf = False


class Wp(WaveParameter):
    name = "wp"
    _long_name = "peak_angular_wave_frequency"
    _standard_name = (
        "sea_surface_angular_wave_frequency_at_variance_spectral_density_maximum"
    )
    _unit = 'rad/s'
    _cf = False


class Wm(WaveParameter):
    name = "wm"
    _long_name = "mean_angular_wave_frequency"
    _standard_name = "sea_surface_angular_wave_mean_frequency"
    _unit = 'rad/s'
    _cf = False