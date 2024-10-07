from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg

from .relationships import RELATIONSHIPS


class WaveParameter(MetaParameter):
    @classmethod
    def my_family(cls):
        """Returns the dictonary containing the parameters where cls is in"""
        for rel in RELATIONSHIPS:
            for param in rel.values():
                if type(cls()).__name__ == param:
                    # This needs to be done to circument circular imports etc
                    eval_rel = {}
                    for key, value in rel.items():
                        eval_rel[key] = eval(value)
                    return eval_rel

        return None


## Wave heights
class Hs(WaveParameter):
    name = "hs"
    _long_name = "significant_wave_height"
    _standard_name = [
        "sea_surface_wave_significant_height",
        "significant_height_of_wind_and_swell_waves",
    ]
    _unit = ureg.m


class HsSwell(WaveParameter):
    name = "hs_swell"
    _long_name = "significant_swell_height"
    _standard_name = [
        "sea_surface_swell_wave_significant_height",
        "significant_height_of_swell_waves",
    ]
    _unit = ureg.m


class HsSwell1(WaveParameter):
    name = "hs_swell1"
    _long_name = "significant_primary_swell_height"
    _standard_name = "sea_surface_primary_swell_wave_significant_height"
    _unit = ureg.m


class HsSwell2(WaveParameter):
    name = "hs_swell2"
    _long_name = "significant_secondary_swell_height"
    _standard_name = "sea_surface_secondary_swell_wave_significant_height"
    _unit = ureg.m


class HsSwell3(WaveParameter):
    name = "hs_swell3"
    _long_name = "significant_tertiary_swell_height"
    _standard_name = "sea_surface_tertiary_swell_wave_significant_height"
    _unit = ureg.m


class HsSea(WaveParameter):
    name = "hs_sea"
    _long_name = "significant_wind_sea_height"
    _standard_name = [
        "sea_surface_wind_wave_significant_height",
        "significant_height_of_wind_waves",
    ]
    _unit = ureg.m


class HsIG(WaveParameter):
    name = "hs_ig"
    _long_name = "significant_infragravity_wave_height"
    _standard_name = "sea_surface_infragravity_wave_significant_height"
    _unit = ureg.m


class Hmax(WaveParameter):
    name = "hmax"
    _long_name = "maximum_wave_heigh"
    _standard_name = "sea_surface_wave_maximum_height"
    _unit = ureg.m


class EtaMax(WaveParameter):
    name = "eta_max"
    _long_name = "maximum_crest_heigh"
    _standard_name = "sea_surface_wave_maximum_crest_height"
    _unit = ureg.m


class Hs110(WaveParameter):
    name = "hs_110"
    _long_name = "highest_tenth_wave_heigh"
    _standard_name = "sea_surface_wave_mean_height_of_highest_tenth"
    _unit = ureg.m


## Wave frequencies
class Fp(WaveParameter):
    name = "fp"
    _long_name = "peak_wave_frequency"
    _standard_name = "sea_surface_wave_frequency_at_variance_spectral_density_maximum"
    _unit = ureg.s**-1


class Fm(WaveParameter):
    name = "fm"
    _long_name = "mean_wave_frequency"
    _standard_name = "sea_surface_wave_mean_frequency"
    _unit = ureg.s**-1
    _cf = False


class Wp(WaveParameter):
    name = "wp"
    _long_name = "peak_angular_wave_frequency"
    _standard_name = (
        "sea_surface_angular_wave_frequency_at_variance_spectral_density_maximum"
    )
    _unit = ureg.rad * ureg.s**-1
    _cf = False


class Wm(WaveParameter):
    name = "wm"
    _long_name = "mean_angular_wave_frequency"
    _standard_name = "sea_surface_angular_wave_mean_frequency"
    _unit = ureg.rad * ureg.s**-1
    _cf = False


## Wave periods
class Tp(WaveParameter):
    name = "tp"
    _long_name = "peak_wave_period"
    _standard_name = "sea_surface_wave_period_at_variance_spectral_density_maximum"
    _unit = ureg.s


class Tz(WaveParameter):
    name = "tz"
    _long_name = "zero_upcrossing_period"
    _standard_name = [
        "sea_surface_wave_mean_period",
        "sea_surface_wave_zero_upcrossing_period",
    ]
    _unit = ureg.s


class T13(WaveParameter):
    name = "t13"
    _long_name = "significant_wave_period"
    _standard_name = "sea_surface_wave_significant_period"
    _unit = ureg.s


class T110(WaveParameter):
    name = "t110"
    _long_name = "highest_tenth_wave_period"
    _standard_name = "sea_surface_wave_mean_period_of_highest_tenth"
    _unit = ureg.s


