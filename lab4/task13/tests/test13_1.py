import unittest
from lab4.task13.src.task13_1 import Stack
import datetime
import time
from time import perf_counter
task_numb = "13_1"

class TestStack(unittest.TestCase):
    start_time = datetime.datetime.now()
    print(f"Lab4 task{task_numb} test")
    def setUp(self):
        self.stack = Stack()

    def test_is_empty_on_init(self):
        self.assertTrue(self.stack.isEmpty())

    def test_push_and_is_empty(self):
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())

    def test_push_multiple_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.assertFalse(self.stack.isEmpty())

    def test_pop_single_element(self):
        self.stack.push(1)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 1)
        self.assertTrue(self.stack.isEmpty())

    def test_pop_multiple_elements(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 3)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 2)
        popped_value = self.stack.pop()
        self.assertEqual(popped_value, 1)
        self.assertTrue(self.stack.isEmpty())

    finish_time = datetime.datetime.now()
    result_time = finish_time - start_time
    print("Итоговое время тестов:", result_time)

if __name__ == "__main__":
    start = time.perf_counter()
    unittest.main()
    time = float(time.perf_counter() - start)
    print(time)