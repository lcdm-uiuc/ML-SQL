"""
Performs logic to handle the read keyword from ML-SQL language
"""

from ..utils.modelIO import load_model
from ..utils.filepath import is_mlsql_file

def handle_read(userfile, separator, header):
    """
    Main exported function
    Performs logic to handle the read keyword from ML-SQL language
    """
    if is_mlsql_file(userfile):
        model = load_model(userfile)
    else:
        return _read_data_file(userfile, separator, header)   


def _read_data_file(userfile, separator, header):
    """
    Reads a CSV-like file from memory with options for header and separator
    """
    from pandas import read_csv

    #create dataframe for read in file
    df = None

    #handle different parameters for read
    head = _handle_header(header)
    separ = _handle_separator(separator)

    #attempt to read file with given parameters
    try:
        df = read_csv(userfile, sep = separ, header = head)
    except OSError as e:
        print("Error importing file" + userfile)
        print(e)
        return None
    return (df)


def _handle_header(header):
    """
    Translates header into a proper value to be read by read_csv functions from pandas
    """
    if header is None or header == "":
        return None
    elif header.lower() == "false":
        return None
    elif header.lower() == "true":
        return True
    else:
        return True


def _handle_separator(sep):
    """
    Translates separator into a proper value to be read by read_csv functions from pandas
    """
    if sep is None or sep == "":
        return ","
    else:
        return str(sep)