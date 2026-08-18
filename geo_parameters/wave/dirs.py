from .wave import WaveParameter

class Dirm(WaveParameter):
    name = "dirm"
    _long_name = "mean_wave_direction"
    _standard_name = "sea_surface_wave_from_direction"
    _unit = 'deg'


class DirmTo(WaveParameter):
    name = "dirm"
    _long_name = "mean_wave_direction"
    _standard_name = "sea_surface_wave_to_direction"
    _unit = 'deg'


class Dirp(WaveParameter):
    name = "dirp"
    _long_name = "peak_wave_direction"
    _standard_name = (
        "sea_surface_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = 'deg'


class DirpTo(WaveParameter):
    name = "dirp"
    _long_name = "peak_wave_direction"
    _standard_name = (
        "sea_surface_wave_to_direction_at_variance_spectral_density_maximum"
    )
    _unit = 'deg'
    _cf = False


class DirmSwell(WaveParameter):
    name = "dirm_swell"
    _long_name = "mean_swell_direction"
    _standard_name = "sea_surface_swell_wave_from_direction"
    _unit = 'deg'


class DirmSwellTo(WaveParameter):
    name = "dirm_swell"
    _long_name = "mean_swell_direction"
    _standard_name = [
        "sea_surface_swell_wave_to_direction",
        "direction_of_swell_wave_velocity",
    ]
    _unit = 'deg'


class DirpSwell(WaveParameter):
    name = "dirp_swell"
    _long_name = "peak_swell_direction"
    _standard_name = (
        "sea_surface_swell_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = 'deg'


class DirpSwellTo(WaveParameter):
    name = "dirp_swell"
    _long_name = "peak_swell_direction"
    _standard_name = (
        "sea_surface_swell_wave_to_direction_at_variance_spectral_density_maximum"
    )
    _unit = 'deg'
    _cf = False


class DirmSwell1(WaveParameter):
    name = "dirm_swell1"
    _long_name = "mean_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_from_direction"
    _unit = 'deg'


class DirmSwell1To(WaveParameter):
    name = "dirm_swell1"
    _long_name = "mean_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_to_direction"

    _unit = 'deg'
    _cf = False


class DirpSwell1(WaveParameter):
    name = "dirp_swell1"
    _long_name = "peak_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = 'deg'


class DirpSwell1To(WaveParameter):
    name = "dirp_swell1"
    _long_name = "peak_primary_swell_direction"
    _standard_name = "sea_surface_primary_swell_wave_to_direction_at_variance_spectral_density_maximum"
    _unit = 'deg'
    _cf = False


class DirmSwell2(WaveParameter):
    name = "dirm_swell2"
    _long_name = "mean_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_from_direction"
    _unit = 'deg'


class DirmSwell2To(WaveParameter):
    name = "dirm_swell2"
    _long_name = "mean_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_to_direction"

    _unit = 'deg'
    _cf = False


class DirpSwell2(WaveParameter):
    name = "dirp_swell2"
    _long_name = "peak_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = 'deg'


class DirpSwell2To(WaveParameter):
    name = "dirp_swell2"
    _long_name = "peak_secondary_swell_direction"
    _standard_name = "sea_surface_secondary_swell_wave_to_direction_at_variance_spectral_density_maximum"
    _unit = 'deg'
    _cf = False


class DirmSwell3(WaveParameter):
    name = "dirm_swell3"
    _long_name = "mean_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_from_direction"
    _unit = 'deg'


class DirmSwell3To(WaveParameter):
    name = "dirm_swell3"
    _long_name = "mean_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_to_direction"

    _unit = 'deg'
    _cf = False


class DirpSwell3(WaveParameter):
    name = "dirp_swell3"
    _long_name = "peak_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = 'deg'


class DirpSwell3To(WaveParameter):
    name = "dirp_swell3"
    _long_name = "peak_tertiary_swell_direction"
    _standard_name = "sea_surface_tertiary_swell_wave_to_direction_at_variance_spectral_density_maximum"
    _unit = 'deg'
    _cf = False


class DirmSea(WaveParameter):
    name = "dirm_sea"
    _long_name = "mean_wind_sea_direction"
    _standard_name = "sea_surface_wind_wave_from_direction"
    _unit = 'deg'


class DirmSeaTo(WaveParameter):
    name = "dirm_sea"
    _long_name = "mean_wind_sea_direction"
    _standard_name = [
        "sea_surface_wind_wave_to_direction",
        "direction_of_wind_wave_velocity",
    ]
    _unit = 'deg'


class DirpSea(WaveParameter):
    name = "dirp_sea"
    _long_name = "peak_wind_sea_direction"
    _standard_name = (
        "sea_surface_wind_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = 'deg'


class DirpSeaTo(WaveParameter):
    name = "dirp_sea"
    _long_name = "peak_wind_sea_direction"
    _standard_name = (
        "sea_surface_wind_wave_to_direction_at_variance_spectral_density_maximum"
    )
    _unit = 'deg'
    _cf = False