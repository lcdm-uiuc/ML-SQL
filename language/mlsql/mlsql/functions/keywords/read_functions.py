"""
Performs logic to handle the read keyword from ML-SQL language
"""

def handle_read(userfile, separator, header):
    from pandas import read_csv

    #create dataframe for read in file
    df = None

    #attempt to read file with given parameters
    try:
        df = read_csv(userfile, sep = separator, header = header)
    except OSError as e:
        print("Error importing file" + userfile)
        print(e)

    return (df)