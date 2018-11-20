def reduce_file_path(path):
    result = ''

    for char in path:
        if char == '.':
            if len(result) > 1 and result[-1] == '.':
                result += char
                result = result[: result.find('..') - 1]
                split_text = result.split('/')
                result = split_text[0] + '/'
            else:
                result += char
        elif char == '/':
            if len(result) > 1 and result[-1] == '/':
                continue
            result += char
        else:
            result += char

    while result[-1] == '/' or result[-1] == '.':
        if len(result) > 1 and '/' in result or '.' in result:
            result = result[: len(result) - 1]
        else:
            break
    return result
