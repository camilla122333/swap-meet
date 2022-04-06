#from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):
        if not inventory:
           inventory = []
        self.inventory = inventory

    def add(self, item):
        if not item:
            return False

        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        list_of_items_per_cat = []  # do i need .self? i do not.

        for item in self.inventory:
            if item.category == category:
               list_of_items_per_cat.append(item)

        return list_of_items_per_cat

    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        '''
        order does not matter
        self.inventory.remove or other_vendor.remove does not matter
        self.other_vendor / self.my_item, etc. does not matter
        '''
        other_vendor.add(my_item)
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):

        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        self.add(other_vendor.inventory[0])
        other_vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        other_vendor.remove(other_vendor.inventory[0])

        return True

    def get_best_by_category(self, category):
        if category not in self.inventory:
            return None

    def swap_best_by_category(self):
        pass


rafferty = Vendor()
closet_items = ["white shirt", "balenciaga jeans", "flat shoes", "work gown"]
rafferty.inventory = closet_items
print(vars(rafferty))
rafferty.add("elegant work gown")
rafferty.remove("flat shoes")
print(vars(rafferty))

'''
Notes and Questions:


# inventory = ["ball", "jeans" "shirt"]
# # inventory = ["clothing", "decor", "electronics"] #<--
# inventory[0] = ["jeans", "shirt"]


# print(Vendor.get_by_category("instruments"))

# questions

'''
