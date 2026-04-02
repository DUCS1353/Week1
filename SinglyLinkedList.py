"""
Starter code for a Singly Linked List homework assignment.

Required instance attributes:
    self.head
    self.size

Required methods:
    __init__(self)
    get_size(self)
    is_empty(self)
    __str__(self)
    add_first(self, value)
    add_last(self, value)
    remove_first(self)
    remove_last(self)
    get(self, index)
    remove_at_index(self, index)
"""


class Node:
    """A single node in a singly linked list."""

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class SinglyLinkedList:
    """A singly linked list that stores values in Node objects."""

    def __init__(self):
        """
        Create an empty singly linked list.

        TODO:
        - Set head to None because the list starts empty.
        - Set size to 0 because there are no nodes yet.
        """
        self.head = None
        self.size = 0

    def get_size(self):
        """
        Return the number of nodes currently in the list.

        Returns:
            int: The current size of the list.
        """
        return self.size

    def is_empty(self):
        """
        Return True if the list has no nodes, otherwise return False.

        Returns:
            bool: True when the list is empty, False otherwise.

        - Use either self.size or self.head to determine whether the list
          is empty.
        """
        return self.size==0

    def __str__(self):
        """
        Return a string showing all values in the list from first to last.

        Example format:
            [10 -> 20 -> 30]

        Returns:
            str: A string representation of the list contents.

        TODO:
        - Traverse from self.head to the end of the list.
        - Collect each node's value as a string.
        - Join the values into one readable result.
        """
        raise NotImplementedError("TODO: implement __str__")

    def add_first(self, value):
        """
        Insert a new node containing value at the front of the list.

        Args:
            value: The value to store in the new first node.

        Returns:
            None

        - Create a new Node.
        - Make the new node point to the current head.
        - Update self.head to the new node.
        - Increase self.size by 1.
        """
        temp=Node(value, self.head)
        self.head=temp
        self.size+=1

    def add_last(self, value):
        """
        Append a new node containing value to the end of the list.

        Args:
            value: The value to store in the new last node.

        Returns:
            None

        TODO:
        - Create a new Node.
        - If the list is empty, make it the head.
        - Otherwise, traverse to the last node and link the new node there.
        - Increase self.size by 1.
        """
        temp=Node(value)
        if self.head is None:
            self.head=temp
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=temp
        self.size+=1       

    def remove_first(self):
        """
        Remove the first node from the list and return its value.

        Returns:
            The value stored in the removed first node.

        Raises:
            IndexError: If the list is empty.

        TODO:
        - Check for the empty-list case.
        - Save the value from the current head.
        - Move self.head to the next node.
        - Decrease self.size by 1.
        - Return the saved value.
        """
        if self.size==0:
            raise IndexError
            return
        return_val=self.head.value
        self.head=self.head.next
        self.size-=1
        return return_val

    def remove_last(self):
        """
        Remove the last node from the list and return its value.

        Returns:
            The value stored in the removed last node.

        Raises:
            IndexError: If the list is empty.

        TODO:
        - Check for the empty-list case.
        - Handle the one-node case separately.
        - Otherwise, traverse to the second-to-last node.
        - Remove the last node, decrease self.size, and return its value.
        """
        raise NotImplementedError("TODO: implement remove_last")

    def get(self, index):
        """
        Return the value stored at the given index.

        Args:
            index (int): The position to retrieve.

        Returns:
            The value stored at the given index.

        Raises:
            IndexError: If index is out of bounds.

        TODO:
        - Validate that index is between 0 and self.size - 1.
        - Traverse to the node at that position.
        - Return that node's value.
        """
        raise NotImplementedError("TODO: implement get")

    def remove_at_index(self, index):
        """
        Remove the node at the given index and return its value.

        Args:
            index (int): The position of the node to remove.

        Returns:
            The value stored in the removed node.

        Raises:
            IndexError: If index is out of bounds.

        TODO:
        - Validate that index is between 0 and self.size - 1.
        - If index is 0, remove the first node.
        - Otherwise, traverse to the node just before index.
        - Bypass the target node, decrease self.size, and return its value.
        """
        raise NotImplementedError("TODO: implement remove_at_index")
