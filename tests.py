#Задача 1.1
def is_number_in_ranges(num):
    if not isinstance(num, (int, float)):
        raise TypeError("input is not a number")
    if 0 <= num < 10:
        return "0 <= num < 10"
    elif 10 <= num < 20:
        return "10 <= num < 20"
    elif 20 <= num < 30:
        return "20 <= num < 30"
    else:
        return "num >= 30"


import unittest


class TestIsNumberInRanges(unittest.TestCase):

    def test_in_range_1(self):
        self.assertEqual(is_number_in_ranges(5), "0 <= num < 10")

    def test_in_range_2(self):
        self.assertEqual(is_number_in_ranges(15), "10 <= num < 20")

    def test_in_range_3(self):
        self.assertEqual(is_number_in_ranges(25), "20 <= num < 30")

    def test_out_of_range(self):
        self.assertEqual(is_number_in_ranges(35), "num >= 30")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_number_in_ranges("string")


if __name__ == '__main__':
    unittest.main()

#Задача 1.2
def calculate_boiling_time(start_temperature: int) -> int:
    time = 0
    temperature = start_temperature
    while temperature < 100:
        temperature += 1
        time += 2
    return time

import unittest

class TestCalculateBoilingTime(unittest.TestCase):
    def test_boiling_time(self):
        self.assertEqual(calculate_boiling_time(20), 160)
        self.assertEqual(calculate_boiling_time(30), 140)
        self.assertEqual(calculate_boiling_time(50), 100)
        self.assertEqual(calculate_boiling_time(70), 60)
        self.assertEqual(calculate_boiling_time(90), 20)

if __name__ == '__main__':
    unittest.main()

#Задача 2.1
import unittest

def will_box_fit(x, y, z, a, b):
    sides = [x, y, z]
    sides.sort()
    hole = [a, b]
    hole.sort()
    if sides[0] <= hole[0] and sides[1] <= hole[1]:
        return True
    else:
        return False

class TestWillBoxFit(unittest.TestCase):
    def test_will_fit(self):
        self.assertTrue(will_box_fit(1, 1, 1, 1, 1))
        self.assertTrue(will_box_fit(1, 2, 3, 3, 2))
        self.assertFalse(will_box_fit(5, 6, 7, 3, 4))

if __name__ == '__main__':
    unittest.main()

#Задача 3.1 Tests
def can_buy_ice_cream(K):
    """
    Проверяет, можно ли купить ровно K шариков мороженого (в кафе продают по 3 шарика мороженного и по 5).
    Возвращает строку "да", если можно, иначе - "нет".
    """
    if K is None:
        return "нет"
    try:
        K = int(K)
    except ValueError:
        return "нет"
    if K % 3 == 0 or K % 5 == 0 or K % 8 == 0:
        return "да"
    else:
        return "нет"

def run_task_3_1():
    try:
        with open('input.txt', 'r') as f:
            K = int(f.readline())
    except ValueError:
        print("Неверный формат входных данных.")
        return

    result = can_buy_ice_cream(K)

    with open('output.txt', 'a') as out_file:
        out_file.write("Задача 3.1:\n " + result + "\n")

    print(result)


import unittest
from io import StringIO
from unittest.mock import patch

class TestCanBuyIceCream(unittest.TestCase):

    def test_can_buy_ice_cream_positive(self):
        self.assertEqual(can_buy_ice_cream(3), "да")
        self.assertEqual(can_buy_ice_cream(5), "да")
        self.assertEqual(can_buy_ice_cream(8), "да")
        self.assertEqual(can_buy_ice_cream(9), "да")
        self.assertEqual(can_buy_ice_cream(10), "да")
        self.assertEqual(can_buy_ice_cream(15), "да")

    def test_can_buy_ice_cream_negative(self):
        self.assertEqual(can_buy_ice_cream(1), "нет")
        self.assertEqual(can_buy_ice_cream(2), "нет")
        self.assertEqual(can_buy_ice_cream(4), "нет")
        self.assertEqual(can_buy_ice_cream(7), "нет")
        self.assertEqual(can_buy_ice_cream(11), "нет")
        self.assertEqual(can_buy_ice_cream(13), "нет")

    def test_can_buy_ice_cream_invalid_input(self):
        self.assertEqual(can_buy_ice_cream("abc"), "нет")
        self.assertEqual(can_buy_ice_cream(None), "нет")

    @patch('sys.stdout', new_callable=StringIO)
    def test_run_task_3_1_positive(self, mock_stdout):
        with patch('builtins.open', side_effect=[StringIO("3\n"), StringIO()]) as mock_open:
            run_task_3_1()
            mock_open.assert_called_with('output.txt', 'a')
            self.assertEqual(mock_stdout.getvalue(), "да\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_run_task_3_1_negative(self, mock_stdout):
        with patch('builtins.open', side_effect=[StringIO("4\n"), StringIO()]) as mock_open:
            run_task_3_1()
            mock_open.assert_called_with('output.txt', 'a')








