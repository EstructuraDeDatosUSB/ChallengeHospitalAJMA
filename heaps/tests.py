from django.test import TestCase
import unittest
import pytest
from scripts.maxHeap import MaxHeap

class HeapTestCase(unittest.TestCase):
    def setUp(self):
        self.patientsMaxHeap = MaxHeap()

        self.patientsMaxHeap.insert({
            'name': 'John',
            'id': "1",
            'priority': "1",
            'case': 'fever'
        })

        self.patientsMaxHeap.insert({
            'name': 'Jane',
            'id': "2",
            'priority': "2",
            'case': 'fever'
        })

        self.patientsMaxHeap.insert({
            'name': 'Mary',
            'id': "3",
            'priority': "3",
            'case': 'fever'
        })

        self.patientsMaxHeap.insert({
            'name': 'Peter',
            'id': "4",
            'priority': "4",
            'case': 'fever'
        })

        self.patientsMaxHeap.insert({
            'name': 'Harry',
            'id': "5",
            'priority': "5",
            'case': 'fever'
        })

    def test_insert(self):
        self.assertEqual(self.patientsMaxHeap.root.value['priority'], '5')
        self.assertEqual(self.patientsMaxHeap.root.left.value['priority'], '4')
        self.assertEqual(self.patientsMaxHeap.root.right.value['priority'], '2')
        self.assertEqual(self.patientsMaxHeap.root.left.left.value['priority'], '1')
        self.assertEqual(self.patientsMaxHeap.root.left.right.value['priority'], '3')

    def test_delete(self):
        self.patientsMaxHeap.delete()
        self.assertEqual(self.patientsMaxHeap.root.value['priority'], '4')
        self.assertEqual(self.patientsMaxHeap.root.right.value['priority'], '2')
        self.assertEqual(self.patientsMaxHeap.root.left.value['priority'], '3')
        self.assertEqual(self.patientsMaxHeap.root.left.left.value['priority'], '1')

    def test_delete_specific(self):
        self.patientsMaxHeap.delete_specific('2')
        self.assertEqual(self.patientsMaxHeap.root.value['priority'], '5')
        self.assertEqual(self.patientsMaxHeap.root.left.value['priority'], '4')
        self.assertEqual(self.patientsMaxHeap.root.right.value['priority'], '3')
        self.assertEqual(self.patientsMaxHeap.root.left.left.value['priority'], '1')

    def test_find(self):
        self.assertEqual(self.patientsMaxHeap.get_node('2')['priority'], '2')
        self.assertEqual(self.patientsMaxHeap.get_node('3')['priority'], '3')
        self.assertEqual(self.patientsMaxHeap.get_node('4')['priority'], '4')
        self.assertEqual(self.patientsMaxHeap.get_node('5')['priority'], '5')
        self.assertEqual(self.patientsMaxHeap.get_node('1')['priority'], '1')





