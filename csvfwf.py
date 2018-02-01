#!/usr/bin/python3

import sys
from sys import stdout, argv, stderr
import pandas

#default delimiter
delimiter=","

def RemovePandasNan(val):
  """resets values set by pandas to empty space again"""
  if val.startswith("Unnamed:") or val == "nan":
    val = ""
  return val

def FixWidth(df):
  """generate a table with fixed width columns"""
  cols = df.columns
  vals = df.values
  table = []
  for icol in range(len(cols)):
    col = cols[icol].strip()
    col=RemovePandasNan(col)
    #find the optimal width for each column
    maxlen=len(col)
    for irow in range(len(vals)):
      val=str(vals[irow][icol])
      val=val.strip()
      val=RemovePandasNan(val)
      vals[irow][icol]=val
      itlen=len(val)
      if itlen > maxlen:
        maxlen = itlen
    maxlen += 1
    fcol=[]
    fcol.append('{:>{}}'.format(col,maxlen))
    for irow in range(len(vals)):
      fcol.append('{:>{}}'.format(vals[irow][icol],maxlen))
    table.append(fcol)
  return table

def PrintTable(table):
  for irow in range(len(table[0])):
    for icol in range(len(table)):
      print(table[icol][irow],delimiter,end="",sep="")
    print()

ArgsLoop = iter(sys.argv[1:]) 
for Arg in ArgsLoop:
  if Arg.startswith("-"):
    if Arg.startswith("-d"): 
      Arg = next(ArgsLoop)
      delimiter = Arg
    else:
      print("option "+Arg+" not known") 
  else:
    CSVFile = Arg
    df = pandas.read_csv(CSVFile)
    table = FixWidth(df)
    PrintTable(table)

