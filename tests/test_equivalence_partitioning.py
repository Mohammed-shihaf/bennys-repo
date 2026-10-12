"""Technique: equivalence partitioning. One representative per class of tier."""
import pytest

from minilab.pricing import tier_discount


@pytest.mark.parametrize("tier,expected", [
    ("standard", 0.00),      # valid class 1
    ("silver", 0.05),        # valid class 2
    ("gold", 0.10),          # valid class 3
    ("platinum", 0.00),      # invalid class: unknown tier
])
def test_one_representative_per_tier_class(tier, expected):
    assert tier_discount(tier) == expected
