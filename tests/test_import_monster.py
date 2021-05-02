# -*- coding: utf-8 -*-
import builtins
import collections
import math

from import_monster import MethodsImporter


def test_methods_importer_imported_module_callable():
    result = MethodsImporter.methods_importer("deque", [collections])
    assert result == [collections.deque]


def test_methods_importer_imported_module_not_callable():
    result = MethodsImporter.methods_importer("pi", [math])
    assert result == []


def test_methods_importer_string_module():
    result = MethodsImporter.methods_importer("deque", ["collections"])
    assert result == [collections.deque]


def test_methods_importer_multiply_strings():
    result = MethodsImporter.methods_importer("__init__", ["builtins", "collections", "math"])
    assert result == [builtins.__init__, collections.__init__, math.__init__]


def test_methods_importer_multiply_modules():
    result = MethodsImporter.methods_importer("__init__", [builtins, collections, math])
    assert result == [builtins.__init__, collections.__init__, math.__init__]
