# Are two words anagrams?
Create a function, that reads two words from the standard input and output and returns if the two of them are anagrams.

For example, `listen` and `silent` are anagrams.
**Consider lowering the case of the two words since the case does not matter. `SILENT` and `listen` are also anagrams.**

## Signature:
```python
def anagrams():
    pass
```

* `ANAGRAMS` if the words are anagrams of each other
* `NOT ANAGRAMS` if the two words are not anagrams of each other



## Test Examples

Input:

```
TOP_CODER COTO_PRODE
```

Output:

```
NOT ANAGRAMS
```

---

Input:

```
kilata cvetelina_yaneva
```

Output:

```
NOT ANAGRAMS
```

Also, should not make songs together.

---

Input:

```
BRADE BEARD
```

Output:

```
ANAGRAMS
```

## Test Signature
To verify that your implementation is right, use the following signature and upload your solution to the system.

```python
def anagrams(word_1, word_2):
    pass
```

The returned value is either 'ANAGRAMS' or 'NOT ANAGRAMS'.
