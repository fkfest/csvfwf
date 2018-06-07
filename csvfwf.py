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
    csvobj = csv.reader(csvfile,delimiter=inpdelim)
    for row in csvobj:
      table.append(row)
  # remove the last column if it's empty
  lastcol = [row[-1] for row in table]
  if all(not str(val).strip() for val in lastcol):
    table = [row[:-1] for row in table]
  return table

def OnlyEntry(row,icol):
  """check, if it's the only entry in the row"""
  for icolx in range(len(row)):
    if icolx != icol:
      if str(row[icolx]).strip():
        return False
  return True

def NextColumnDense(vals,icol,extlast):
  """check if the next column is dense (e.g., >20% of elements non empty)"""
  nval=0
  last=0
  for irow in range(len(vals)):
    if icol+1 >= len(vals[irow]):
      last+=1
    elif str(vals[irow][icol+1]).strip():
      nval += 1

  if last == len(vals):
    return extlast
  else:
    return (nval/len(vals)>0.2)

def CanExtend(row,icol,extlast):
  """check if the next element in the row is empty"""
  if icol+1 >= len(row):
    return extlast
  if not str(row[icol+1]).strip():
    return True
  return False


def FixWidth(vals):
  """generate a table with fixed width columns"""
  table1 = []
  offsrow = [0] * len(vals)
  for icol in range(len(vals[0])):
    #find the optimal width for each column
    maxlen=0
    for irow in range(len(vals)):
      if icol >= len(vals[irow]):
        vals[irow].append("")
      val=str(vals[irow][icol])
      val=val.strip()
      if delimiter in val:
        #add quotes
        val='"'+val+'"' 
      vals[irow][icol]=val
      itlen=len(val)+offsrow[irow]
      if offsrow[irow] == 0:
        itlen += 1
      if itlen > maxlen:
        # check whether one can expand to the next column
        if not NextColumnDense(vals,icol,offsrow[irow]) or not CanExtend(vals[irow],icol,offsrow[irow]):
        #if not OnlyEntry(vals[irow],icol):
          maxlen = itlen
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
    if Arg.startswith("-do"): 
      # output delimiter
      Arg = next(ArgsLoop)
      delimiter = Arg
    elif Arg.startswith("-di"): 
      # input delimiter
      Arg = next(ArgsLoop)
      inpdelim = Arg
    else:
      print("option "+Arg+" not known") 
  else:
    CSVFile = Arg
    table = GetTable(CSVFile)
    table = FixWidth(table)
    PrintTable(table)

