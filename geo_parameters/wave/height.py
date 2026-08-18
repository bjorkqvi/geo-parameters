
from .wave import WaveParameter

class Hs(WaveParameter):
    name = "hs"
    _long_name = "significant_wave_height"
    _standard_name = [
        "sea_surface_wave_significant_height",
        "significant_height_of_wind_and_swell_waves",
    ]
    _unit = 'm'


class HsSwell(WaveParameter):
    name = "hs_swell"
    _long_name = "significant_swell_height"
    _standard_name = [
        "sea_surface_swell_wave_significant_height",
        "significant_height_of_swell_waves",
    ]
    _unit = 'm'


class HsSwell1(WaveParameter):
    name = "hs_swell1"
    _long_name = "significant_primary_swell_height"
    _standard_name = "sea_surface_primary_swell_wave_significant_height"
    _unit = 'm'


class HsSwell2(WaveParameter):
    name = "hs_swell2"
    _long_name = "significant_secondary_swell_height"
    _standard_name = "sea_surface_secondary_swell_wave_significant_height"
    _unit = 'm'


class HsSwell3(WaveParameter):
    name = "hs_swell3"
    _long_name = "significant_tertiary_swell_height"
    _standard_name = "sea_surface_tertiary_swell_wave_significant_height"
    _unit = 'm'


class HsSea(WaveParameter):
    name = "hs_sea"
    _long_name = "significant_wind_sea_height"
    _standard_name = [
        "sea_surface_wind_wave_significant_height",
        "significant_height_of_wind_waves",
    ]
    _unit = 'm'


class HsIG(WaveParameter):
    name = "hs_ig"
    _long_name = "significant_infragravity_wave_height"
    _standard_name = "sea_surface_infragravity_wave_significant_height"
    _unit = 'm'


class Hmax(WaveParameter):
    name = "hmax"
    _long_name = "maximum_wave_heigh"
    _standard_name = "sea_surface_wave_maximum_height"
    _unit = 'm'


class EtaMax(WaveParameter):
    name = "eta_max"
    _long_name = "maximum_crest_heigh"
    _standard_name = "sea_surface_wave_maximum_crest_height"
    _unit = 'm'


class Hs110(WaveParameter):
    name = "hs_110"
    _long_name = "highest_tenth_wave_heigh"
    _standard_name = "sea_surface_wave_mean_height_of_highest_tenth"
    _unit = 'm'
