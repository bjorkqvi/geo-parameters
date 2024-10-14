"""This module contains functions to help work with geo-parameters, such as decoding and checking"""

from .metaparameter import MetaParameter


def decode(parameter, init: bool = False) -> tuple[str, MetaParameter]:
    """Returns the name of the geo-parameter and the geo-parameter.
    If a string is given, the string and None is returned, otherwise an error is thrown.

    Examples:
    >> gp.decode(gp.wave.Hs('hsig)) -> ('hsig', gp.wave.Hs('hsig'))
    >> gp.decode('hsig') -> ('hsig', None)
    >> gp.decode(gp.wave.Hs) -> ('hs', gp.wave.Hs)
    >> gp.decode(gp.wave.Hs, init=True) -> ('hs', gp.wave.Hs())
    >> gp.decode(<xr.DataArray>) -> *** TypeError: Can only decode types 'MetaParameter' and 'str', not 'DataArray'
    """

    if is_gp(parameter):
        if init and is_gp_class(parameter):
            parameter = parameter()
        return parameter.name, parameter
    elif isinstance(parameter, str):
        return parameter, None
    else:
        raise TypeError(
            f"Can only decode types 'MetaParameter' and 'str', not '{type(parameter).__name__}'"
        )


def is_gp(parameter) -> bool:
    """Checks if the given objects is an instance or class of a geo-parameter"""
    return is_gp_instance(parameter) or is_gp_class(parameter)


def is_gp_instance(parameter) -> bool:
    """Checks if the given object is an instance of a geo-parameter"""
    return isinstance(parameter, MetaParameter)


def is_gp_class(parameter) -> bool:
    """Checks if the given object is a geo-parameter class (i.e. a subclass of MetaParameter"""
    try:
        return issubclass(parameter, MetaParameter)
    except TypeError:
        return False
