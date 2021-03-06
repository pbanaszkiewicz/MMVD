# coding: utf-8
import pytest


@pytest.mark.utils
@pytest.mark.io
def test_reading_order(order1):
    """
    Test if ``utils.read_order`` works properly.
    """
    products = ("f", "b", "a", "c", "d", "e")
    assert products == order1
