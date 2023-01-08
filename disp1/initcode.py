# coding=utf-8
""" initcode.py
"""
from __future__ import print_function
import sys, re,codecs

def make_line(disppage, isect=''):
 # disppage is int; it is the page number shown on a page
 # offset is particular to speijer
 # pagenum is the string whose value is used to generate the file name
 #  for the image of the page with given disppage
 offset = 16
 ipagenum = disppage + offset
 pagenum = '%03d' % ipagenum
 word = '&sect; %s' % isect
 line = "{'disppage': %s, 'pagenum':'%s', 'word':'%s'}, " %(disppage,pagenum,word)
 return line
def make_lines(ipage1,ipage2):
 lines = []
 for idx,ipage in enumerate(range(ipage1,ipage2+1)):
  # print('ipage=',ipage)
  # isect = isect1 + idx
  lines.append(make_line(ipage))
 return lines

def make_outrec(rec):
 code,lines = rec
 outarr = []
 outarr.append(" '%s': [" % code)
 for line in lines:
  outarr.append("     %s" % line)
 outarr.append("    ],") 
 return outarr

def write_recs(fileout,recs):
 outrecs = []
 for rec in recs:
  outrec = make_outrec(rec)
  outrecs.append(outrec)
 with codecs.open(fileout,"w","utf-8") as f:
  nout = 0
  for outrec in outrecs:
   for out in outrec:
    f.write(out+'\n')
    nout = nout + 1
 print(len(recs),"records written to",fileout)
 print(nout,"lines written")

codep12 = """
01,1-13
02,13-23
03,24-29
04,29-42
05,42-58
06,58-67
07,67-81
08,81-101
09,102-113
10,113-134
11,134-141
12,141-145
13,146-178
14,179-193
15,193-201
16,201-215
17,215-221
18,221-222
19,222-227
20,228-235
21,235-241
22,241-278
23,241-278
24,278-296
25,296-300
26,300-309
27,310-315
28,315-320
27,320-326
28,326-329
27,329-336
28,337-346
27,347-352
28,352-357
27,358-372
28,372-379
28,379-388
""".splitlines()
if __name__=="__main__":
 fileout = sys.argv[1]
 recs = []
 for iline,line in enumerate(codep12):
  option = line.strip()
  m = re.search(r'^([0-9]+).([0-9]+).([0-9]+)',option)
  if m == None:
   print('WARNING. Line %s of codep12 not parsed: "%s"' % (iline+1,option))
   continue
  code = m.group(1)
  ipage1 = int(m.group(2))
  ipage2 = int(m.group(3))
  lines = make_lines(ipage1,ipage2)
  rec = (code,lines)
  recs.append(rec)
 write_recs(fileout,recs)
 
