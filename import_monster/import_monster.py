# -*- coding: utf-8 -*-
import importlib
from types import ModuleType
from typing import Callable, List, Union


def methods_importer(method_name: str, modules: List[Union[str, ModuleType]]) -> List[Callable]:
    callable_objects = []
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Must be list of strings or ModuleType")

            callable_pointer = getattr(mod, method_name, None)
            if callable(callable_pointer):
                callable_objects.append(callable_pointer)

        except ImportError:
            continue

    return callable_objects
