
import sys
from invertory_config import Config


class InventoryAllocator(object):
	def __init__(self, order, warehouse_list):
		""" inits InvertoryAllocator with order dict and warehouse list """
		self.order = order
		self.warehouse_list = warehouse_list

	def allocator(self):
		""" 
		allocate warehouse for orders
		returns:
		[] if the order can not be allocated
		res, if the order can be allocated. res will include warehouse name and order amount
		"""
		res = []
		order_list = [order_name for order_name in self.order if self.order[order_name] > 0]  # get all valid order items
		# check warehouse from beginning
		for warehouse in self.warehouse_list:
			del_list = []
			inventory_amount = {}
			for num in range(len(order_list)):
				warehouse.setdefault('inventory', {})
				if order_list[num] in warehouse['inventory']:
					# if inventory in warehouse is enough for order item, delete item in order_list and we do not check it in next warehouse
					if self.order[order_list[num]] <= warehouse['inventory'][order_list[num]]: 
						inventory_amount[order_list[num]] = self.order[order_list[num]]
						self.order[order_list[num]] = 0
						del_list.append(num)
					# if inventory in warehouse is not enough, append invetory and reduce the amount in order dict
					else:
						if warehouse['inventory'][order_list[num]] > 0:
							inventory_amount[order_list[num]] = warehouse['inventory'][order_list[num]]
							self.order[order_list[num]] -= warehouse['inventory'][order_list[num]]
			# check if warehouse has the item that ordered and append warehouse name and item to result
			if inventory_amount:
				warehouse.setdefault('name', 'Unknow Name')
				res.append({warehouse['name']: inventory_amount})
			# delete the order items that already satisfied
			del_list.reverse()
			for done_num in del_list:
				del order_list[done_num]
		# if order_list is not empty, some item do not have inventory in all warehouse
		if order_list:
			return []
		else:
			return res


if __name__ == '__main__':
	inv_config = Config()
	print('Order List : ', inv_config.order_map)
	print('Wearhouse List : ', inv_config.warehouse_list)
	IA = InventoryAllocator(inv_config.order_map, inv_config.warehouse_list)
	res = IA.allocator()
	print('Result : ', res)
