# Mixins

## Serializers/Deserializers to and from JSON / XML

In a python module `utils.serializers`, create the following classes:

* `Jsonable` with methods
  * `to_json(indent=4)`
  * classmethod `from_json(json_string)`
* `Xmlable` with methods:
  * `to_xml()`
  * classmethod `from_xml(xml_string)`

Those classes should serve as mixins. Here is example usage:


```python
class Panda(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name
```

Now, lets see how we can turn our pandas in JSON / XML:

```python
>>> p = Panda(name='Ivo')
>>> p.to_json()
{
    "dict": {
        "name": "Ivo"
    },
    "class_name": "Panda"
}
>>> p.to_xml()
<Panda><name>Ivo</name></Panda>
```

Now, the other way around - we should be able to create panda instances from their respective JSON / XML representations:

```python
p = Panda(name='Ivo')
json_string = p.to_json()
xml_string = p.to_xml()

p1 = Panda.from_json(json_string)
p2 = Panda.from_xml(xml_string)

assert p == p1 #  Be sure to define __eq__
assert p == p2 #  Be sure to define __eq__
assert p1 == p2 #  Since we are not using PHP, we are not afraid of transitivity
```

Make additional type checks. Since we are keeping the `class_name` in our JSON or XML representation, if you try to create `Panda` from `Person` representation, raise a `ValueError`:

```python
class Person(Jsonable, Xmlable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

person = Person(name='Rado')
print(Panda.from_json(person.to_json()))  # ValueError
```

### Hints

* For XML, use the standard library - <https://docs.python.org/3/library/xml.etree.elementtree.html>
* think of `globals()` and `locals()`
