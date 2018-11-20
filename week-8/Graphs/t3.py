def deep_update(data, key, val):
    if isinstance(data, list):
        for i in data:
            for x in deep_update(i, key, val):
                yield x
    elif isinstance(data, dict):
        if key in data:
            data[key] = val
            yield data[key]
        for j in data.values():
            for x in deep_update(j, key, val):
                yield x


data = {"id": "abcde",
        "key1": "blah",
        "key2": "blah blah",
        "nestedlist": [
            {"id": "qwerty",
             "nestednestedlist": [
              {"id": "xyz", "keyA": "blah blah blah"},
              {"id": "fghi", "keyZ": "blah blah blah"}],
             "anothernestednestedlist": [
                 {"id": "asdf", "keyQ": "blah blah"},
                 {"id": "yuiop", "keyW": "blah"}]}]}

print(dict(deep_update(data, 'id', 'gh')))
print(data)
