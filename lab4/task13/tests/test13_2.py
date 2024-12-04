import unittest
import datetime
import time
from time import perf_counter
from lab4.task13.src.task13_2 import Queue
task_numb = "13_2"

class TestQueue(unittest.TestCase):
    start_time = datetime.datetime.now()
    print(f"Lab4 task{task_numb} test")
    def setUp(self):
        self.queue = Queue(5)

    def test_is_empty_on_init(self):
        self.assertTrue(self.queue.isEmpty(), "очередь должна быть пустой")

    def test_enqueue_and_is_empty(self):
        self.queue.enqueue(10)
        self.assertFalse(self.queue.isEmpty(), "очередь не должна быть пустой ")

    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        dequeued_value = self.queue.dequeue()
        self.assertEqual(dequeued_value, 10, "элемент должен быть извлечен")
        self.assertEqual(self.queue.queue_size(), 1, "размер очереди должен быть 1")


    def test_peek(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.peek(), 10, "ошибка")
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 20, "ошибка")

    def test_size(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.queue_size(), 2, "ошибка")
        self.queue.dequeue()
        self.assertEqual(self.queue.queue_size(), 1, "ошибка")


    finish_time = datetime.datetime.now()
    result_time = finish_time - start_time
    print("Итоговое время тестов:", result_time)


if __name__ == "__main__":
    start = time.perf_counter()
    unittest.main()
    time = float(time.perf_counter() - start)
    print(time)
