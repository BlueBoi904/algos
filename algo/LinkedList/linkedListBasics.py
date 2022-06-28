import math


class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def get_head(self):
        return self.head_node.data

    def insert_at_head(self, data):
        # Create a new node containing your specified value
        temp_node = Node(data)
        # The new node points to the same node as the head
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False
    # Supplementary print function

    def insert_at_tail(self, lst, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if lst.get_head() is None:
            lst.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = lst.get_head()

        while temp.next_element:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node

    def search(self, lst, value):

        # Start from first element
        current_node = lst.get_head()

        # Traverse the list till you reach end
        while current_node:
            if current_node.data == value:
                return True  # value found
            current_node = current_node.next_element

        return False  # value not found

    def delete(self, lst, value):
        current_node = lst.get_head()
        prev_node = None

        while current_node:
            if current_node.data == value:
                prev_node.next_element = current_node.next_element
                return True  # value deleted
            prev_node = current_node
            current_node = current_node.next_element
        return False

    def length(self, lst):
        current_node = lst.get_head()
        length = 0
        if current_node is None:
            return length

        # Traverse the list till you reach end
        while current_node:
            current_node = current_node.next_element
            length += 1

        return length  # value not found

    def reverse(self, lst):
        # To reverse linked, we need to keep track of three things
        previous = None  # Maintain track of the previous node
        current = lst.get_head()  # The current node
        next = None  # The next node in the list

        # Reversal
        while current:
            next = current.next_element
            current.next_element = previous
            previous = current
            current = next

            # Set the last element as the new head node
            lst.head_node = previous
        return lst

    def detect_loop(self, lst):
        hashMap = {}
        # Start from first element
        current_node = lst.get_head()

        # Traverse the list till you reach end
        while current_node:
            if current_node in hashMap:
                return True  # value found
            else:
                hashMap[current_node] = True
            current_node = current_node.next_element

        return False  # value not found

    def detect_loop_step_algo(self, lst):
        # Keep two iterators
        onestep = lst.get_head()
        twostep = lst.get_head()
        while onestep and twostep and twostep.next_element:
            onestep = onestep.next_element  # Moves one node at a time
            twostep = twostep.next_element.next_element  # Skips a node
            if onestep == twostep:  # Loop exists
                return True
        return False

    def find_mid(self, lst):
        if lst.is_empty():
            return None

        node = lst.get_head()
        mid = 0
        if lst.length() % 2 == 0:
            mid = lst.length()//2
        else:
            mid = lst.length()//2 + 1

        for i in range(mid - 1):
            node = node.next_element

        return node.data

    def remove_duplicates(lst):
        current_node = lst.get_head()
        prev_node = lst.get_head()
        # To store values of nodes which we already visited
        visited_nodes = set()
        # If List is not empty and there is more than 1 element in List
        if not lst.is_empty() and current_node.next_element:
            while current_node:
                value = current_node.data
                if value in visited_nodes:
                    # current_node is already in the HashSet
                    # connect prev_node with current_node's next element
                    # to remove it
                    prev_node.next_element = current_node.next_element
                    current_node = current_node.next_element
                    continue
                # Visiting currentNode for first time
                visited_nodes.add(current_node.data)
                prev_node = current_node
                current_node = current_node.next_element

    def find_nth(lst, n):
        length = lst.length()
        target = length - n
        curr_length = 0
        current = lst.get_head()
        while current:
            if curr_length == target:
                return current.data
            curr_length += 1
            current = current.next_element
        return -1

    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True


# Recursive search solution

def search(node, value):

    # Base case
    if(not node):
        return False  # value not found

    # check if the node's data matches our value
    if(node.data is value):
        return True  # value found

    # Recursive call to next node in the list
    return search(node.next_element, value)


newNode = Node(1)

lst = LinkedList(newNode)  # Linked List created
# Returns None since headNode does not contain any data
print(lst.get_head())
lst.insert_at_head(2)
print(lst.get_head())
