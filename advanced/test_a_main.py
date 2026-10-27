import pytest

from advanced_main import (
    temperature_in_safe_range,
    can_afford_with_tip,
    meets_average,
    initials_match,
)


# --------------------------------------------------
# temperature_in_safe_range()
# --------------------------------------------------

@pytest.mark.parametrize(
    "celsius, minimum_f, maximum_f, expected",
    [
        (0, 32, 100, True),
        (100, 32, 212, True),
        (-40, -40, 50, True),
        (20, 70, 100, False),
        (30, 50, 80, False),
    ],
)
def test_temperature_in_safe_range(
    celsius,
    minimum_f,
    maximum_f,
    expected,
):
    assert temperature_in_safe_range(
        celsius,
        minimum_f,
        maximum_f,
    ) is expected


# --------------------------------------------------
# can_afford_with_tip()
# --------------------------------------------------

@pytest.mark.parametrize(
    "balance, cost, tip_percent, expected",
    [
        (100.0, 80.0, 10, True),
        (50.0, 50.0, 0, True),
        (55.0, 50.0, 10, True),
        (54.99, 50.0, 10, False),
        (20.0, 25.0, 20, False),
    ],
)
def test_can_afford_with_tip(
    balance,
    cost,
    tip_percent,
    expected,
):
    assert can_afford_with_tip(
        balance,
        cost,
        tip_percent,
    ) is expected


# --------------------------------------------------
# meets_average()
# --------------------------------------------------

@pytest.mark.parametrize(
    "score1, score2, score3, required_average, expected",
    [
        (80, 90, 100, 90, True),
        (70, 80, 90, 80, True),
        (79, 80, 80, 80, False),
        (100, 100, 100, 100, True),
        (50, 60, 70, 65, False),
    ],
)
def test_meets_average(
    score1,
    score2,
    score3,
    required_average,
    expected,
):
    assert meets_average(
        score1,
        score2,
        score3,
        required_average,
    ) is expected


# --------------------------------------------------
# initials_match()
# --------------------------------------------------

@pytest.mark.parametrize(
    "first_name, last_name, expected_initials, expected",
    [
        ("Ada", "Lovelace", "AL", True),
        ("ada", "lovelace", "al", True),
        ("Grace", "Hopper", "gh", True),
        ("Alan", "Turing", "AT", True),
        ("Alan", "Turing", "AG", False),
    ],
)
def test_initials_match(
    first_name,
    last_name,
    expected_initials,
    expected,
):
    assert initials_match(
        first_name,
        last_name,
        expected_initials,
    ) is expected