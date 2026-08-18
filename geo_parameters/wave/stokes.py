from .wave import WaveParameter

class EastStokes(WaveParameter):
    name = "x_stokes"
    _long_name = "east_stokes_component"
    _standard_name = "sea_surface_wave_stokes_drift_eastward_velocity"
    _unit = 'm/s'


class NorthStokes(WaveParameter):
    name = "y_stokes"
    _long_name = "north_stokes_component"
    _standard_name = "sea_surface_wave_stokes_drift_northward_velocity"
    _unit = 'm/s'


class XStokes(WaveParameter):
    name = "x_stokes"
    _long_name = "x_stokes_component"
    _standard_name = "sea_surface_wave_stokes_drift_x_velocity"
    _unit = 'm/s'


class YStokes(WaveParameter):
    name = "y_stokes"
    _long_name = "y_stokes_component"
    _standard_name = "sea_surface_wave_stokes_drift_y_velocity"
    _unit = 'm/s'


class Stokes(WaveParameter):
    name = "stokes"
    _long_name = "stokes_drift"
    _standard_name = "sea_surface_wave_stokes_drift_speed"
    _unit = 'm/s'


class StokesDir(WaveParameter):
    name = "stokes_dir"
    _long_name = "stokes_direction"
    _standard_name = "sea_surface_wave_stokes_drift_to_direction"
    _unit = 'deg'


class StokesDirFrom(WaveParameter):
    name = "stokes_dir"
    _long_name = "stokes_direction"
    _standard_name = "sea_surface_wave_stokes_drift_from_direction"
    _unit = 'deg'
    _cf = False