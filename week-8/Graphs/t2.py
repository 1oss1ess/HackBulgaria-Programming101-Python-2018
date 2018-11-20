def deep_find_all(data, key):
    if isinstance(data, list):
        for i in data:
            for x in deep_find_all(i, key):
                yield x
    elif isinstance(data, dict):
        if key in data:
            yield data[key]
        for j in data.values():
            for x in deep_find_all(j, key):
                yield x


def get_recursively(search_dict, field):
    fields_found = []

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found


d = {"id": "abcde",
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
# my_data = {"c": [{"b": 2}, {'c': 3}]}
print(get_recursively(d, 'id'))
print(list(deep_find_all(d, 'id')))
