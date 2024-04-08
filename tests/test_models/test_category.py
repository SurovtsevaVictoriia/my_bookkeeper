from inspect import isgenerator
# from ...bookkeeper.dirs.models_dir.base import db
import pytest

from bookkeeper.dirs.models_dir.category import Category


def test_get_id():
    c = Category(name = 'name', id = 0)
    assert c.get_id() == 0
