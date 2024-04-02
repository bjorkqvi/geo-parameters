from .metaparameter import MetaParameter
import pint

ureg = pint.UnitRegistry()

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


class DirmSwell(MetaParameter):
    _short_name = "dirm_swell"
    _long_name = "mean_swell_direction"
    _standard_name = "sea_surface_swell_wave_from_direction"
    _unit = ureg.deg


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
