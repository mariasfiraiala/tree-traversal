import pytest
from tree import *


@pytest.fixture(scope="session", autouse=True)
def tree():
    tree = Tree()
    tree.add(0)
    tree.add(8)

    return tree

def test_find1(tree):
    assert tree.find(0) is not None

def test_find2(tree):
    assert tree.find(1024) is None
