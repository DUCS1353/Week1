"""
Starter code for Doubly Linked List lab and homework work.

Suggested instance attributes:
    self.head
    self.tail
    self.size

This starter includes a common set of list methods so students can fill
in the implementation details later. The __str__ method is intended as a
lab task, and search(value) is included as a later method that returns
the index of the first matching value or -1 if not found.
"""


class Node:
    """A single node in a doubly linked list."""

    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()


class DoublyLinkedList:
    """A doubly linked list that stores values in Node objects."""

    def __init__(self):
        """
        Create an empty doubly linked list.

        TODO:
        - Set head to None.
        - Set tail to None.
        - Set size to 0.
        """
        self.header = Node(None,None,None)
        self.trailer = Node(None,None,self.header)
        self.header.next=self.trailer
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

        TODO:
        - Use self.size, self.head, or both to determine whether the list
          is empty.
        """
        return self.size==0

    def __str__(self):
        """
        LAB TASK:
        Implement __str__ for the DoublyLinkedList class.

        Return a string showing all values in the list from first to last.

        Example format:
            [2 4 6]

        Returns:
            str: A string representation of the list contents.

        TODO:
        - This method is intended to be completed during lab.
        - Traverse from self.head to the end of the list.
        - Collect each node's value as a string.
        - Return the values inside square brackets.
        - Separate the values with spaces or commas.
        """
        string_rep='['
        curr=self.header.next
        while curr is not self.trailer:
            if curr.next is not self.trailer:
                string_rep=string_rep+str(curr.value)+str(',')
            else:
                string_rep=string_rep+str(curr.value)
        string_rep=string_rep+']'
        return 

    def add_first(self, value):
        """
        Insert a new node containing value at the front of the list.

        Args:
            value: The value to store in the new first node.

        Returns:
            None

        TODO:
        - Create a new Node.
        - If the list is empty, update both head and tail.
        - Otherwise, link the new node before the current head.
        - Increase self.size by 1.
        """
        temp=Node(value,self.header,self.header.next)
        temp.prev.next=temp
        temp.next.prev=temp
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
        - If the list is empty, update both head and tail.
        - Otherwise, link the new node after the current tail.
        - Increase self.size by 1.
        """
        raise NotImplementedError("TODO: implement add_last")

    def remove_first(self):
        """
        LAB TASK:
        Implement remove_first for the DoublyLinkedList class.

        Remove the first node from the list and return its value.

        Returns:
            The value stored in the removed first node.

        Raises:
            IndexError: If the list is empty.

        TODO:
        - This method is intended to be completed during lab.
        - If your class later includes a helper like remove_between,
          this method may be only one line of code.
        - Check for the empty-list case.
        - Save the value at the head.
        - Update head to the next node.
        - Fix prev/next references as needed.
        - Update tail too if the list becomes empty.
        - Decrease self.size by 1 and return the saved value.
        """
        raise NotImplementedError("TODO: implement remove_first")

    def remove_last(self):
        """
        LAB TASK:
        Implement remove_last for the DoublyLinkedList class.

        Remove the last node from the list and return its value.

        Returns:
            The value stored in the removed last node.

        Raises:
            IndexError: If the list is empty.

        TODO:
        - This method is intended to be completed during lab.
        - If your class later includes a helper like remove_between,
          this method may be only one line of code.
        - Check for the empty-list case.
        - Save the value at the tail.
        - Update tail to the previous node.
        - Fix prev/next references as needed.
        - Update head too if the list becomes empty.
        - Decrease self.size by 1 and return the saved value.
        """
        raise NotImplementedError("TODO: implement remove_last")

    def get(self, index: int):
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
        if index<0 or index> self.size-1:
            raise IndexError
        curr=self.header.next
        for _ in range(index):
            curr=curr.next

        return curr.value

    def remove_at_index(self, index: int):
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
        - If index is self.size - 1, remove the last node.
        - Otherwise, traverse to the target node.
        - Re-link the previous and next nodes around it.
        - Decrease self.size and return the removed value.
        """
        raise NotImplementedError("TODO: implement remove_at_index")

    def search(self, value):
        """
        Return the index of the first occurrence of value in the list.

        Args:
            value: The value to search for.

        Returns:
            int: The index of the first matching node, or -1 if the value
            does not appear in the list.

        TODO:
        - Start at self.head.
        - Walk through the list one node at a time while tracking the
          current index.
        - If a node's value matches value, return that index immediately.
        - If the loop finishes without a match, return -1.
        """
        raise NotImplementedError("TODO: implement search")
