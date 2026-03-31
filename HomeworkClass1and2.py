from SinglyLinkedList import SinglyLinkedList
import random
"""
Homework placeholder for class assignments 1 and 2.

Use this file for homework driver code, assignment examples, or small
tests related to linked list work from the first two class homework sets.
"""



def HomeworkDriver():
    random.seed(1)
    TestingList= SinglyLinkedList()
    for i in range(1,4):
        TestingList.add_first(i * random.randint(0,10))
        TestingList.add_last(i * random.randint(0,10))
        TestingList.add_first(i * random.randint(0,10))
        TestingList.add_last(i * random.randint(0,10))
    print(TestingList.verify())
    # print(TestingList)
    for _ in range(5):
        rand_index=random.randint(0,20)
        # print(f'rand_index is {rand_index}')
        try: TestingList.remove_at_index(rand_index)
        except IndexError as e:
            pass
            print(e)
    print(TestingList)
HomeworkDriver()


