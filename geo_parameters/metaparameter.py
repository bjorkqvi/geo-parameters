from abc import ABC, abstractmethod
import numpy as np
from typing import Union
from pint import Unit


class MetaParameter(ABC):
    _cf = True

    def __init__(self, name: str = ""):
        self.name = name or self.name

    @staticmethod
    @abstractmethod
    def _long_name() -> str:
        pass

    @staticmethod
    @abstractmethod
    def _standard_name() -> str:
        pass

    @staticmethod
    @abstractmethod
    def _unit() -> str:
        pass

    @classmethod
    def cf(cls) -> bool:
        return cls._cf

    @classmethod
    def long_name(cls) -> str:
        return cls._long_name

    @classmethod
    def standard_name(cls, strict: bool = False, alias: bool = False) -> str:
        names = np.atleast_1d(cls._standard_name)
        if cls.cf() or not strict:
            if alias:
                return str(names[-1])
            return str(names[0])

        return ""

    @classmethod
    def standard_aliases(cls, strict=False) -> list[str]:
        """Returns a list of all aliases, possible a list of only one name"""
        if cls.cf() or not strict:
            if isinstance(cls._standard_name, list):
                return cls._standard_name
            else:
                return [cls._standard_name]

        return [""]

    @classmethod
    def unit(cls) -> Unit:
        return cls._unit

    def quantify(self):
        return self * self.unit()

    @classmethod
    def cf(cls) -> str:
        return cls._cf

    @classmethod
    def meta_dict(cls, alias: bool = False) -> dict:
        return {
            "short_name": cls.name,
            "long_name": cls.long_name(),
            "standard_name": cls.standard_name(alias=alias),
            "unit": str(cls.unit()),
        }

    @classmethod
    def find_me_in_ds(
        cls, ds, return_first: bool = False
    ) -> Union[list[str], str, None]:
        """Takes an Xarray Dataset and returns list of all variable names that matches the parameter based on standard_name

        If return_first = True, then returns first name as a sting"""
        data_vars = list(ds.data_vars)
        coords = list(ds.coords)

        if not return_first:
            vars = []

        for var in data_vars:
            if hasattr(ds.get(var), "standard_name"):
                if ds.get(var).standard_name in cls.standard_aliases():
                    if return_first:
                        return var
                    else:
                        vars.append(var)

        for var in coords:
            if hasattr(ds.get(var), "standard_name"):
                if ds.get(var).standard_name in cls.standard_aliases():
                    if return_first:
                        return var
                    else:
                        vars.append(var)

        if return_first:
            return None
        else:
            return vars

    @classmethod
    def dir_type(cls) -> str:
        for std_name in cls.standard_aliases():
            if "to_direction" in std_name:
                return "to"
            if "from_direction" in std_name:
                return "from"
        return None
