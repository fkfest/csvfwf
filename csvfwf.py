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
      table.append(row)
  return table

def OnlyEntry(row,icol):
  """check, if it's the only entry in the row"""
  for icolx in range(len(row)):
    if icolx != icol:
      if str(row[icolx]).strip():
        return False
  return True

def FixWidth(vals):
  """generate a table with fixed width columns"""
  table1 = []
  offsrow = [0] * len(vals)
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
        #don't count single entries in the row
        if not OnlyEntry(vals[irow],icol):
          maxlen = itlen
    maxlen += 1
    fcol=[]
    for irow in range(len(vals)):
      rowwidth = maxlen
      if offsrow[irow] > 0:
        if offsrow[irow] < maxlen:
          rowwidth = maxlen - offsrow[irow]
        else:
          rowwidth = 0
        offsrow[irow] -= maxlen - rowwidth
      fcol.append('{:>{}}'.format(vals[irow][icol],rowwidth))
      itlen = len(vals[irow][icol])
      if itlen > maxlen:
        offsrow[irow] = itlen - maxlen;
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