class Tm01(WaveParameter):
    name = "tm01"
    _long_name = "first_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = ureg.s


class Tm_10(WaveParameter):
    name = "tm_10"
    _long_name = "inverse_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = ureg.s


class Tm02(WaveParameter):
    name = "tm02"
    _long_name = "second_moment_mean_wave_period"
    _standard_name = "sea_surface_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = ureg.s


class TpSwell(WaveParameter):
    name = "tp_swell"
    _long_name = "peak_wave_period_of_swell"
    _standard_name = (
        "sea_surface_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class Tm01Swell(WaveParameter):
    name = "tm01_swell"
    _long_name = "first_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = ureg.s


class Tm_10Swell(WaveParameter):
    name = "tm_10_swell"
    _long_name = "inverse_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = ureg.s


class Tm02Swell(WaveParameter):
    name = "tm02_swell"
    _long_name = "second_moment_mean_wave_period_of_swell"
    _standard_name = "sea_surface_swell_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = ureg.s


class TpSwell1(WaveParameter):
    name = "tp_swell1"
    _long_name = "peak_wave_period_of_primary_swell"
    _standard_name = (
        "sea_surface_primary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class TpSwell2(WaveParameter):
    name = "tp_swell2"
    _long_name = "peak_wave_period_of_secondary_swell"
    _standard_name = (
        "sea_surface_secondary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class TpSwell3(WaveParameter):
    name = "tp_swell3"
    _long_name = "peak_wave_period_of_tertiary_swell"
    _standard_name = (
        "sea_surface_tertiary_swell_wave_period_at_variance_spectral_density_maximum"
    )
    _unit = ureg.s


class TpSea(WaveParameter):
    name = "tp_sea"
    _long_name = "peak_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_period_at_variance_spectral_density_maximum"
    _unit = ureg.s


class Tm01Sea(WaveParameter):
    name = "tm01_sea"
    _long_name = "first_moment_mean_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_first_frequency_moment"
    _unit = ureg.s


class Tm_10Sea(WaveParameter):
    name = "tm_10_sea"
    _long_name = "inverse_moment_mean_wave_period_of_wind_sea"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_inverse_frequency_moment"
    _unit = ureg.s


class Tm02Sea(WaveParameter):
    name = "tm02_sea"
    _long_name = "second_moment_mean_wave_period_of_wind_swa"
    _standard_name = "sea_surface_wind_wave_mean_period_from_variance_spectral_density_second_frequency_moment"
    _unit = ureg.s


## Directions
class Dirm(WaveParameter):
    name = "dirm"
    _long_name = "mean_wave_direction"
    _standard_name = "sea_surface_wave_from_direction"
    _unit = ureg.deg


class DirmTo(WaveParameter):
    name = "dirm"
    _long_name = "mean_wave_direction"
    _standard_name = "sea_surface_wave_to_direction"
    _unit = ureg.deg


class Dirp(WaveParameter):
    name = "dirp"
    _long_name = "peak_wave_direction"
    _standard_name = (
        "sea_surface_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirpTo(WaveParameter):
    name = "dirp"
    _long_name = "peak_wave_direction"
    _standard_name = (
        "sea_surface_wave_to_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg
    _cf = False


class DirmSwell(WaveParameter):
    name = "dirm_swell"
    _long_name = "mean_swell_direction"
    _standard_name = "sea_surface_swell_wave_from_direction"
    _unit = ureg.deg


class DirmSwellTo(WaveParameter):
    name = "dirm_swell"
    _long_name = "mean_swell_direction"
    _standard_name = [
        "sea_surface_swell_wave_to_direction",
        "direction_of_swell_wave_velocity",
    ]
    _unit = ureg.deg


class DirpSwell(WaveParameter):
    name = "dirp_swell"
    _long_name = "peak_swell_direction"
    _standard_name = (
        "sea_surface_swell_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirpSwellTo(WaveParameter):
    name = "dirp_swell"
    _long_name = "peak_swell_direction"
    _standard_name = (
        "sea_surface_swell_wave_to_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg
    _cf = False


class DirmSwell1(WaveParameter):
    name = "dirm_swell1"
    _long_name = "mean_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_from_direction"
    _unit = ureg.deg


class DirmSwell1To(WaveParameter):
    name = "dirm_swell1"
    _long_name = "mean_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_to_direction"

    _unit = ureg.deg
    _cf = False


class DirpSwell1(WaveParameter):
    name = "dirp_swell1"
    _long_name = "peak_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg


class DirpSwell1To(WaveParameter):
    name = "dirp_swell1"
    _long_name = "peak_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_to_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class DirmSwell2(WaveParameter):
    name = "dirm_swell2"
    _long_name = "mean_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_from_direction"
    _unit = ureg.deg


class DirmSwell2To(WaveParameter):
    name = "dirm_swell2"
    _long_name = "mean_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_to_direction"

    _unit = ureg.deg
    _cf = False


class DirpSwell2(WaveParameter):
    name = "dirp_swell2"
    _long_name = "peak_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg


class DirpSwell2To(WaveParameter):
    name = "dirp_swell2"
    _long_name = "peak_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_to_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class DirmSwell3(WaveParameter):
    name = "dirm_swell3"
    _long_name = "mean_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_from_direction"
    _unit = ureg.deg


class DirmSwell3To(WaveParameter):
    name = "dirm_swell3"
    _long_name = "mean_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_to_direction"

    _unit = ureg.deg
    _cf = False


class DirpSwell3(WaveParameter):
    name = "dirp_swell3"
    _long_name = "peak_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg


class DirpSwell3To(WaveParameter):
    name = "dirp_swell3"
    _long_name = "peak_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_to_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class DirmSea(WaveParameter):
    name = "dirm_sea"
    _long_name = "mean_wind_sea_direction"
    _standard_name = "sea_surface_wind_wave_from_direction"
    _unit = ureg.deg


class DirmSeaTo(WaveParameter):
    name = "dirm_sea"
    _long_name = "mean_wind_sea_direction"
    _standard_name = [
        "sea_surface_wind_wave_to_direction",
        "direction_of_wind_wave_velocity",
    ]
    _unit = ureg.deg


class DirpSea(WaveParameter):
    name = "dirp_sea"
    _long_name = "peak_wind_sea_direction"
    _standard_name = (
        "sea_surface_wind_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class DirpSeaTo(WaveParameter):
    name = "dirp_sea"
    _long_name = "peak_wind_sea_direction"
    _standard_name = (
        "sea_surface_wind_wave_to_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg
    _cf = False


## Spreading
class Spr(WaveParameter):
    name = "spr"
    _long_name = "wave_directional_spread"
    _standard_name = "sea_surface_wave_directional_spread"
    _unit = ureg.deg


class SprP(WaveParameter):
    name = "sprp"
    _long_name = "peak_wave_directional_spread"
    _standard_name = (
        "sea_surface_wave_directional_spread_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg


class SprSwell(WaveParameter):
    name = "spr_swell"
    _long_name = "swell_directional_spread"
    _standard_name = "sea_surface_swell_wave_directional_spread"
    _unit = ureg.deg


class SprPSwell(WaveParameter):
    name = "sprp_swell"
    _long_name = "peak_swell_directional_spread"
    _standard_name = (
        "sea_surface_swell_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg
    _cf = False


class SprSwell1(WaveParameter):
    name = "spr_swell1"
    _long_name = "primary_swell_directional_spread"
    _standard_name = "sea_surface_primary_swell_wave_directional_spread"
    _unit = ureg.deg


class SprPSwell1(WaveParameter):
    name = "sprp_swell1"
    _long_name = "peak_primary_swell_directional_spread"
    _standard_name = "sea_surface_primary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class SprSwell2(WaveParameter):
    name = "spr_swell2"
    _long_name = "secondary_swell_directional_spread"
    _standard_name = "sea_surface_scondary_swell_wave_directional_spread"
    _unit = ureg.deg


class SprPSwell2(WaveParameter):
    name = "sprp_swell2"
    _long_name = "peak_secondary_swell_directional_spread"
    _standard_name = "sea_surface_secondary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class SprSwell3(WaveParameter):
    name = "spr_swell3"
    _long_name = "tertiary_swell_directional_spread"
    _standard_name = "sea_surface_tertiary_swell_wave_directional_spread"
    _unit = ureg.deg


class SprPSwell3(WaveParameter):
    name = "sprp_swell3"
    _long_name = "peak_tertiary_swell_directional_spread"
    _standard_name = "sea_surface_tertiary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = ureg.deg
    _cf = False


class SprSea(WaveParameter):
    name = "spr_sea"
    _long_name = "wind_sea_directional_spread"
    _standard_name = "sea_surface_wind_wave_directional_spread"
    _unit = ureg.deg


class SprPSea(WaveParameter):
    name = "sprp_sea"
    _long_name = "peak_wind_sea_directional_spread"
    _standard_name = (
        "sea_surface_wind_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = ureg.deg
    _cf = False


## Spectral
class Ef(WaveParameter):
    name = "ef"
    _long_name = "spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.s


class Efth(WaveParameter):
    name = "efth"
    _long_name = "directional_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.s / ureg.rad


class Fk(WaveParameter):
    name = "fk"
    _long_name = "wavenumer_spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.m


class Fkth(WaveParameter):
    name = "fkth"
    _long_name = "directional_wavenumber_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.m / ureg.rad


class Qv(WaveParameter):
    name = "qv"
    _long_name = "inverse_phase_speed_spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.m * ureg.s


class Qvth(WaveParameter):
    name = "qvth"
    _long_name = "directional_inverse_phase_speed_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = ureg.m * ureg.m * ureg.m * ureg.s / ureg.rad


class Freq(WaveParameter):
    name = "freq"
    _long_name = "frequency"
    _standard_name = ["wave_frequency", "sea_surface_wave_frequency"]
    _unit = ureg.s**-1


class Dirs(WaveParameter):
    name = "dirs"
    _long_name = "wave_direction"
    _standard_name = "wave_direction"
    _unit = ureg.deg
    _cf = False


class DirsFrom(WaveParameter):
    name = "dirs"
    _long_name = "wave_direction"
    _standard_name = "wave_from_direction"
    _unit = ureg.deg
    _cf = False


class DirsTo(WaveParameter):
    name = "dirs"
    _long_name = "wave_direction"
    _standard_name = "wave_to_direction"
    _unit = ureg.deg
    _cf = False


##Stokes
class EastStokes(WaveParameter):
    name = "x_stokes"
    _long_name = "east_stokes_component"
    _standard_name = "sea_surface_wave_stokes_drift_eastward_velocity"
    _unit = ureg.m / ureg.s


class NorthStokes(WaveParameter):
    name = "y_stokes"
    _long_name = "north_stokes_component"
    _standard_name = "sea_surface_wave_stokes_drift_northward_velocity"
    _unit = ureg.m / ureg.s


class XStokes(WaveParameter):
    name = "x_stokes"
    _long_name = "x_stokes_component"
    _standard_name = "sea_surface_wave_stokes_drift_x_velocity"
    _unit = ureg.m / ureg.s


class YStokes(WaveParameter):
    name = "y_stokes"
    _long_name = "y_stokes_component"
    _standard_name = "sea_surface_wave_stokes_drift_y_velocity"
    _unit = ureg.m / ureg.s


class Stokes(WaveParameter):
    name = "stokes"
    _long_name = "stokes_drift"
    _standard_name = "sea_surface_wave_stokes_drift_speed"
    _unit = ureg.m / ureg.s


class StokesDir(WaveParameter):
    name = "stokes_dir"
    _long_name = "stokes_direction"
    _standard_name = "sea_surface_wave_stokes_drift_to_direction"
    _unit = ureg.deg


class StokesDirFrom(WaveParameter):
    name = "stokes_dir"
    _long_name = "stokes_direction"
    _standard_name = "sea_surface_wave_stokes_drift_from_direction"
    _unit = ureg.deg
    _cf = False


## Moments (non-standard)
class M0(WaveParameter):
    name = "m0"
    _long_name = "zeroth_wave_moment"
    _standard_name = "sea_surface_zeroth_wave_moment"
    _unit = ureg.m**2
    _cf = False


class M1(WaveParameter):
    name = "m1"
    _long_name = "first_wave_moment"
    _standard_name = "sea_surface_first_wave_moment"
    _unit = ureg.m**2 / ureg.s
    _cf = False


class M_1(WaveParameter):
    name = "m_1"
    _long_name = "first_inverse_wave_moment"
    _standard_name = "sea_surface_first_inverse_wave_moment"
    _unit = ureg.m**2 * ureg.s
    _cf = False


class M2(WaveParameter):
    name = "m2"
    _long_name = "second_wave_moment"
    _standard_name = "sea_surface_second_wave_moment"
    _unit = ureg.m**2 / ureg.s**2
    _cf = False


class M3(WaveParameter):
    name = "m3"
    _long_name = "thirds_wave_moment"
    _standard_name = "sea_surface_thirds_wave_moment"
    _unit = ureg.m**2 / ureg.s**3
    _cf = False


class M4(WaveParameter):
    name = "m4"
    _long_name = "fourth_wave_moment"
    _standard_name = "sea_surface_fourth_wave_moment"
    _unit = ureg.m**2 / ureg.s**4
    _cf = False


class M5(WaveParameter):
    name = "m5"
    _long_name = "fifth_wave_moment"
    _standard_name = "sea_surface_fifth_wave_moment"
    _unit = ureg.m**2 / ureg.s**5
    _cf = False
