# -*- coding: utf-8 -*-
import builtins
import collections
import heapq  # noqa
import importlib
import sys
from types import ModuleType
from typing import Callable, List, Union


def methods_importer(
    method_name: str, modules: List[Union[str, ModuleType]]
) -> List[Callable]:
    callable_modules = []
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Must be list of strings or ModuleType")

            if callable(getattr(mod, method_name, None)):
                callable_modules.append(mod)

            # callable_modules.append(mod)

        except ImportError:
            continue

    return callable_modules


print(methods_importer("__import__", ["builtins"]))
# [<module 'builtins' (built-in)>]

print(methods_importer("__import__", [builtins]))
# [<module 'builtins' (built-in)>]

print(methods_importer("deque", ["collections"]))
# [<module 'collections' from '/Library/Frameworks/Python.framework/Versions/
# 3.9/lib/python3.9/collections/__init__.py'>]

print(methods_importer("deque", [collections]))
# [<module 'collections' from '/Library/Frameworks/Python.framework/Versions/
# 3.9/lib/python3.9/collections/__init__.py'>]

print(methods_importer("mime", ["email"]))
# should be:
# [<module 'email' from '/Library/Frameworks/Python.framework/Versions/3.9/
# lib/python3.9/email/__init__.py'>]
# why doesn't work?

print(sys.meta_path)
# [<class '_frozen_importlib.BuiltinImporter'>,
# <class '_frozen_importlib.FrozenImporter'>,
# <class '_frozen_importlib_external.PathFinder'>]
