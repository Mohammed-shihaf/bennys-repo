"""Technique: decision table. All eight rules of shipping_fee(express, heavy, member)."""
import pytest

from minilab.pricing import shipping_fee


@pytest.mark.parametrize("express,heavy,member,expected", [
    (True,  True,  True,  30.0),
    (True,  True,  False, 30.0),
    (True,  False, True,  15.0),
    (True,  False, False, 15.0),
    (False, True,  True,  0.0),
    (False, True,  False, 12.0),
    (False, False, True,  0.0),
    (False, False, False, 5.0),
])
def test_every_rule_of_the_shipping_table(express, heavy, member, expected):
    assert shipping_fee(express, heavy, member) == expected
