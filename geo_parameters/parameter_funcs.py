from . import wave, ocean, wind
import inspect
from .metaparameter import MetaParameter


def list_of_parameters() -> list:
    """Get a list of all available geo-parameters"""
    parameter_list = []
    modules_to_inspect = [wave, ocean, wind]
    for module in modules_to_inspect:
        for __, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                if issubclass(obj, MetaParameter) and not obj == MetaParameter:
                    parameter_list.append(obj)
    return parameter_list


def dict_of_parameters(short: bool = False, alias: bool = False) -> dict:
    """Get a dict of all availabel geo-parameters.

    Key is either standard_name (default), alias (alias=True) or non standard short name (short=True)
    """
    if short:
        return {c.name: c for c in list_of_parameters()}
    return {c.standard_name(alias=alias): c for c in list_of_parameters()}


def shortget(key: str):
    """Find a geo-parameter based on a short string. Warning, these short strings follow no standard convention."""
    return dict_of_parameters(short=True).get(key)


def get(key: str):
    """Find a geo-parameter based on a string of the standard_name (or an alias)."""
    return dict_of_parameters().get(key) or dict_of_parameters(alias=True).get(key)


def create_parameter_dict(parameter_strings: list[str]):
    """Create a dict of geo-parameters based on a list of strings of standard_names"""
    metaparameter_dict = {}
    for param in parameter_strings:
        val = get(param)
        if val is not None:
            metaparameter_dict[param] = val
    return metaparameter_dict


def decode(parameter) -> tuple[str, MetaParameter]:
    """Returns the name of the geo-parameter and the geo-parameter.
    It a string is given, the string and None is returned.
    Otherwise an error is thrown"""
    if is_gp(parameter):
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
