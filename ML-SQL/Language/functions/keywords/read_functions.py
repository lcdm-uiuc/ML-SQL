"""
Performs logic to handle the read keyword from ML-SQL language
"""

def handle_read(userfile, separator, header):
	from pandas import read_csv
	df = read_csv(userfile, sep = separator, header = header)
	return (df)