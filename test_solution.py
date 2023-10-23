import pytest
from copy import deepcopy

from solution import (
    calculate_distance,
    calculate_force,
    calculate_net_force_on,
    calculate_acceleration,
    update_velocity,
    update,
    G,
)


def test_calculate_distance():
    body1 = (1, (0, 0), (0, 0))
    body2 = (1, (1, 0), (0, 0))
    assert calculate_distance(body1, body2) == 1

    body3 = (1, (0, 0), (0, 0))
    assert calculate_distance(body1, body3) == 0

    body4 = (1, (1, 1), (0, 0))
    assert calculate_distance(body1, body4) == 2**0.5

    body5 = (1, (3, 4), (0, 0))
    assert calculate_distance(body1, body5) == 5.0


def test_calculate_force():
    body1 = (1, (0, 0), (0, 0))
    body2 = (1, (1, 0), (0, 0))

    target = (G, 0)
    actual = calculate_force(body1, body2)

    assert abs(actual[0] - target[0]) <= 1e-3 * abs(target[0])
    assert abs(actual[1] - target[1]) <= 1e-3 * abs(target[1])


def test_calculate_net_force_on():
    body1 = (1, (0, 0), (0, 0))
    body2 = (1, (1, 0), (0, 0))
    body3 = (1, (2, 0), (0, 0))

    system = [body1, body2, body3]

    target = (1.25 * G, 0)
    actual = calculate_net_force_on(body1, system)

    assert abs(actual[0] - target[0]) <= 1e-3 * abs(target[0])
    assert abs(actual[1] - target[1]) <= 1e-3 * abs(target[1])


def test_calculate_acceleration():
    body1 = (2, (0, 0), (0, 0))
    body2 = (1, (1, 0), (0, 0))
    body3 = (1, (2, 0), (0, 0))

    system = [body1, body2, body3]

    target = (1.25 * G, 0)
    actual = calculate_acceleration(body1, system)

    assert abs(actual[0] - target[0]) <= 1e-3 * abs(target[0])
    assert abs(actual[1] - target[1]) <= 1e-3 * abs(target[1])


def test_update_velocity():
    body1 = (2, (0, 0), (0, 0))
    body2 = (1, (1, 0), (0, 0))
    body3 = (1, (2, 0), (0, 0))

    original_system = deepcopy([body1, body2, body3])
    system = deepcopy([body1, body2, body3])

    target = [
        (2, (0, 0), (1.25 * G, 0)),
        (1, (1, 0), (-1 * G, 0)),
        (1, (2, 0), (-1.5 * G, 0)),
    ]
    actual = update_velocity(system, 1)

    for i in range(len(original_system)):
        for j in range(1, 3):
            for k in range(2):
                assert abs(actual[i][j][k] - target[i][j][k]) <= 1e-3 * abs(
                    target[i][j][k] - original_system[i][j][k]
                )


def test_update():
    body1 = (2, (0, 0), (0, 0))
    body2 = (1, (1, 0), (0, 0))
    body3 = (1, (2, 0), (0, 0))

    original_system = deepcopy([body1, body2, body3])
    system = deepcopy([body1, body2, body3])

    target = [
        (2, (1.25 * G, 0), (1.25 * G, 0)),
        (1, (1 - 1 * G, 0), (-1 * G, 0)),
        (1, (2 - 1.5 * G, 0), (-1.5 * G, 0)),
    ]
    actual = update(system, 1)

    for i in range(len(original_system)):
        for j in range(1, 3):
            for k in range(2):
                assert abs(actual[i][j][k] - target[i][j][k]) <= 1e-3 * abs(
                    target[i][j][k] - original_system[i][j][k]
                )


def test_simulation():
    body1 = (2, (0, 0), (2, 0))
    body2 = (1, (1, 0), (0, 3))
    body3 = (1, (2, 0), (1, 1))

    original_system = deepcopy([body1, body2, body3])
    system = deepcopy([body1, body2, body3])

    target = [
        (2, (2.000000000083426, 0.0), (2.000000000083426, 0.0)),
        (1, (0.9999999999332592, 3.0), (-6.67408e-11, 3.0)),
        (1, (2.999999999899889, 1.0), (0.9999999998998887, 1.0)),
    ]

    actual = update(system, 1)

    for i in range(len(original_system)):
        for j in range(1, 3):
            for k in range(2):
                assert abs(actual[i][j][k] - target[i][j][k]) <= 1e-3 * abs(
                    target[i][j][k] - original_system[i][j][k]
                )
