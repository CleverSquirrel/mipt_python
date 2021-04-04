# -*- coding: utf-8 -*-
import builtins
import collections
import email
import importlib
import sys
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

            if callable(getattr(mod, method_name, None)):
                callable_objects.append(getattr(mod, method_name, None))

            # callable_objects.append(getattr(mod, method_name, None))

        except ImportError:
            continue

    return callable_objects


print(methods_importer("__init__", ["builtins", "collections", "email"]))
# [<method-wrapper '__init__' of module object at 0x7fc4fcd6b860>,
# <method-wrapper '__init__' of module object at 0x7fc4fe037ea0>,
# <method-wrapper '__init__' of module object at 0x7fc4fe06a040>]

print(methods_importer("__init__", [builtins, collections, email]))
# [<method-wrapper '__init__' of module object at 0x7fc4fcd6b860>,
# <method-wrapper '__init__' of module object at 0x7fc4fe037ea0>,
# <method-wrapper '__init__' of module object at 0x7fc4fe06a040>]

print(methods_importer("deque", ["collections"]))
# [<class 'collections.deque'>]

print(methods_importer("deque", [collections]))
# [<class 'collections.deque'>]

print(methods_importer("parser", [email]))
# should be: class email.parser
# why doesn't work?

print(sys.meta_path)
# [<class '_frozen_importlib.BuiltinImporter'>,
# <class '_frozen_importlib.FrozenImporter'>,
# <class '_frozen_importlib_external.PathFinder'>]
