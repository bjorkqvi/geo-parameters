from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg


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
    name = "hs_swell2"
    _long_name = "significant_secondary_swell_height"
    _standard_name = "sea_surface_secondary_swell_wave_significant_height"
    _unit = ureg.m


class HsSwell3(MetaParameter):
    name = "hs_swell3"
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


## Wave frequencies
class Fp(MetaParameter):
    name = "fp"
    _long_name = "peak_wave_frequency"
    _standard_name = "sea_surface_wave_frequency_at_variance_spectral_density_maximum"
    _unit = ureg.s**-1


class Fm(MetaParameter):
    name = "fm"
    _long_name = "mean_wave_frequency"
    _standard_name = "sea_surface_wave_mean_frequency"
    _unit = ureg.s**-1
    _cf = False


class Wp(MetaParameter):
    name = "Wp"
    _long_name = "peak_angular_wave_frequency"
    _standard_name = (
        "sea_surface_angular_wave_frequency_at_variance_spectral_density_maximum"
    )
    _unit = ureg.rad * ureg.s**-1
    _cf = False


class Wm(MetaParameter):
    name = "Wm"
    _long_name = "mean_angular_wave_frequency"
    _standard_name = "sea_surface_angular_wave_mean_frequency"
    _unit = ureg.rad * ureg.s**-1
    _cf = False


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


class DirmTo(MetaParameter):
    name = "dirm"
    _long_name = "mean_wave_direction"
    _standard_name = "sea_surface_wave_to_direction"
    _unit = ureg.deg


