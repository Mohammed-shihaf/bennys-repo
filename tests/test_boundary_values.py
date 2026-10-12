"""Technique: boundary value analysis. Each step of volume_bonus, just below and on it."""
import pytest

from minilab.pricing import combined_discount, volume_bonus


@pytest.mark.parametrize("units,expected", [
    (0, 0.0), (24, 0.0), (25, 0.02), (99, 0.02),
    (100, 0.05), (499, 0.05), (500, 0.08),
])
def test_volume_bonus_boundaries(units, expected):
    assert volume_bonus(units) == expected


def test_negative_units_are_rejected():
    with pytest.raises(ValueError):
        volume_bonus(-1)


def test_combined_discount_on_and_over_the_cap():
    assert combined_discount("gold", 100) == 0.15     # exactly the cap
    assert combined_discount("gold", 500) == 0.15     # 0.18 capped
    assert combined_discount("silver", 25) == 0.07    # under the cap
