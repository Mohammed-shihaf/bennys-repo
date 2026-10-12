"""Refund rules. Target of the coverage measures.

``tests/test_coverage_partial.py`` takes some of these branches and leaves
others on purpose, so a working coverage tool reports a share strictly between
0 and 100 for this file.
"""


def refund_amount(paid, days_since_purchase, damaged=False):
    if paid <= 0:
        return 0.0
    if damaged:                              # never taken by the tests
        return round(paid, 2)
    if days_since_purchase <= 14:
        return round(paid, 2)
    if days_since_purchase <= 30:
        return round(paid * 0.5, 2)
    return 0.0                               # never reached by the tests


def can_refund(paid, days_since_purchase, damaged=False):
    """One compound decision with three conditions, for condition coverage."""
    return paid > 0 and (damaged or days_since_purchase <= 30)


def refund_label(amount):                    # never called by the tests
    if amount > 0:
        return "refund"
    return "no refund"
