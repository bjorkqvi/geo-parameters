from .metaparameter import MetaParameter
import pint

ureg = pint.UnitRegistry()


## Wave heights
class Hs(MetaParameter):
    _short_name = "hs"
    _long_name = "significant_wave_height"
    _standard_name = [
        "sea_surface_wave_significant_height",
        "significant_height_of_wind_and_swell_waves",
    ]
    _unit = ureg.m


class HsSwell(MetaParameter):
    _short_name = "hs_swell"
    _long_name = "significant_swell_height"
    _standard_name = [
        "sea_surface_swell_wave_significant_height",
        "significant_height_of_swell_waves",
    ]
    _unit = ureg.m


class HsSwell1(MetaParameter):
    _short_name = "hs_swell1"
    _long_name = "significant_primary_swell_height"
    _standard_name = "sea_surface_primary_swell_wave_significant_height"
    _unit = ureg.m


class HsSwell2(MetaParameter):
    _short_name = "hs_swell12"
    _long_name = "significant_secondary_swell_height"
    _standard_name = "sea_surface_secondary_swell_wave_significant_height"
    _unit = ureg.m


class HsSwell3(MetaParameter):
    _short_name = "hs_swell13"
    _long_name = "significant_tertiary_swell_height"
    _standard_name = "sea_surface_tertiary_swell_wave_significant_height"
    _unit = ureg.m


class HsSea(MetaParameter):
    _short_name = "hs_sea"
    _long_name = "significant_wind_sea_height"
    _standard_name = [
        "sea_surface_wind_wave_significant_height",
        "significant_height_of_wind_waves",
    ]
    _unit = ureg.m


class HsIG(MetaParameter):
    _short_name = "hs_ig"
    _long_name = "significant_infragravity_wave_height"
    _standard_name = "sea_surface_infragravity_wave_significant_height"
    _unit = ureg.m


class HsMax(MetaParameter):
    _short_name = "hs_max"
    _long_name = "maximum_wave_heigh"
    _standard_name = "sea_surface_wave_maximum_height"
    _unit = ureg.m


class EtaMax(MetaParameter):
    _short_name = "eta_max"
    _long_name = "maximum_crest_heigh"
    _standard_name = "sea_surface_wave_maximum_crest_height"
    _unit = ureg.m


class Hs110(MetaParameter):
    _short_name = "hs_110"
    _long_name = "highest_tenth_wave_heigh"
    _standard_name = "sea_surface_wave_mean_height_of_highest_tenth"
    _unit = ureg.m


## Wave periods
class Tp(MetaParameter):
    _short_name = "tp"
    _long_name = "peak_wave_period"
    _standard_name = "sea_surface_wave_period_at_variance_spectral_density_maximum"
    _unit = ureg.s


class Tz(MetaParameter):
    _short_name = "tz"
    _long_name = "zero_upcrossing_period"
    _standard_name = [
        "sea_surface_wave_mean_period",
        "sea_surface_wave_zero_upcrossing_period",
    ]
    _unit = ureg.s


class T13(MetaParameter):
    _short_name = "t13"
    _long_name = "significant_wave_period"
    _standard_name = "sea_surface_wave_significant_period"
    _unit = ureg.s


class T110(MetaParameter):
    _short_name = "t110"
    _long_name = "highest_tenth_wave_period"
    _standard_name = "sea_surface_wave_mean_period_of_highest_tenth"
    _unit = ureg.s


class Tm01(MetaParameter):
    _short_name = "tm01"
    _long_name = "first_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = ureg.s


class Tm_10(MetaParameter):
    _short_name = "tm_10"
    _long_name = "inverse_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = ureg.s


class Tm02(MetaParameter):
    _short_name = "tm02"
    _long_name = "second_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = ureg.s


