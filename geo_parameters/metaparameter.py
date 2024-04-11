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
                return names[-1]
            return names[0]

        return ""

    @classmethod
    def standard_aliases(cls, strict=False) -> list[str]:
        if cls.cf() or not strict:
            return cls._standard_name

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
    def find_me_in_ds(cls, ds) -> Union[str, None]:
        """Takes an Xarray Dataset and returns name of variable that matches the parameter based on standard_name"""
        data_vars = list(ds.data_vars)

        for var in data_vars:
            if hasattr(ds.get(var), "standard_name"):
                if ds.get(var).standard_name in cls.standard_aliases():
                    return var

        return None
