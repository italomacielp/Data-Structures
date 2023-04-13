import pytest as pytest

from linkedlist import *


def removeDuplicatesFromLinkedList(self):
    linkedlist = self.head
    linkedlist_next = self.head
    qntd_por_numero = dict()
    numero = set()
    qntd = 0

    while linkedlist is not None:
        while linkedlist_next is not None:
            if(linkedlist_next.data == linkedlist.data):
                qntd +=1
                valor = linkedlist.data
            linkedlist_next = linkedlist_next.next
        qntd_por_numero[str(valor)] = qntd -1
        numero.add(valor)
        qntd = 0
        linkedlist = linkedlist.next
        linkedlist_next = self.head

    for i in numero:
        for j in qntd_por_numero:
            if(str(i) == j):
                for t in range(0, qntd_por_numero[j]):
                    self.__remove__(i)

    return self

@pytest.fixture(scope="session")
def data():
    array = []

    # test 1 data
    array.append([1, 1, 1, 3, 4, 4, 4, 5, 6, 6])

    # test 2 data
    array.append([1, 1, 1, 1, 1, 4, 4, 5, 6, 6])

    # test 3 data
    array.append([1, 1, 1, 1, 1, 1, 1])

    # test 4 data
    array.append([1, 9, 11, 15, 15, 16, 17])

    # test 5 data
    array.append([1])

    # test 6 data
    array.append([-5, -1, -1, -1, 5, 5, 5, 8, 8, 9, 10, 11, 11])

    # test 7 data
    array.append([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12])

    return array


def test_1(data):
    """
    Test evaluation for [1,1,1,3,4,4,4,5,6,6]
    """
    linkedlist = LinkedList()
    for item in data[0]:
        linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1, 3, 4, 5, 6]:
        linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist).__str__() == linkedlist_test.__str__()


def test_2(data):
    """
    Test evaluation for [1,1,1,1,1,4,4,5,6,6]
    """
    linkedlist = LinkedList()
    for item in data[1]:
        linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1, 4, 5, 6]:
        linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist).__str__() == linkedlist_test.__str__()


def test_3(data):
    """
    Test evaluation for [1,1,1,1,1,1,1]
    """
    linkedlist = LinkedList()
    for item in data[2]:
        linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1]:
        linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist).__str__() == linkedlist_test.__str__()


def test_4(data):
    """
    Test evaluation for [1,9,11,15,15,16,17]
    """
    linkedlist = LinkedList()
    for item in data[3]:
        linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1, 9, 11, 15, 16, 17]:
        linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist).__str__() == linkedlist_test.__str__()


def test_5(data):
    """
    Test evaluation for [1]
    """
    linkedlist = LinkedList()
    for item in data[4]:
        linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1]:
        linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist).__str__() == linkedlist_test.__str__()


def test_6(data):
    """
    Test evaluation for [-5,-1,-1,-1,5,5,5,8,8,9,10,11,11]
    """
    linkedlist = LinkedList()
    for item in data[5]:
        linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [-5, -1, 5, 8, 9, 10, 11]:
        linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist).__str__() == linkedlist_test.__str__()


def test_7(data):
    """
    Test evaluation for [1,2,3,4,5,6,7,8,9,10,11,12,12]
    """
    linkedlist = LinkedList()
    for item in data[6]:
        linkedlist.append(item)

    linkedlist_test = LinkedList()
    for item in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        linkedlist_test.append(item)

    assert removeDuplicatesFromLinkedList(linkedlist).__str__() == linkedlist_test.__str__()