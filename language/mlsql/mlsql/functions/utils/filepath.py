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


def is_mlsql_file(filepath):
    """
    Checks if the filename extension ends with a .mlsql suffix as the file type
    @return: boolean
    """
    dotsplit = filepath.split(".")
    extension = dotsplit[-1]
    return extension == "mlsql"

def file_exists(filename):
    """
    Returns whether a file exists by the path defined above
    """
    from os.path import isfile
    if isfile(filename):
        return True
    else:
        print("File '" + filename + "' does not exist")
        return False