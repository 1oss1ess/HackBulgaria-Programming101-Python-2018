Dive into Python
========================

Code the solutions to the following problems :)


## Counting substrings
----------------

Implement the function `count_substrings(haystack, needle)`. It returns the count of occurrences of the string `needle` in the string `haystack`.

__Don't count overlapped substings and take case into consideration!__
For overlapping substrings, check the "baba" example below.

### Signature

```python
def count_substrings(haystack, needle):
    pass
```

### Test examples

```python
>>> count_substrings("This is a test string", "is")
2
>>> count_substrings("babababa", "baba")
2
>>> count_substrings("Python is an awesome language to program in!", "o")
4
>>> count_substrings("We have nothing in common!", "really?")
0
>>> count_substrings("This is this and that is this", "this")  # "This" != "this"
2
```



## Sum Numbers in Matrix
----------------

You are given a `NxM` matrix  of integer numbers.

Implement a function, called `sum_matrix(m)` that returns the sum of all numbers in the matrix.

The matrix will be represented as nested lists in Python.

### Examples:

```python
>>> m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> sum_matrix(m)
45
>>> m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> sum_matrix(m)
0
>>> m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
>>> sum_matrix(m)
55
```


## NaN Expand
----------------

In most programming languages, `NaN` stands for `Not a Number`.

If we take a look at the following JavaScript code:

```javascript
typeof NaN === 'number' // true
```

We will see that in JavaScript, `NaN` stands for `Not a NaN`, which is recursive by nature.

Implement a Python function, called `nan_expand(times)`, which returns the expansion of `NaN` (In JavaScript terms :P) that many `times`.

For example:

* If we expand `NaN` once (`times=1`), we will have `"Not a NaN"`
* If we expand `NaN` twice (`times=2`), we will have `"Not a Not a NaN"`
* If `times=3`, we have `"Not a Not a Not a NaN"`
* And so on ...

### Examples

```python
>>> nan_expand(0)
""
>>> nan_expand(1)
"Not a NaN"
>>> nan_expand(2)
"Not a Not a NaN"
>>> nan_expand(3)
"Not a Not a Not a NaN"
```


## Integer prime factorization
----------------

Given an integer `n`, we can factor it in the following form:

```
n = p1^a1 * p2^a2 * ... * pn^an
```

Where each `p` is a prime number and each `a` is an integer and `p^a` means `p` to the power of `a`.

[This is called prime factorization.](http://mathworld.wolfram.com/PrimeFactorization.html)

Lets see few examples:

```
10 = 2^1 * 5^1
25 = 5^2
356 = 2^2 * 89 ^ 1
```

Implement a function, called `prime_factorization(n)`, which takes an integer and returns a list of tuples `(pi, ai)` that is the result of the factorization.

The list should be sorted in increasing order of the prime numbers.

### Signature

```python
def prime_factorization(n):
    pass
```

### Test examples

```python
>>> prime_factorization(10)
[(2, 1), (5, 1)] # This is 2^1 * 5^1
>>> prime_factorization(14)
[(2, 1), (7, 1)]
>>> prime_factorization(356)
[(2, 2), (89, 1)]
>>> prime_factorization(89)
[(89, 1)] # 89 is a prime number
>>> prime_factorization(1000)
[(2, 3), (5, 3)]
```


## The group function
----------------

We are going to implement a very helpful function, called `group`.

`group` takes a list of things and returns a list of group, where each group is formed by all **equal consecutive elements** in the list.


For example:

```python
group([1, 1, 1, 2, 3, 1, 1]) == [[1, 1, 1], [2], [3], [1, 1]]
group([1, 2, 1, 2, 3, 3]) == [[1], [2], [1], [2], [3, 3]]
```

## Longest subsequence of equal consecutive elements
----------------

Implement the function `max_consecutive(items)`, which takes a list of things and returns an integer - the count of elements in the longest subsequence of equal consecutive elements.

For example, in the list `[1, 2, 3, 3, 3, 3, 4, 3, 3]`, the result is 4, where the longest subsequence is formed by `3, 3, 3, 3`

### Signature

```python
def max_consecutive(items):
    pass
```

### Test examples

```python
>>> max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3])
4
>>> max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5])
3
```



## Word counter
----------------

You are given a rectangular table filled with characters and a `word`.
Your task is to count the occurences of a `word` in the table. The word can be found horizontaly, vertically and across both left to right and right to left.

### For example:

Find the word `ivan` in the table:

| i    | v     | a     | n     |
|---   |---    |---    |---    |
| e    | **v** | **n** | h     |
| i    | n     | **a** | v     |
| m    | v     | **v** | **n** |
| q    | r     | **i** | t     |

Result:
```
3
```
The first thing you need to do is to input the word you are looking for.
You need to provide the number of rows and columns of your table.
Then input the characters into the table.

Note: If the word you are looking for is longer than the length of your rows, columns or diagonals, you need to return message to the user that the input was invalid.

## Example inputs:

### Example 1:

```
ivan
5 4
i v	a n
e v n h
i n	a v
m v	v n
q r	i t
```

Should print:

```
3
```

### Example 2:

```
actually
8 15
i v a n q h r e z g t z o y m
e v n h t r x e k y d a i l c
i a c t u a l l y m c x r l e
m v c n p u a m n t l u e a a
q r i t w e a q u p r x t u z
p e a c t u a l l y w p y t m
o y h t r e l u f p q n z c s
p a c t u a l l y u r e q a r
```

Should print:

```
4
```

### Example 3:

```
madam
8 12
z v a n q h r e z g t z
e v m h t r x e k y m a
i a c a u a l l y a c x
m v c n d u a m d t l u
q t i t w a a a u p r x
p e m a d a m l l y w p
o y h t e e l u f p q n
p a c t u a l l y u r e
```

Should print:

```
3
```
Notice that this should print 3, not 6!


### Example 4:

```
table
3 4
```

Should print:

```
Invalid number of rows or columns!
```

## Gas Stations
----------

We are implementing a smart GPS software.

- We are taking a long trip from Sofia to Plovdiv and we know the distance between the two cities.It is a positive integer and we mark it as ``distance``.

- We know how much our car can ride with a full tank of gas. It is a positive integer in kilometers. We mark it as ``tank_size``.

- We have a list of gas stations. We know the distance between Sofia and the current gas station. ``stations = [50, 80, 110, 180, 220, 290]`` The list is sorted!

By using this information we will implement a function that returns the shortest `list` of gas stations that we have to visit in order to travel from Sofia to Plovdiv. Know that are allways starting with a full tank_size.

## Signature
```python
def gas_stations(distance, tank_size, stations):
	pass
```

## Test Example
```python
>>> gas_stations(320, 90, [50, 80, 140, 180, 220, 290])
[80, 140, 220, 290]
>>> gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350])
[70, 140, 210, 280, 350]
```
