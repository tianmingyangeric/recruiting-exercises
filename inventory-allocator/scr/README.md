The src folder contains Inventory.py that install InventoryAllocation class.

You can run it with python3 inventory.py in command line.

    python3 inventory.py
  
The output will looks like:

    Order List: {'apple': 1}
    Wearhouse List: [{'name': 'owd', 'inventory': {'apple': 1}}]
    Result: [{'owd': {'apple': 1}}]

invertory_config.py has configures for order list and wearhouse, you can manually test the class by editing the configure.

	order_map = {'apple': 1}
	warehouse_list = [{'name': 'owd', 'inventory': {'apple': 1}}]
  
replace the value and run python3 inventory.py will test the code.

    python3 inventory.py

test_inventory.py has all unit test, you can run it in command line with python3 -m unittest test_inventory.py
the output will be:

    Ran 16 tests in 0.001s
    OK
