from .wave import WaveParameter

class Ef(WaveParameter):
    name = "ef"
    _long_name = "spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = 'm**2/Hz'


class Efth(WaveParameter):
    name = "efth"
    _long_name = "directional_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = 'm**2/Hz/rad'


class Fk(WaveParameter):
    name = "fk"
    _long_name = "wavenumer_spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = 'm**3'


class Fkth(WaveParameter):
    name = "fkth"
    _long_name = "directional_wavenumber_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = 'm**3/rad'

class Qv(WaveParameter):
    name = "qv"
    _long_name = "inverse_phase_speed_spectral_density"
    _standard_name = "sea_surface_wave_variance_spectral_density"
    _unit = 'm**3*s'


class Qvth(WaveParameter):
    name = "qvth"
    _long_name = "directional_inverse_phase_speed_spectral_density"
    _standard_name = "sea_surface_wave_directional_variance_spectral_density"
    _unit = 'm**3*s/rad'


class Efth_max(WaveParameter):
    name = "efth_max"
    _long_name = "maximum_of_directional_variance_spectral_density"
    _standard_name = "sea_surface_wave_energy_at_variance_spectral_density_maximum"
    _unit = 'm**2/Hz/rad'


class Ef_max(WaveParameter):
    name = "emax"
    _long_name = "maximum_of_variance_spectral_density"
    _standard_name = "sea_surface_wave_energy_at_variance_spectral_density_maximum"
    _unit = 'm**2/Hz'


class Freq(WaveParameter):
    name = "freq"
    _long_name = "frequency"
    _standard_name = ["wave_frequency", "sea_surface_wave_frequency"]
    _unit = 'Hz'

class Dirs(WaveParameter):
    name = "dirs"
    _long_name = "wave_direction"
    _standard_name = "wave_direction"
    _unit = 'deg'
    _cf = False


class DirsFrom(WaveParameter):
    name = "dirs"
    _long_name = "wave_direction"
    _standard_name = "wave_from_direction"
    _unit = 'deg'
    _cf = False


class DirsTo(WaveParameter):
    name = "dirs"
    _long_name = "wave_direction"
    _standard_name = "wave_to_direction"
    _unit = 'deg'
    _cf = False
