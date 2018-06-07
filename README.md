# csvfwf

Create comma-separated fixed-width formated tables from csv files.

Usage: 

    csvfwf.py <csv-file> > <csv-fwf-file>

`-di` : define delimiter in the input file

`-do` : define delimiter for the output

Example:

Input file `input.csv`:

    This is a test file for csvfwf,,
    "First column, A","Second, B","Third, C"
    Row A,12.34,56.7
    Row B,8,12.12
    Here is a very long description for the following rows,,
    Row C,9.1,13.1415
    Here is a short description,,
    Here are two descriptions,,second

after running `csvfwf.py input.csv > output.csv` the output file `output.csv` contains:

    This is a test file for csvfwf,,           ,
     "First column, A", "Second, B", "Third, C",
                 Row A,       12.34,       56.7,
                 Row B,           8,      12.12,
    Here is a very long description for the following rows,,,
                 Row C,         9.1,    13.1415,
    Here is a short description,   ,           ,
    Here are two descriptions,     ,     second,

or after running `csvfwf.py -do "|" input.csv > output.csv` :

    This is a test file for csvfwf||     |
     First column, A| Second, B| Third, C|
               Row A|     12.34|     56.7|
               Row B|         8|    12.12|
    Here is a very long description for the following rows|||
               Row C|       9.1|  13.1415|
    Here is a short description||        |
    Here are two descriptions| |   second|


