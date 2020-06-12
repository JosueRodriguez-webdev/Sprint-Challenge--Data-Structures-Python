import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Return the list of duplicates in this data structure
duplicates = []
# dupName for dupName in names_1 if dupName in names_2

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.duplicates = 0

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        if target > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        # check if target is greater than root, then:
        # if target == self.value, then return true
        # else recursion self.right.contain(target)

        # check if target is less than root, then:
        # if target == self.value, then return true
        # else recursion self.left.contain(target)

        # check if self.value == none, then return false

        # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def for_each(self, value):
        if value == self.value:
            return value
        if self.left:
            self.left.for_each(value)
        if self.right:
            self.right.for_each(value)
        if self.right or self.left is None:
            return


middle = BSTNode("M")

for name in names_1:
    middle.insert(name)

for name in names_2:
    if middle.contains(name):
        duplicates.append(name)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
