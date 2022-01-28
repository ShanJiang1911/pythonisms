from re import L
from xml.dom import IndexSizeErr
import pytest

from linked_list import LinkedList

def test_for_in():
    animals = LinkedList(("dog", "cat", "tiger"))
    animals_list = []
    for animal in animals:
        animals_list.append(animal)
    assert animals_list == ["dog", "cat", "tiger"]

def test_list_comprehension():
    origin_nums = LinkedList(("1", "2", "3"))
    squared_nums = [int(num)**2 for num in origin_nums]
    assert squared_nums == [1, 4, 9]

def test_convert_list():
    animal_list = ["dog", "cat", "tiger"]
    animals = LinkedList(animal_list)
    assert list(animals) == animal_list

def test_length():
    num_range = range(1, 11)
    nums = LinkedList(num_range)
    assert len(nums) == 10

def test_filter():
    nums = LinkedList(range(1, 11))
    even = [num for num in nums if num%2==0 ]
    assert even == [2,4,6,8,10]

def test_next():
    animal = LinkedList(["dog", "cat", "tiger"])
    iterator = iter(animal)
    assert next(iterator) == "dog"
    assert next(iterator) == "cat"
    assert next(iterator) == "tiger"

def test_stop_iteration():
    animal = LinkedList(["dog", "cat", "tiger"])
    iterator = iter(animal)
    with pytest.raises(StopIteration):
        while True:
            name = next(iterator)

def test_str():
    nums = LinkedList(["1", "2", "3"])
    assert str(nums) == "[ 1 ] -> [ 2 ] -> [ 3 ] -> None"

def test_equal():
    num_a = LinkedList(["1", "2", "3"])
    num_b = LinkedList(["1", "2", "3"])
    assert num_a == num_b

def test_get_item():
    animals = LinkedList(["dog", "cat", "tiger"])
    assert animals[2] == "tiger"

def test_get_wrong_index():
    nums = LinkedList(["1", "2", "3"])
    with pytest.raises(IndexError):
        nums[10]

def test_set_item():
    animals = LinkedList(["dog", "cat", "tiger"])
    animals[0] = "hippo"
    assert animals[0] == "hippo"