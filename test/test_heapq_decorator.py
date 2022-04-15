from unittest import TestCase
import heapq_decorator as hd


class TestHeapqDecorator(TestCase):
    test_priority_queue = hd.HeapqDecorator()
    test_priority_queue.push(5, "ziemniaki")
    test_priority_queue.push(1, "kotlety")
    test_priority_queue.push(1, "buraczki")
    test_priority_queue.push(7, "surowka")
    test_priority_queue.push(2, "salatka")

    def test_push_pop_len(self):
        new_priority_queue = hd.HeapqDecorator()
        self.assertEqual(0, len(new_priority_queue))
        new_priority_queue.push(5, "kotlety")
        self.assertEqual(1, len(new_priority_queue))
        new_priority_queue.push(2, "buraczki")
        self.assertEqual(2, len(new_priority_queue))
        new_priority_queue.push(3, "ziemniaki")
        self.assertEqual(3, len(new_priority_queue))

        self.assertEqual("buraczki", new_priority_queue.pop())
        self.assertEqual("ziemniaki", new_priority_queue.pop())
        self.assertEqual("kotlety", new_priority_queue.pop())

    def test_contains(self):
        self.assertEqual(True, self.test_priority_queue.contains("kotlety"))
        self.assertEqual(False, self.test_priority_queue.contains("spagetti"))

    def test_priority(self):
        self.assertEqual(7, self.test_priority_queue.priority("surowka"))
        self.assertEqual(2, self.test_priority_queue.priority("salatka"))
        self.assertRaises(hd.ObjectNotFoundException, self.test_priority_queue.priority, "makaron")

    def test_update(self):
        self.assertNotEqual(0, self.test_priority_queue.priority("surowka"))
        self.test_priority_queue.update(0, "surowka")
        self.assertEqual(0, self.test_priority_queue.priority("surowka"))
        self.assertEqual("surowka", self.test_priority_queue.pop())

    def test__getitem__(self):
        self.assertEqual(["surowka"], self.test_priority_queue[7])
        self.assertEqual([], self.test_priority_queue[69])