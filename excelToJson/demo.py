import xlrd
from collections import OrderedDict
import json
import codecs
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

cur_path = os.getcwd()
excel_file = cur_path + "\\demo.xlsx"

wb = xlrd.open_workbook(excel_file)

convert_list = {}
sh = wb.sheet_by_index(0)
title = sh.row_values(1)
pass_id = 0
is_read_next = False
index = 0
for rownum in range(2, sh.nrows):
    rowvalue = sh.row_values(rownum)
    if len(rowvalue) > 0:
        tmp = {}
        chapt_id = str(int(rowvalue[0]))
        for i in range(1, len(rowvalue)) :
            strval = str(rowvalue[i])
            if strval.find(';') != -1 :
                tmp[title[i]] = strval.split(';')
            else:
                tmp[title[i]] = rowvalue[i]
             
        print(chapt_id)
        convert_list[chapt_id] = tmp
        index = index + 1

          

if len(convert_list) > 0 :
    j = json.dumps(convert_list)
    file_str = j.strip().decode('unicode-escape').encode('utf-8')
    #print(file_str, str(int(pass_id)))
    json_file = cur_path + "\\" + 'chapt' + '.json'
    print(json_file)
    with codecs.open(json_file,"wb","utf-8") as f:
        f.write(j.strip().decode('unicode-escape').encode('utf-8'))
    convert_list.clear()


