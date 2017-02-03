# Data Range Parser

Simple python script to range date array into a time series date range.

Inputand output data formats can be found on the example files input.txt and output.txt file.

###Usage:

python rangedate.py -i input.txt -o output.txt -f 2015-10-22 -t 2017-01-10 -p f

###Legand

-i (mandatory) - Input file. This should be in the format of the sample file (input.txt)

-o (optional) - Output file. If you don't specify, defalut file name is output.txt

-f (optional) - From date. The starting date of the time series. If not specified, it will take the first date in the input file as the starting date.

-t (optional) - To date. The ending date of the time series. If not specified, it will take the last date in the input file as the To date.

-p (optional) - Output format. If you need both date and occurances, enter 'F', 'f' or keep not specified. If you want only the occurance value in order of the time series, you must specify the value - 'T' or 't'. 
