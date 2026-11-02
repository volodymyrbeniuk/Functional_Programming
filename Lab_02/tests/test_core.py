import pytest
from lab import (
    average_score,
    compose,
    honor_roll,
    juxt,
    normalize_record,
    pipe,
    select,
    transform,
)


def test_higher_order_transformations() -> None:
    assert transform([1, 2, 3], lambda value: value * 2) == [2, 4, 6]
    assert select([1, 2, 3, 4], lambda value: value % 2 == 0) == [2, 4]


def test_compose_is_right_to_left_and_pipe_is_left_to_right() -> None:
    double = lambda value: value * 2
    increment = lambda value: value + 1

    assert compose(increment, double)(10) == 21
    assert pipe(10, double, increment) == 21
    assert compose()(10) == 10
    assert pipe(10) == 10


def test_juxt_applies_all_functions_to_same_input() -> None:
    describe = juxt(len, min, max)

    assert describe([3, 1, 4]) == (3, 1, 4)


def test_record_pipeline_and_purity() -> None:
    records = [
        {"name": " Ada ", "score": 95},
        {"name": "Grace", "score": 80},
    ]

    assert honor_roll(records) == [{"name": "Ada", "score": 95.0}]
    assert records[0] == {"name": " Ada ", "score": 95}
    assert normalize_record(records[0]) == {"name": "Ada", "score": 95.0}


def test_average_score_handles_empty_and_nonempty_inputs() -> None:
    assert (
        average_score([{"name": "A", "score": 90}, {"name": "B", "score": 80}]) == 85.0
    )
    assert average_score([]) == 0.0


def test_invalid_threshold_is_rejected() -> None:
    with pytest.raises(ValueError, match="between 0 and 100"):
        honor_roll([], threshold=101)
