from .parameter_funcs import (
    list_of_parameters,
    dict_of_parameters,
    create_parameter_dict,
    get,
    shortget,
)

from . import wave, wind, ocean, grid, atm

from .metaparameter import decode, is_same_class,is_gp, is_gp_instance, is_gp_class
