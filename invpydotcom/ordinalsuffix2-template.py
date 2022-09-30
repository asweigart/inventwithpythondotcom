def ordinalSuffix(number):
    # 11, 12, and 13 have the suffix th:
    if ____ % 100 in (11, ____, ____):
        return str(number) + 'th'
    # Numbers that end with 1 have the suffix st:
    if ____ % 10 == ____:
        return str(number) + 'st'
    # Numbers that end with 2 have the suffix nd:
    if ____ % 10 == ____:
        return str(number) + 'nd'
    # Numbers that end with 3 have the suffix rd:
    if ____ % 10 == ____:
        return str(number) + 'rd'
    # All other numbers end with th:
    return ____(____) + ____
