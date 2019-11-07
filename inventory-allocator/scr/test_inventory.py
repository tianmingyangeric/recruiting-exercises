import unittest
from inventory import InventoryAllocator


class TestInventory(unittest.TestCase):
	""" 
	Unittest invertory.py InvertoryAllocatoe class

	"""

	def test_happy_case(self):
		""" happy case, exact inventory match"""
		expeted_res = [{'owd': {'apple': 1}}]  # expected result for the program
		IA = InventoryAllocator({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 1}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)   # check if real output sane as expected

	def test_no_allocation(self):
		""" Not enough inventory"""
		expeted_res = []
		IA = InventoryAllocator({'apple': 1}, [{'name': 'owd', 'inventory': {'apple': 0}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_across_warehouse(self):
		"""Should split an item across warehouses if that is the only way to completely ship an item"""
		expeted_res = [{'owd': {'apple': 5}}, {'dm': {'apple': 5}}]
		IA = InventoryAllocator({'apple': 10}, [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_multi_warehouse(self):
		""" Should split an item across warehouses, test more order items"""
		expeted_res = [{'owd': {'apple': 5, 'orange': 5}}, {'dm': {'banana': 5}}]
		IA = InventoryAllocator({'apple': 5, 'banana': 5, 'orange': 5}, [{'name': 'owd', 'inventory': {'apple': 5, 'orange': 10}}, {'name': 'dm', 'inventory': {'banana': 5, 'orange': 10}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_zero_order(self):
		""" when there is an order, however, the order amont is 0"""
		expeted_res = []
		IA = InventoryAllocator({'apple': 0}, [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_no_order(self):
		""" when there is no order"""
		expeted_res = []
		IA = InventoryAllocator({}, [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dm', 'inventory': {'apple': 5}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_no_warehouse(self):
		""" when the wearhouse is empty"""
		expeted_res = []
		IA = InventoryAllocator({'apple': 1}, [])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_empty_inventory(self):
		""" when wearhouse exist but no inventory in that wearhouse"""
		expeted_res = []
		IA = InventoryAllocator({'apple': 1}, [{'name': 'owd', 'inventory': {}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_no_inventory(self):
		""" when inventory key is missing"""
		expeted_res = []
		IA = InventoryAllocator({'apple': 1}, [{'name': 'owd'}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_empty_name(self):
		""" when warehouse name is missing"""
		expeted_res = [{'': {'apple': 1}}]
		IA = InventoryAllocator({'apple': 1}, [{'name': '', 'inventory': {'apple': 5}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_no_name(self):
		""" when name key is missing"""
		expeted_res = [{'Unknow Name': {'apple': 1}}]
		IA = InventoryAllocator({'apple': 1}, [{'inventory': {'apple': 5}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_no_inputs(self):
		""" both order and wearhouse is empty"""
		expeted_res = []
		IA = InventoryAllocator({}, [])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_negtive_value(self):
		expeted_res = []
		IA = InventoryAllocator({'apple': -1}, [{'inventory': {'apple': 5}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_one_not_enough(self):
		""" the inventory is enough for one item but another is not enough"""
		expeted_res = []
		IA = InventoryAllocator({'apple': 5, 'orange': 2}, [{'name': 'owd', 'inventory': {'apple': 0, 'orange': 3}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_multi_empty(self):
		""" when there are several empty warehouse"""
		expeted_res = []
		IA = InventoryAllocator({'apple': 5}, [{}, {}, {}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)

	def test_no_order_item(self):
		""" the order item is not in wearhouse"""
		expeted_res = []
		IA = InventoryAllocator({'apple': 1}, [{'inventory': {'orange': 5}}])
		real_res = IA.allocator()
		self.assertEqual(expeted_res, real_res)


if __name__ == '__main__':
	unittest.main()