"""Here is my solution for Kata 'Can you get the loop?'.
Task description you can find on link below
https://www.codewars.com/kata/52a89c2ea8ddc5547a000863 """

def loop_size(node):
    lst = []
    while True:
        node = node.next
        if node in lst:
            return len(lst[lst.index(node):])
        else:
            lst.append(node)
