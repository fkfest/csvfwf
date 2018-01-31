#!/usr/bin/python3

import numpy as np
import pandas as pd

df = pd.read_csv("test1.csv")

cols = df.columns
vals = df.values
table = []
# find the optimal width for each column
for icol in range(len(cols)):
  col = cols[icol].strip()
  if col.startswith("Unnamed:") or col == "nan":
    col = ""
  maxlen=len(col)
  #print(col,maxlen)
  for irow in range(len(vals)):
    val=str(vals[irow][icol])
    val=val.strip()
    itlen=len(val)
    if itlen > maxlen:
      maxlen = itlen
    #print("*",val,"*")
  #print("maxlen=",maxlen)
  maxlen += 1
  fcol=[]
  fcol.append('{:>{}}'.format(col,maxlen))
  for irow in range(len(vals)):
    val=str(vals[irow][icol])
    val=val.strip()
    if val.startswith("Unnamed:") or val == "nan":
      val = ""
    fcol.append('{:>{}}'.format(val,maxlen))
  #print(fcol)
  table.append(fcol)
#output
for irow in range(len(vals)+1):
  for icol in range(len(cols)):
    print(table[icol][irow],",",end="",sep="")
  print()

#print(table)

