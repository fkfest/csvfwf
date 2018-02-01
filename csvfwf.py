#!/usr/bin/python3

import sys
from sys import stdout, argv, stderr
import csv

#default delimiter
delimiter = ","
#default delimiter for input files
inpdelim = ","

def GetTable(CSVFile):
  """read csv to a table"""
  table = []
  with open(CSVFile, newline='') as csvfile:
    csvobj = csv.reader(csvfile)
    for row in csvobj:
      print(row)    
      table.append(row)
  return table

def FixWidth(vals):
  """generate a table with fixed width columns"""
  table1 = []
  for icol in range(len(vals[0])):
    #find the optimal width for each column
    maxlen=0
    for irow in range(len(vals)):
      val=str(vals[irow][icol])
      val=val.strip()
      if delimiter in val:
        #add quotes
        val='"'+val+'"' 
      vals[irow][icol]=val
      itlen=len(val)
      if itlen > maxlen:
        maxlen = itlen
    maxlen += 1
    fcol=[]
    for irow in range(len(vals)):
      fcol.append('{:>{}}'.format(vals[irow][icol],maxlen))
    table1.append(fcol)
  #transpose the table
  return [list(i) for i in zip(*table1)]

def PrintTable(table):
  for irow in range(len(table)):
    for icol in range(len(table[0])):
      print(table[irow][icol],delimiter,end="",sep="")
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
    table = GetTable(CSVFile)
    table = FixWidth(table)
    PrintTable(table)

