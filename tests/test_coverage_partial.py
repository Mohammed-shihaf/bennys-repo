"""Coverage target. Leaves the damaged, over-30-day and refund_label paths untested on purpose."""
from minilab.refunds import can_refund, refund_amount


def test_nothing_paid_means_nothing_refunded():
    assert refund_amount(0, 3) == 0.0


def test_full_refund_inside_fourteen_days():
    assert refund_amount(40.0, 14) == 40.0


def test_half_refund_inside_thirty_days():
    assert refund_amount(40.0, 20) == 20.0


def test_can_refund_inside_the_window():
    assert can_refund(40.0, 20) is True
    assert can_refund(0, 20) is False
