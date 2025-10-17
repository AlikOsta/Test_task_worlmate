
import os
import csv
import pytest

from read_csv import read_csv
from aggregate_data import aggregate_data
from save_report import save_report


@pytest.mark.parametrize(
    "link_list, expected_count",
    [
        (["test_data/products1.csv", "test_data/products2.csv"], 10),  
        (["test_data/products1", "test_data/products2"], 10),         
        (["test1.csv", "test2"], 0),               
        ([""], 0),                                
        ([], 0),                                 
    ]
)
def test_read_csv(link_list, expected_count):
    """Проверяем на чтение файлов"""
    result = read_csv(link_list)

    assert isinstance(result, list)
    assert len(result) == expected_count



@pytest.mark.parametrize(
    "data, expected",
    [
        ([], []),
        (
            [
                {"brand": "samsung", "rating": 4.0},
                {"brand": "samsung", "rating": 5.0},
            ],
            [
                {"brand": "samsung", "rating": 4.5}
            ],
        ),
        (
            [
                {"brand": "samsung", "rating": 4.0},
                {"brand": "apple", "rating": 3.0},
                {"brand": "apple", "rating": 5.0},
            ],
            [
                {"brand": "samsung", "rating": 4.0},
                {"brand": "apple", "rating": 4.0},
            ],
        ),
        (
            [
                {"brand": "lg", "rating": None},
                {"brand": "lg", "rating": "4"},
                {"brand": "lg", "rating": 4.0},
            ],
            [
                {"brand": "lg", "rating": 4.0}
            ],
        ),
        (
            [
                {"brand": "sony", "rating": None}
            ],
            [
                {"brand": "sony", "rating": 0}
            ],
        ),
    ]
)
def test_aggregate_data(data, expected):
    result = aggregate_data(data)

    assert isinstance(result, list)
    assert len(result) == len(expected)

    for r, e in zip(result, expected):
        assert r["brand"] == e["brand"]
        assert r["rating"] == pytest.approx(e["rating"], rel=1e-2)



