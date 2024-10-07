from geo_parameters.metaparameter import MetaParameter
from geo_parameters.ureg import ureg
from .relationships import RELATIONSHIPS


class GridParameter(MetaParameter):
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


class Lon(GridParameter):
    name = "lon"
    _long_name = "longitude"
    _standard_name = "longitude"
    _unit = "degrees_east"


class Lat(GridParameter):
    name = "lat"
    _long_name = "latitude"
    _standard_name = "latitude"
    _unit = "degrees_north"


class X(GridParameter):
    name = "x"
    _long_name = "x_distance"
    _standard_name = "distance_in_x_direction"
    _unit = ureg.m
    _cf = False


class Y(GridParameter):
    name = "y"
    _long_name = "y_distance"
    _standard_name = "distance_in_y_direction"
    _unit = ureg.m
    _cf = False


class Inds(GridParameter):
    name = "inds"
    _long_name = "index_of_points"
    _standard_name = "index_of_geophysical_points"
    _unit = "-"
    _cf = False
