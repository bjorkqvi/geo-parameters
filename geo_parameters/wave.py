from .metaparameter import MetaParameter
import pint

ureg = pint.UnitRegistry()
ureg.default_format = "~C"


## Wave heights
class Hs(MetaParameter):
    name = "hs"
    _long_name = "significant_wave_height"
    _standard_name = [
        "sea_surface_wave_significant_height",
        "significant_height_of_wind_and_swell_waves",
    ]
    _unit = ureg.m


class HsSwell(MetaParameter):
    name = "hs_swell"
    _long_name = "significant_swell_height"
    _standard_name = [
        "sea_surface_swell_wave_significant_height",
        "significant_height_of_swell_waves",
    ]
    _unit = ureg.m


class HsSwell1(MetaParameter):
    name = "hs_swell1"
    _long_name = "significant_primary_swell_height"
    _standard_name = "sea_surface_primary_swell_wave_significant_height"
    _unit = ureg.m


class HsSwell2(MetaParameter):
    name = "hs_swell12"
    _long_name = "significant_secondary_swell_height"
    _standard_name = "sea_surface_secondary_swell_wave_significant_height"
    _unit = ureg.m


class HsSwell3(MetaParameter):
    name = "hs_swell13"
    _long_name = "significant_tertiary_swell_height"
    _standard_name = "sea_surface_tertiary_swell_wave_significant_height"
    _unit = ureg.m


class HsSea(MetaParameter):
    name = "hs_sea"
    _long_name = "significant_wind_sea_height"
    _standard_name = [
        "sea_surface_wind_wave_significant_height",
        "significant_height_of_wind_waves",
    ]
    _unit = ureg.m


class HsIG(MetaParameter):
    name = "hs_ig"
    _long_name = "significant_infragravity_wave_height"
    _standard_name = "sea_surface_infragravity_wave_significant_height"
    _unit = ureg.m


class HsMax(MetaParameter):
    name = "hs_max"
    _long_name = "maximum_wave_heigh"
    _standard_name = "sea_surface_wave_maximum_height"
    _unit = ureg.m


class EtaMax(MetaParameter):
    name = "eta_max"
    _long_name = "maximum_crest_heigh"
    _standard_name = "sea_surface_wave_maximum_crest_height"
    _unit = ureg.m


class Hs110(MetaParameter):
    name = "hs_110"
    _long_name = "highest_tenth_wave_heigh"
    _standard_name = "sea_surface_wave_mean_height_of_highest_tenth"
    _unit = ureg.m


## Wave periods
class Tp(MetaParameter):
    name = "tp"
    _long_name = "peak_wave_period"
    _standard_name = "sea_surface_wave_period_at_variance_spectral_density_maximum"
    _unit = ureg.s


class Tz(MetaParameter):
    name = "tz"
    _long_name = "zero_upcrossing_period"
    _standard_name = [
        "sea_surface_wave_mean_period",
        "sea_surface_wave_zero_upcrossing_period",
    ]
    _unit = ureg.s


class T13(MetaParameter):
    name = "t13"
    _long_name = "significant_wave_period"
    _standard_name = "sea_surface_wave_significant_period"
    _unit = ureg.s


class T110(MetaParameter):
    name = "t110"
    _long_name = "highest_tenth_wave_period"
    _standard_name = "sea_surface_wave_mean_period_of_highest_tenth"
    _unit = ureg.s


class Tm01(MetaParameter):
    name = "tm01"
    _long_name = "first_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = ureg.s


class Tm_10(MetaParameter):
    name = "tm_10"
    _long_name = "inverse_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = ureg.s


class Tm02(MetaParameter):
    name = "tm02"
    _long_name = "second_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = ureg.s


