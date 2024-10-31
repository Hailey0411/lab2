import pytest
from Lab2 import calc_average, calc_min_max_temperature, calculate_median_temp

def test_calc_average():
    num_list = [10, 20, 30, 40, 50]
    assert calc_average(num_list) == 30

def test_calc_min_max_temperature():
    num_list = [10, 20, 30, 40, 50]
    assert calc_min_max_temperature(num_list) == [10, 50]

def test_calculate_median_temp():
    num_list = [10, 20, 30, 40, 50]
    assert calculate_median_temp(num_list) == 30

    num_list_even = [10, 20, 30, 40]
    assert calculate_median_temp(num_list_even) == 25  # Median of even count

if __name__ == "__main__":
    pytest.main()
