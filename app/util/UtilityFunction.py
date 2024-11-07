from typing import List


def transform(list1: List[str], list2: List[str]) -> str:
    result = ""
    for i in(range(len(list1))):
        result = result + list1[i].upper() +"," +list2[i].upper()
    return result

def key(list1: List[str], list2: List[str]) -> str:
    result = ""
    for i in(range(len(list1))):
        result = result + list1[i] +","+list2[i]
    return result