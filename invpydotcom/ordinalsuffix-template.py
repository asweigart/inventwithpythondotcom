def ordinalSuffix(number):
    numberStr = str(number)

    # 11, 12, and 13 have the suffix th:
    if numberStr[____:] in ('11', ____, ____):
        return numberStr + 'th'
    # Numbers that end with 1 have the suffix st:
    if numberStr[____] == '1':
        return numberStr + 'st'
    # Numbers that end with 2 have the suffix nd:
    if numberStr[____] == ____:
        return numberStr + 'nd'
    # Numbers that end with 3 have the suffix rd:
    if numberStr[____] == ____:
        return numberStr + 'rd'
    # All other numbers end with th:
    return ____ + ____
