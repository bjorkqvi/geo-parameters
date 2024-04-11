from .metaparameter import MetaParameter
import pint

ureg = pint.UnitRegistry()

ureg.default_format = "~C"


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
