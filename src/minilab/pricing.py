"""Discount and shipping rules. Target of the test-technique suites."""

TIER_DISCOUNT = {"standard": 0.00, "silver": 0.05, "gold": 0.10}
MAX_DISCOUNT = 0.15


def tier_discount(tier):
    """Three valid tiers and one invalid class: the equivalence-partitioning target."""
    return TIER_DISCOUNT.get(tier, 0.0)


def volume_bonus(units):
    """Steps at 25, 100 and 500 units: the boundary-value target."""
    if units < 0:
        raise ValueError("units must not be negative")
    if units >= 500:
        return 0.08
    if units >= 100:
        return 0.05
    if units >= 25:
        return 0.02
    return 0.0


def combined_discount(tier, units):
    total = tier_discount(tier) + volume_bonus(units)
    return round(min(total, MAX_DISCOUNT), 4)


def shipping_fee(express, heavy, member):
    """Three conditions, eight rules: the decision-table target."""
    if express and heavy:
        fee = 30.0
    elif express:
        fee = 15.0
    elif heavy:
        fee = 12.0
    else:
        fee = 5.0
    if member and not express:
        fee = 0.0
    return fee
