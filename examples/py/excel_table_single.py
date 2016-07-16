#!/usr/bin/env python
# encoding: utf-8

import pytablewriter


writer = pytablewriter.ExcelXlsxTableWriter()
writer.open_workbook("sample.xlsx")

writer.make_worksheet("example")
writer.header_list = ["int", "float", "str", "bool", "mix", "time"]
writer.value_matrix = [
    [0,   0.1,      "hoge", True,   0,      "2017-01-01 03:04:05+0900"],
    [2,   "-2.23",  "foo",  False,  None,   "2017-12-23 12:34:51+0900"],
    [3,   0,        "bar",  "true",  "inf", "2017-03-03 22:44:55+0900"],
    [-10, -9.9,     "",     "FALSE", "nan", "2017-01-01 00:00:00+0900"],
]
writer.write_table()

writer.close()
