from .wave import WaveParameter


class Tp(WaveParameter):
    name = "tp"
    _long_name = "peak_wave_period"
    _standard_name = "sea_surface_wave_period_at_variance_spectral_density_maximum"
    _unit = 's'


class Tz(WaveParameter):
    name = "tz"
    _long_name = "zero_upcrossing_period"
    _standard_name = [
        "sea_surface_wave_mean_period",
        "sea_surface_wave_zero_upcrossing_period",
    ]
    _unit = 's'


class T13(WaveParameter):
    name = "t13"
    _long_name = "significant_wave_period"
    _standard_name = "sea_surface_wave_significant_period"
    _unit = 's'


class T110(WaveParameter):
    name = "t110"
    _long_name = "highest_tenth_wave_period"
    _standard_name = "sea_surface_wave_mean_period_of_highest_tenth"
    _unit = 's'


class Tm01(WaveParameter):
    name = "tm01"
    _long_name = "first_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = 's'


class Tm_10(WaveParameter):
    name = "tm_10"
    _long_name = "inverse_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = 's'


class Tm02(WaveParameter):
    name = "tm02"
    _long_name = "second_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = 's'


class TpSwell(WaveParameter):
    name = "tp_swell"
    _long_name = "peak_wave_period_of_swell"
    _standard_name = (
        "sea_surface_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = 's'


class Tm01Swell(WaveParameter):
    name = "tm01_swell"
    _long_name = "first_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = 's'


class Tm_10Swell(WaveParameter):
    name = "tm_10_swell"
    _long_name = "inverse_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = 's'


class Tm02Swell(WaveParameter):
    name = "tm02_swell"
    _long_name = "second_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = 's'


class TpSwell1(WaveParameter):
    name = "tp_swell1"
    _long_name = "peak_wave_period_of_primary_swell"
    _standard_name = (
        "sea_surface_primary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = 's'


class TpSwell2(WaveParameter):
    name = "tp_swell2"
    _long_name = "peak_wave_period_of_secondary_swell"
    _standard_name = (
        "sea_surface_secondary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = 's'


class TpSwell3(WaveParameter):
    name = "tp_swell3"
    _long_name = "peak_wave_period_of_tertiary_swell"
    _standard_name = (
        "sea_surface_tertiary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = 's'


class TpSea(WaveParameter):
    name = "tp_sea"
    _long_name = "peak_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_period_at_variance_spectral_density_maximum"
    _unit = 's'


class Tm01Sea(WaveParameter):
    name = "tm01_sea"
    _long_name = "first_moment_mean_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = 's'


class Tm_10Sea(WaveParameter):
    name = "tm_10_sea"
    _long_name = "inverse_moment_mean_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = 's'


class Tm02Sea(WaveParameter):
    name = "tm02_sea"
    _long_name = "second_moment_mean_wave_period_of_wind_swa"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = 's'



## Wavenumbers and wavelengths
class Km(WaveParameter):
    name = "km"
    _long_name = "mean_wavenumber"
    _standard_name = "sea_surface_wave_mean_wavenumber_from_variance_spectral_density_first_wavenumber_moment"
    _unit = 'rad/m'


class Lm_10(WaveParameter):
    name = "lm_10"
    _long_name = "inverse_moment_mean_wavelength"
    _standard_name = "sea_surface_wave_mean_wavelength_from_variance_spectral_density_inverse_wavenumber_moment"
    _unit = 'rad/m'
