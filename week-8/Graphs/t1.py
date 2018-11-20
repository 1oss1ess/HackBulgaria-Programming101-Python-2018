def deep_find(data, key):
    if key in data:
        return data[key]
    for k, v in data.items():
        if isinstance(v, dict):
            item = deep_find(v, key)
            if item is not None:
                return item
        # elif isinstance(v, list):
        #     for d in v:
        #         for result in deep_find(d, key):
        #             return result


my_data = {"id": "abcde",
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

print(deep_find(my_data, 'id'))
