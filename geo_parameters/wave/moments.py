from .wave import WaveParameter

class M0(WaveParameter):
    name = "m0"
    _long_name = "zeroth_wave_moment"
    _standard_name = "sea_surface_zeroth_wave_moment"
    _unit = 'm**2'
    _cf = False


class M1(WaveParameter):
    name = "m1"
    _long_name = "first_wave_moment"
    _standard_name = "sea_surface_first_wave_moment"
    _unit = 'm**2/s'
    _cf = False


class M_1(WaveParameter):
    name = "m_1"
    _long_name = "first_inverse_wave_moment"
    _standard_name = "sea_surface_first_inverse_wave_moment"
    _unit = 'm**2*s'
    _cf = False


class M2(WaveParameter):
    name = "m2"
    _long_name = "second_wave_moment"
    _standard_name = "sea_surface_second_wave_moment"
    _unit = 'm**2/s**2'
    _cf = False


class M3(WaveParameter):
    name = "m3"
    _long_name = "thirds_wave_moment"
    _standard_name = "sea_surface_thirds_wave_moment"
    _unit = 'm**2/s**3'
    _cf = False


class M4(WaveParameter):
    name = "m4"
    _long_name = "fourth_wave_moment"
    _standard_name = "sea_surface_fourth_wave_moment"
    _unit = 'm**2/s**4'
    _cf = False


class M5(WaveParameter):
    name = "m5"
    _long_name = "fifth_wave_moment"
    _standard_name = "sea_surface_fifth_wave_moment"
    _unit = 'm**2/s**5'
    _cf = False
