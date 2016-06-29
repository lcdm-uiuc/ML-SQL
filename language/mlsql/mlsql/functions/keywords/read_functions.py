"""
Performs logic to handle the read keyword from ML-SQL language
"""

def handle_read(userfile, separator, header):
    """
    Performs logic to handle the read keyword from ML-SQL language
    """
    from pandas import read_csv

    #create dataframe for read in file
    df = None

    #attempt to read file with given parameters
    try:
        header = handle_header(header)
        separator = handle_separator(separator)
        df = read_csv(userfile, sep = separator, header = header)
    except OSError as e:
        print("Error importing file" + userfile)
        print(e)
        return None
    return (df)

def handle_header(header):
    """
    Translates header into a proper value to be read by read_csv functions from pandas
    """
    if header is None:
        return None
    elif header.lower() == "false":
        return None
    elif header.lower() == "true":
        return True
    else:
        return True

def handle_separator(sep):
    """
    Translates separator into a proper value to be read by read_csv functions from pandas
    """
    if sep is None:
        return ","
    else:
        return sep