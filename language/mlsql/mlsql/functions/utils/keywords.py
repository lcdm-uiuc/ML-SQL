keywords = ["load", "read", "split", "replace", "classify", "regress", "cluster", "save"]

def keyword_check(parsing):
    keys = {}
    for key in keywords:
        parse_check = None
        try:
            parse_check = parsing[key]
        except KeyError:
            parse_check = ""
        keys[key] = (parse_check is not None) and (parse_check != "")

    return keys