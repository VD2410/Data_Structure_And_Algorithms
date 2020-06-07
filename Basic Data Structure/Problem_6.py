class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here

    listUnion = LinkedList()

    node = llist_2.head

    nextNode = llist_1.head

    listUnion.append(nextNode.value)

    while nextNode.next:
        nextNode = nextNode.next
        listUnion.append(nextNode.value)

    listUnion.append(node.value)

    while node.next:
        node = node.next
        listUnion.append(node.value)


    return listUnion

def intersection(llist_1, llist_2):
    # Your Solution Here

    listInter = LinkedList()

    list_set = set()

    node = llist_2.head

    nextNode = llist_1.head

    # listInter.append(nextNode.value)

    while nextNode:

        while node:

            if nextNode.value==node.value:
                list_set.add(nextNode.value)
            node = node.next

        node=llist_2.head
        nextNode=nextNode.next


    for value in list_set:
        listInter.append(value)



            


    return listInter


# Test case 1

print("-----------------------------Test 1-------------------------------------")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print("List1 ", element_1)
print("List2 ", element_2)
print ("Union ",union(linked_list_1,linked_list_2))
print ("Intersection ",intersection(linked_list_1,linked_list_2))

# Test case 2


print("-----------------------------Test 2-------------------------------------")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print("List1 ", element_1)
print("List2 ", element_2)
print ("Union ",union(linked_list_3,linked_list_4))
print ("Intersection ",intersection(linked_list_3,linked_list_4))


# Test case 3


print("-----------------------------Test 3-------------------------------------")

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = [1, 2, 3]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print("List1 ", element_1)
print("List2 ", element_2)
print ("Union ",union(linked_list_5,linked_list_6))
print ("Intersection ",intersection(linked_list_5,linked_list_6))


# Test case 4


print("-----------------------------Test 4-------------------------------------")

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("List1 ", element_1)
print("List2 ", element_2)
print ("Union ",union(linked_list_7,linked_list_8))
print ("Intersection ",intersection(linked_list_7,linked_list_8))


print("-----------------------------Test 1-------------------------------------")