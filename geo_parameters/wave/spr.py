from .wave import WaveParameter

class Spr(WaveParameter):
    name = "spr"
    _long_name = "wave_directional_spread"
    _standard_name = "sea_surface_wave_directional_spread"
    _unit = 'deg'


class SprP(WaveParameter):
    name = "sprp"
    _long_name = "peak_wave_directional_spread"
    _standard_name = (
        "sea_surface_wave_directional_spread_at_variance_spectral_density_maximum"
    )
    _unit = 'deg'


class SprSwell(WaveParameter):
    name = "spr_swell"
    _long_name = "swell_directional_spread"
    _standard_name = "sea_surface_swell_wave_directional_spread"
    _unit = 'deg'


class SprPSwell(WaveParameter):
    name = "sprp_swell"
    _long_name = "peak_swell_directional_spread"
    _standard_name = (
        "sea_surface_swell_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = 'deg'
    _cf = False


class SprSwell1(WaveParameter):
    name = "spr_swell1"
    _long_name = "primary_swell_directional_spread"
    _standard_name = "sea_surface_primary_swell_wave_directional_spread"
    _unit = 'deg'


class SprPSwell1(WaveParameter):
    name = "sprp_swell1"
    _long_name = "peak_primary_swell_directional_spread"
    _standard_name = "sea_surface_primary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = 'deg'
    _cf = False


class SprSwell2(WaveParameter):
    name = "spr_swell2"
    _long_name = "secondary_swell_directional_spread"
    _standard_name = "sea_surface_scondary_swell_wave_directional_spread"
    _unit = 'deg'


class SprPSwell2(WaveParameter):
    name = "sprp_swell2"
    _long_name = "peak_secondary_swell_directional_spread"
    _standard_name = "sea_surface_secondary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = 'deg'
    _cf = False


class SprSwell3(WaveParameter):
    name = "spr_swell3"
    _long_name = "tertiary_swell_directional_spread"
    _standard_name = "sea_surface_tertiary_swell_wave_directional_spread"
    _unit = 'deg'


class SprPSwell3(WaveParameter):
    name = "sprp_swell3"
    _long_name = "peak_tertiary_swell_directional_spread"
    _standard_name = "sea_surface_tertiary_swell_wave_from_direction_at_variance_spectral_density_maximum"
    _unit = 'deg'
    _cf = False


class SprSea(WaveParameter):
    name = "spr_sea"
    _long_name = "wind_sea_directional_spread"
    _standard_name = "sea_surface_wind_wave_directional_spread"
    _unit = 'deg'


class SprPSea(WaveParameter):
    name = "sprp_sea"
    _long_name = "peak_wind_sea_directional_spread"
    _standard_name = (
        "sea_surface_wind_wave_from_direction_at_variance_spectral_density_maximum"
    )
    _unit = 'deg'
    _cf = False