class TpSwell(MetaParameter):
    _short_name = "tp_swell"
    _long_name = "peak_wave_period_of_swell"
    _standard_name = (
        "sea_surface_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class Tm01Swell(MetaParameter):
    _short_name = "tm01_swell"
    _long_name = "first_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = ureg.s


class Tm_10Swell(MetaParameter):
    _short_name = "tm_10_swell"
    _long_name = "inverse_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = ureg.s


class Tm02Swell(MetaParameter):
    _short_name = "tm02_swell"
    _long_name = "second_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = ureg.s


class TpSwell1(MetaParameter):
    _short_name = "tp_swell1"
    _long_name = "peak_wave_period_of_primary_swell"
    _standard_name = (
        "sea_surface_primary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class TpSwell2(MetaParameter):
    _short_name = "tp_swell2"
    _long_name = "peak_wave_period_of_secondary_swell"
    _standard_name = (
        "sea_surface_secondary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class TpSwell3(MetaParameter):
    _short_name = "tp_swell3"
    _long_name = "peak_wave_period_of_tertiary_swell"
    _standard_name = (
        "sea_surface_tertiary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class Tm01Sea(MetaParameter):
    _short_name = "tm01_sea"
    _long_name = "first_moment_mean_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = ureg.s


class Tm_10Sea(MetaParameter):
    _short_name = "tm_10_sea"
    _long_name = "inverse_moment_mean_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = ureg.s


class Tm02Sea(MetaParameter):
    _short_name = "tm02_sea"
    _long_name = "second_moment_mean_wave_period_of_wind_swa"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = ureg.s


## Directions
class Dirm(MetaParameter):
    _short_name = "dirm"
    _long_name = "mean_wave_direction"
    _standard_name = "sea_surface_wave_from_direction"
    _unit = ureg.deg


class Dirp(MetaParameter):
    _short_name = "dirp"
    _long_name = "peak_wave_direction"
    _standard_name = (
        "sea_surface_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirmSwell(MetaParameter):
    _short_name = "dirm_swell"
    _long_name = "mean_swell_direction"
    _standard_name = "sea_surface_swell_wave_from_direction"
    _unit = ureg.deg


class DirpSwell(MetaParameter):
    _short_name = "dirp_swell"
    _long_name = "peak_swell_direction"
    _standard_name = (
        "sea_surface_swell_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirmSea(MetaParameter):
    _short_name = "dirm_sea"
    _long_name = "mean_wind_sea_direction"
    _standard_name = "sea_surface_wind_wave_from_direction"
    _unit = ureg.deg


class DirpSea(MetaParameter):
    _short_name = "dirp_sea"
    _long_name = "peak_wind_sea_direction"
    _standard_name = (
        "sea_surface_wind_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class Spr(MetaParameter):
    _short_name = "spr"
    _long_name = "wave_directional_spread"
    _standard_name = "sea_surface_wave_directional_spread"
    _unit = ureg.deg


class SprP(MetaParameter):
    _short_name = "sprp"
    _long_name = "peak_wave_directional_spread"
    _standard_name = (
        "sea_surface_wave_directional_spread_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class SprSwell(MetaParameter):
    _short_name = "spr_swell"
    _long_name = "swell_directional_spread"
    _standard_name = "sea_surface_swell_wave_directional_spread"
    _unit = ureg.deg


class SprPSwell(MetaParameter):
    _short_name = "sprp_swell"
    _long_name = "peak_swell_directional_spread"
    _standard_name = (
        "sea_surface_swell_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class SprSea(MetaParameter):
    _short_name = "spr_sea"
    _long_name = "wind_sea_directional_spread"
    _standard_name = "sea_surface_wind_wave_directional_spread"
    _unit = ureg.deg


class SprPSea(MetaParameter):
    _short_name = "sprp_sea"
    _long_name = "peak_wind_sea_directional_spread"
    _standard_name = (
        "sea_surface_wind_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


## Spectral
class Ef(MetaParameter):
    _short_name = "ef"
    _long_name = "spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.s


class Efth(MetaParameter):
    _short_name = "efth"
    _long_name = "directional_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.s / ureg.rad


## Moments (non-standard)
class M0(MetaParameter):
    _short_name = "m0"
    _long_name = "zeroth_wave_moment"
    _standard_name = "sea_surface_zeroth_wave_moment"
    _unit = ureg.m**2
    _cf = False


class M1(MetaParameter):
    _short_name = "m1"
    _long_name = "first_wave_moment"
    _standard_name = "sea_surface_first_wave_moment"
    _unit = ureg.m**2 / ureg.s
    _cf = False


class M_1(MetaParameter):
    _short_name = "m_1"
    _long_name = "first_inverse_wave_moment"
    _standard_name = "sea_surface_first_inverse_wave_moment"
    _unit = ureg.m**2 * ureg.s
    _cf = False


class M2(MetaParameter):
    _short_name = "m2"
    _long_name = "second_wave_moment"
    _standard_name = "sea_surface_second_wave_moment"
    _unit = ureg.m**2 / ureg.s**2
    _cf = False


class M3(MetaParameter):
    _short_name = "m3"
    _long_name = "thirds_wave_moment"
    _standard_name = "sea_surface_thirds_wave_moment"
    _unit = ureg.m**2 / ureg.s**3
    _cf = False


class M4(MetaParameter):
    _short_name = "m4"
    _long_name = "fourth_wave_moment"
    _standard_name = "sea_surface_fourth_wave_moment"
    _unit = ureg.m**2 / ureg.s**4
    _cf = False


class M5(MetaParameter):
    _short_name = "m5"
    _long_name = "fifth_wave_moment"
    _standard_name = "sea_surface_fifth_wave_moment"
    _unit = ureg.m**2 / ureg.s**5
    _cf = False