class Dirp(MetaParameter):
    name = "dirp"
    _long_name = "peak_wave_direction"
    _standard_name = (
        "sea_surface_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirpTo(MetaParameter):
    name = "dirp"
    _long_name = "peak_wave_direction"
    _standard_name = (
        "sea_surface_wave_to_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg
    _cf = False


class DirmSwell(MetaParameter):
    name = "dirm_swell"
    _long_name = "mean_swell_direction"
    _standard_name = "sea_surface_swell_wave_from_direction"
    _unit = ureg.deg


class DirmSwellTo(MetaParameter):
    name = "dirm_swell"
    _long_name = "mean_swell_direction"
    _standard_name = [
        "sea_surface_swell_wave_to_direction",
        "direction_of_swell_wave_velocity",
    ]
    _unit = ureg.deg


class DirpSwell(MetaParameter):
    name = "dirp_swell"
    _long_name = "peak_swell_direction"
    _standard_name = (
        "sea_surface_swell_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirpSwellTo(MetaParameter):
    name = "dirp_swell"
    _long_name = "peak_swell_direction"
    _standard_name = (
        "sea_surface_swell_wave_to_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg
    _cf = False


class DirmSwell1(MetaParameter):
    name = "dirm_swell1"
    _long_name = "mean_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_from_direction"
    _unit = ureg.deg


class DirmSwell1To(MetaParameter):
    name = "dirm_swell1"
    _long_name = "mean_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_to_direction"

    _unit = ureg.deg
    _cf = False


class DirpSwell1(MetaParameter):
    name = "dirp_swell1"
    _long_name = "peak_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg


class DirpSwell1To(MetaParameter):
    name = "dirp_swell1"
    _long_name = "peak_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_to_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class DirmSwell2(MetaParameter):
    name = "dirm_swell2"
    _long_name = "mean_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_from_direction"
    _unit = ureg.deg


class DirmSwell2To(MetaParameter):
    name = "dirm_swell2"
    _long_name = "mean_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_to_direction"

    _unit = ureg.deg
    _cf = False


class DirpSwell2(MetaParameter):
    name = "dirp_swell2"
    _long_name = "peak_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg


class DirpSwell2To(MetaParameter):
    name = "dirp_swell2"
    _long_name = "peak_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_to_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class DirmSwell3(MetaParameter):
    name = "dirm_swell3"
    _long_name = "mean_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_from_direction"
    _unit = ureg.deg


class DirmSwell3To(MetaParameter):
    name = "dirm_swell3"
    _long_name = "mean_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_to_direction"

    _unit = ureg.deg
    _cf = False


class DirpSwell3(MetaParameter):
    name = "dirp_swell3"
    _long_name = "peak_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg


class DirpSwell3To(MetaParameter):
    name = "dirp_swell3"
    _long_name = "peak_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_to_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class DirmSea(MetaParameter):
    name = "dirm_sea"
    _long_name = "mean_wind_sea_direction"
    _standard_name = "sea_surface_wind_wave_from_direction"
    _unit = ureg.deg


class DirmSeaTo(MetaParameter):
    name = "dirm_sea"
    _long_name = "mean_wind_sea_direction"
    _standard_name = [
        "sea_surface_wind_wave_to_direction",
        "direction_of_wind_wave_velocity",
    ]
    _unit = ureg.deg


class DirpSea(MetaParameter):
    name = "dirp_sea"
    _long_name = "peak_wind_sea_direction"
    _standard_name = (
        "sea_surface_wind_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirpSeaTo(MetaParameter):
    name = "dirp_sea"
    _long_name = "peak_wind_sea_direction"
    _standard_name = (
        "sea_surface_wind_wave_to_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg
    _cf = False


## Spreading
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
    _cf = False


class SprSwell1(MetaParameter):
    name = "spr_swell1"
    _long_name = "primary_swell_directional_spread"
    _standard_name = "sea_surface_primary_swell_wave_directional_spread"
    _unit = ureg.deg


class SprPSwell1(MetaParameter):
    name = "sprp_swell1"
    _long_name = "peak_primary_swell_directional_spread"
    _standard_name = "sea_surface_primary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class SprSwell2(MetaParameter):
    name = "spr_swell2"
    _long_name = "secondary_swell_directional_spread"
    _standard_name = "sea_surface_scondary_swell_wave_directional_spread"
    _unit = ureg.deg


class SprPSwell2(MetaParameter):
    name = "sprp_swell2"
    _long_name = "peak_secondary_swell_directional_spread"
    _standard_name = "sea_surface_secondary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class SprSwell3(MetaParameter):
    name = "spr_swell3"
    _long_name = "tertiary_swell_directional_spread"
    _standard_name = "sea_surface_tertiary_swell_wave_directional_spread"
    _unit = ureg.deg


class SprPSwell3(MetaParameter):
    name = "sprp_swell3"
    _long_name = "peak_tertiary_swell_directional_spread"
    _standard_name = "sea_surface_tertiary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


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
    _cf = False


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


class Fk(MetaParameter):
    name = "fk"
    _long_name = "wavenumer_spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.m


class Fkth(MetaParameter):
    name = "fkth"
    _long_name = "directional_wavenumber_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.m / ureg.rad


class Qv(MetaParameter):
    name = "qv"
    _long_name = "inverse_phase_speed_spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.m * ureg.s


class Qvth(MetaParameter):
    name = "qvth"
    _long_name = "directional_inverse_phase_speed_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.m * ureg.s / ureg.rad


class Freq(MetaParameter):
    name = "freq"
    _long_name = "frequency"
    _standard_name = ["wave_frequency", "sea_surface_wave_frequency"]
    _unit = ureg.s**-1


class DirsFrom(MetaParameter):
    name = "dirs"
    _long_name = "wave_direction"
    _standard_name = "sea_surface_wave_from_direction"
    _unit = ureg.deg


class DirsTo(MetaParameter):
    name = "dirs"
    _long_name = "wave_direction"
    _standard_name = "sea_surface_wave_to_direction"
    _unit = ureg.deg


##Stokes
class EastStokes(MetaParameter):
    name = "usx"
    _long_name = "stokes_east_component"
    _standard_name = "sea_surface_wave_stokes_drift_eastward_velocity"
    _unit = ureg.m / ureg.s


class NorthStokes(MetaParameter):
    name = "usy"
    _long_name = "stokes_north_component"
    _standard_name = "sea_surface_wave_stokes_drift_northward_velocity"
    _unit = ureg.m / ureg.s


class XStokes(MetaParameter):
    name = "usx"
    _long_name = "stokes_x_component"
    _standard_name = "sea_surface_wave_stokes_drift_x_velocity"
    _unit = ureg.m / ureg.s


class YStokes(MetaParameter):
    name = "usy"
    _long_name = "stokes_y_component"
    _standard_name = "sea_surface_wave_stokes_drift_y_velocity"
    _unit = ureg.m / ureg.s


class Stokes(MetaParameter):
    name = "us"
    _long_name = "stokes_drift"
    _standard_name = "sea_surface_wave_stokes_drift_speed"
    _unit = ureg.m / ureg.s


class StokesDir(MetaParameter):
    name = "us_dir"
    _long_name = "stokes_direction"
    _standard_name = "sea_surface_wave_stokes_drift_to_direction"
    _unit = ureg.deg


class StokesDirFrom(MetaParameter):
    name = "us_dir"
    _long_name = "stokes_direction"
    _standard_name = "sea_surface_wave_stokes_drift_from_direction"
    _unit = ureg.deg
    _cf = False


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
