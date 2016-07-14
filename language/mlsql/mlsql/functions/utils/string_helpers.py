def convert_ints(tokens):
    """
    Converts a list of string valued integers to a list of integers so that it does not
    manually have to be preformed on the function side. 
    NOT WORKING
    """
    split = tokens.split(",")
    val = list(map(int, split))
    return val


def convert_int(token):
    """
    Converts a string valued integer to a simple integer so that it does not
    manually have to be preformed on the function side. 
    """
    val = int(token)
    return val