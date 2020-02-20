#!/bin/python3


from collections import *
import copy

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:
    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file
    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)
    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    s = [] # create a stack
    s.append(start_word) # push start_word on stack
    q = deque([]) #create queue
    q.append(s) # enqueue stack onto queue
    # print("q = ", q)

    differences = _diff(start_word, end_word)
    # print(len(differences))
    file = open("words5.dict", "r")
    file = file.read().split("\n")

    if start_word == end_word:
        print(s)
        return s

    while q: # while queue not empty
        # print("q = ", q)
        dequeue_stack = q.pop() #dequeue stack from queue

        # print("dequeue_stack = ", dequeue_stack)
        # print("stack_val = ", elem)
        for word in file:
            # print(str(dequeue_stack.pop))
            # print("_adjacent(word, str(dequeue_stack.pop)) = ", _adjacent(word, str(dequeue_stack.pop)))
            if _adjacent(word, dequeue_stack[-1]) and len(differences) >= len(_diff(word, end_word)):
                # print(word)
                print(len(_diff(word, end_word)))
                differences = _diff(word, end_word)
                if word == end_word:
                    dequeue_stack.append(word)
                    print("dequeue_stack = ", dequeue_stack)
                    # print(q.pop())
                    return dequeue_stack
                copy_s = copy.deepcopy(dequeue_stack)
                copy_s.append(word)
                q.append(copy_s)
                file.remove(word)
            # print(word)
    print("returning none")
    return None

    # print(copy_s)
    # return s

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''

    if not ladder:
        return False

    for i in range(len(ladder)):
        if i != len(ladder)-1 and not _adjacent(ladder[i], ladder[i+1]):
            return False

    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.
    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    diff_char = []

    if len(word1) != len(word2):
        # print("False")
        return False

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_char.append(word1[i])

    # print(len(diff_char) == 1)
    return len(diff_char) == 1

def _diff(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.
    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    diff_index = []

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            diff_index.append(i)

    # print(len(diff_char) == 1)

    return diff_index


# word_ladder('stone','money')
# verify_word_ladder(['stone', 'shone', 'phone', 'phony', 'peony', 'benny', 'bonny', 'boney', 'money'])
# word_ladder('aloof','aloof')
word_ladder('money','stone')


