def get_relative_filename(filename):
    """
    returns only the last part of a file (removes all subdirectories from filename)
    """
    slash_split = filename.split("/")
    return slash_split[-1]


def get_model_type(model):
    """
    returns the name of a sklearn model (indentifies from string version of it)
    """
    stringm = str(model)
    split_paren = stringm.split("(")
    return split_paren[0]