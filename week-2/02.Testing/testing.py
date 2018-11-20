def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]

    if denominator == 0:
        raise Exception("Division by zero is undefined")
    elif nominator == 0:
        return 0
    elif nominator > denominator:
        for index in range(2, denominator + 1):
            while (denominator % index == 0) and (nominator % index == 0):
                nominator /= index
                denominator /= index
    else:
        for index in range(2, nominator + 1):
            while (nominator % index == 0) and (denominator % index == 0):
                nominator /= index
                denominator /= index

    return (int(nominator), int(denominator))


def collect_fractions(fractions):
    for index in range(len(fractions)):
        if index == 0:
            nominator1 = fractions[index][0]
            denominator1 = fractions[index][1]
        elif denominator1 == 0:
            raise Exception("Division by zero is undefined")
        elif nominator1 == 0:
            return 0
        else:
            nominator2 = fractions[index][0]
            denominator2 = fractions[index][1]
            if denominator2 == 0:
                raise Exception("Division by zero is undefined")
            elif nominator2 == 0:
                return 0
            if denominator1 == denominator2:
                nominator1 += nominator2
            else:
                current_denominator1 = denominator1
                current_denominator2 = denominator2
                denominator1 *= denominator2
                nominator1 *= current_denominator2
                nominator2 *= current_denominator1
                nominator1 += nominator2
    return simplify_fraction((nominator1, denominator1))


def sort_fractions(fractions):
    result = []
    my_dict = {}
    for index in range(len(fractions)):
        nominator = fractions[index][0]
        denominator = fractions[index][1]
        my_dict.update({(nominator, denominator): nominator / denominator})
    sorted_by_value = sorted(my_dict.items(), key=lambda kv: kv[1])
    for sorted_index in sorted_by_value:
        result.append(sorted_index[0])
    return result
