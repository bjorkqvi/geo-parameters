from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg


class Lon(MetaParameter):
    name = "lon"
    _long_name = "longitude"
    _standard_name = "longitude"
    _unit = "degrees_east"


class Lat(MetaParameter):
    name = "lat"
    _long_name = "latitude"
    _standard_name = "latitude"
    _unit = "degrees_north"


class X(MetaParameter):
    name = "x"
    _long_name = "x_distance"
    _standard_name = "distance_in_x_direction"
    _unit = ureg.m
    _cf = False


class Y(MetaParameter):
    name = "y"
    _long_name = "y_distance"
    _standard_name = "distance_in_y_direction"
    _unit = ureg.m
    _cf = False


class Inds(MetaParameter):
    name = "inds"
    _long_name = "index_of_points"
    _standard_name = "index_of_geophysical_points"
    _unit = "-"
    _cf = False
