
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


def test_aggregate_data():
    ...


def test_save_report():
    ...