class TpSwell(MetaParameter):
    name = "tp_swell"
    _long_name = "peak_wave_period_of_swell"
    _standard_name = (
        "sea_surface_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class Tm01Swell(MetaParameter):
    name = "tm01_swell"
    _long_name = "first_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = ureg.s


class Tm_10Swell(MetaParameter):
    name = "tm_10_swell"
    _long_name = "inverse_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = ureg.s


class Tm02Swell(MetaParameter):
    name = "tm02_swell"
    _long_name = "second_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = ureg.s


class TpSwell1(MetaParameter):
    name = "tp_swell1"
    _long_name = "peak_wave_period_of_primary_swell"
    _standard_name = (
        "sea_surface_primary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class TpSwell2(MetaParameter):
    name = "tp_swell2"
    _long_name = "peak_wave_period_of_secondary_swell"
    _standard_name = (
        "sea_surface_secondary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class TpSwell3(MetaParameter):
    name = "tp_swell3"
    _long_name = "peak_wave_period_of_tertiary_swell"
    _standard_name = (
        "sea_surface_tertiary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class Tm01Sea(MetaParameter):
    name = "tm01_sea"
    _long_name = "first_moment_mean_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = ureg.s


class Tm_10Sea(MetaParameter):
    name = "tm_10_sea"
    _long_name = "inverse_moment_mean_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = ureg.s


class Tm02Sea(MetaParameter):
    name = "tm02_sea"
    _long_name = "second_moment_mean_wave_period_of_wind_swa"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = ureg.s


## Directions
class Dirm(MetaParameter):
    name = "dirm"
    _long_name = "mean_wave_direction"
    _standard_name = "sea_surface_wave_from_direction"
    _unit = ureg.deg


class Dirp(MetaParameter):
    name = "dirp"
    _long_name = "peak_wave_direction"
    _standard_name = (
        "sea_surface_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirmSwell(MetaParameter):
    name = "dirm_swell"
    _long_name = "mean_swell_direction"
    _standard_name = "sea_surface_swell_wave_from_direction"
    _unit = ureg.deg


class DirpSwell(MetaParameter):
    name = "dirp_swell"
    _long_name = "peak_swell_direction"
    _standard_name = (
        "sea_surface_swell_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirmSea(MetaParameter):
    name = "dirm_sea"
    _long_name = "mean_wind_sea_direction"
    _standard_name = "sea_surface_wind_wave_from_direction"
    _unit = ureg.deg


class DirpSea(MetaParameter):
    name = "dirp_sea"
    _long_name = "peak_wind_sea_direction"
    _standard_name = (
        "sea_surface_wind_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class Spr(MetaParameter):
    name = "spr"
    _long_name = "wave_directional_spread"
    _standard_name = "sea_surface_wave_directional_spread"
    _unit = ureg.deg


class SprP(MetaParameter):
    name = "sprp"
    _long_name = "peak_wave_directional_spread"
    _standard_name = (
        "sea_surface_wave_directional_spread_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class SprSwell(MetaParameter):
    name = "spr_swell"
    _long_name = "swell_directional_spread"
    _standard_name = "sea_surface_swell_wave_directional_spread"
    _unit = ureg.deg


class SprPSwell(MetaParameter):
    name = "sprp_swell"
    _long_name = "peak_swell_directional_spread"
    _standard_name = (
        "sea_surface_swell_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class SprSea(MetaParameter):
    name = "spr_sea"
    _long_name = "wind_sea_directional_spread"
    _standard_name = "sea_surface_wind_wave_directional_spread"
    _unit = ureg.deg


class SprPSea(MetaParameter):
    name = "sprp_sea"
    _long_name = "peak_wind_sea_directional_spread"
    _standard_name = (
        "sea_surface_wind_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


## Spectral
class Ef(MetaParameter):
    name = "ef"
    _long_name = "spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.s


class Efth(MetaParameter):
    name = "efth"
    _long_name = "directional_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.s / ureg.rad


class Freq(MetaParameter):
    name = "freq"
    _long_name = "frequency"
    _standard_name = ["wave_frequency", "sea_surface_wave_frequency"]
    _unit = ureg.s**-1


class DirFrom(MetaParameter):
    name = "dir"
    _long_name = "wave_direction"
    _standard_name = "sea_surface_wave_from_direction"
    _unit = ureg.deg


class DirTo(MetaParameter):
    name = "dir"
    _long_name = "wave_direction"
    _standard_name = "sea_surface_wave_to_direction"
    _unit = ureg.deg


## Moments (non-standard)
class M0(MetaParameter):
    name = "m0"
    _long_name = "zeroth_wave_moment"
    _standard_name = "sea_surface_zeroth_wave_moment"
    _unit = ureg.m**2
    _cf = False


class M1(MetaParameter):
    name = "m1"
    _long_name = "first_wave_moment"
    _standard_name = "sea_surface_first_wave_moment"
    _unit = ureg.m**2 / ureg.s
    _cf = False


class M_1(MetaParameter):
    name = "m_1"
    _long_name = "first_inverse_wave_moment"
    _standard_name = "sea_surface_first_inverse_wave_moment"
    _unit = ureg.m**2 * ureg.s
    _cf = False


class M2(MetaParameter):
    name = "m2"
    _long_name = "second_wave_moment"
    _standard_name = "sea_surface_second_wave_moment"
    _unit = ureg.m**2 / ureg.s**2
    _cf = False


class M3(MetaParameter):
    name = "m3"
    _long_name = "thirds_wave_moment"
    _standard_name = "sea_surface_thirds_wave_moment"
    _unit = ureg.m**2 / ureg.s**3
    _cf = False


class M4(MetaParameter):
    name = "m4"
    _long_name = "fourth_wave_moment"
    _standard_name = "sea_surface_fourth_wave_moment"
    _unit = ureg.m**2 / ureg.s**4
    _cf = False


class M5(MetaParameter):
    name = "m5"
    _long_name = "fifth_wave_moment"
    _standard_name = "sea_surface_fifth_wave_moment"
    _unit = ureg.m**2 / ureg.s**5
    _cf = False
