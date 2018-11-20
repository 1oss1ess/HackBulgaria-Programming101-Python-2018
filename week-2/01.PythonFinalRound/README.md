Final Round
========================
In a file, called final_round.py, code the solutions to the following problems:

# 1. Is Number Balanced?
A number is called balanced, if we take the middle of it and the sums of the left and right parts are equal.

For example, the number `1238033` is balanced, because it's left part is `123` and right part is `033`.

We have: `1 + 2 + 3 = 0 + 3 + 3 = 6`.

* A number with only one digit is always balanced!

## Signature
```python
def is_number_balanced(number):
    pass
```

## Test Examples
```python
>>> is_number_balanced(9)
True
>>> is_number_balanced(4518)
True
>>> is_number_balanced(28471)
False
>>> is_number_balanced(1238033)
True
```

# 2. Increasing and Decreasing Sequences

Implement a function, called `increasing_or_decreasing(seq)` where the `seq` parameter is a `list` of integers.

## Signature
```python
def increasing_or_decreasing(seq):
    pass
```

The function should return `Up!`, if the given sequence is monotonously increasing.
If monotonously decreasing return `Down!` .
If both of the conditions are not satisfied, then return `False`.

And before you skip this problem, because of the math terminology, let me explain:

**A sequence is monotonously increasing if for every two elements `a` and `b`, that are next to each other (`a` is before `b`), we have `a` < `b`.**

For example, `[1,2,3,4,5]` is monotonously increasing, but `[1,2,3,4,5,1]` is not.

Test Examples
```python
>>> increasing_or_decreasing([1,2,3,4,5])
Up!
>>> increasing_or_decreasing([5,6,-10])
False
>>> increasing_or_decreasing([1,1,1,1])
False
>>> increasing_or_decreasing([9,8,7,6])
Down!
```

# 3. Largest Palindrome

Implement a function `get_largest_palindrome`, which returns the largest palindrome smaller than `n`. Given number `n` can also be a palindrome.

## Signature
```python
def get_largest_palindrome(n):
    pass
```

## Test Examples
```python
>>> get_largest_palindrome(99)
88
>>> get_largest_palindrome(252)
242
>>> get_largest_palindrome(994687)
994499
>>> get_largest_palindrome(754649)
754457
```

# 4. Sum all numbers in a given string

You are given a string, where there can be numbers. Return the sum of all numbers in that string(**not digits, numbers**).

## Signature
```python
def sum_of_numbers(input_string):
    pass
```

## Test Examples
```python
>>> sum_of_numbers("ab125cd3")
128
>>> sum_of_numbers("ab12")
12
>>> sum_of_numbers("ab")
0
>>> sum_of_numbers("1101")
1101
>>> sum_of_numbers("1111O")
1111
>>> sum_of_numbers("1abc33xyz22")
56
>>> sum_of_numbers("0hfabnek")
0
```

# 5. Birthday Ranges

Implement a function that calculates how many people are born in a range of `start` and `end` date(`end` is included in the range). The input parameters are:
- `birthdays` - a list of integers, which are in the range from 1 to 365 inclusive.
- `ranges` - a list of tuples, where each tuple has only two integer values(the first one represents the `start` date and the second - `end` date). All values are in the range from 1 to 365 inclusive.

## Signature
```python
def birthday_ranges(birthdays, ranges):
    pass
```

Calculate, for each tuple, how many people are born in that between the `start` and `end` date.

## Test Examples
```python
>>> birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)])
[2, 3, 4, 5, 2]
>>> birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)])
[5, 2, 0, 1]
```

# 6. 100 SMS

A long time ago, before the smartphones, when you had to write some messages, the keypads looked like that:

![Nokia 3310 Keypad](nokia.jpg)

For example, on such keypad, if you want to write **Ruby**, you had to press the following sequence of numbers:

```
7778822999
```

Each key contains some letters from the alphabet. And by pressing that key, you rotate the letters until you get to your desired one.

It's time to implement some encode / decode functions for the old keypads!

First, implement a function that takes a list of integers - the sequence of numbers that have been pressed. The returned value should be the corresponding string of the message.

## Signature:
```python
def numbers_to_message(pressed_sequence):
    pass
```

There are some special rules:

* If you press `1`, the next letter is going to be capitalized
* If you press `0`, this will insert a single white-space
* If you press a number and wait for a few seconds, the special breaking number `-1` enters the sequence. This is the way to write different letters from only one keypad!

## Test examples:
```python
>>> numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
"abc"
>>> numbers_to_message([2, 2, 2, 2])
"a"
>>> numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])
"Ivo e Panda"
```

Now it is time to convert the message to a sequence of numbers. This function takes a string - the `message` and returns the **minimal** keystrokes that you need to write that `message`

## Signature:
```python
def message_to_numbers(message):
    pass
```

## Test examples:
```python
>>> message_to_numbers("abc")
[2, -1, 2, 2, -1, 2, 2, 2]
>>> message_to_numbers("a")
[2]
>>> message_to_numbers("Ivo e Panda")
[1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 2, 6, 6, 3, 2]
>>> message_to_numbers("aabbcc")
[2, -1, 2, -1, 2, 2, -1, 2, 2, -1, 2, 2, 2, -1, 2, 2, 2]
```

# 7. Elevator Trips

Create a function, that calculates the minimal amount of trips an elevator must do to leave the people on their floors.
The input parameters are:
- `people_weight` - a list of integers, which represents the weight of people
- `people_floors` - a list of integers, which represents the floor, on which a person must go
- `elevator_floors` - the number of the elevator floors
- `max_people` - the maximum amount of people, that can be in the elevator at the same time
- `max_weight` - the maximum weight, that the elevator can handle

## Signature
```python
def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    pass
```

## Test Examples
```python
>>> elevator_trips([], [], 5, 2, 200)
0
>>> elevator_trips([40, 50], [], 5, 2, 200)
0
>>> elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200)
6
>>> elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200)
5
```
