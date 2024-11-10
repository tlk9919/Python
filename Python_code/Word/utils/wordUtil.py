#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/26 9:14
# @Author  : 刘宇
# @File    : wordUtil.py
from docxtpl import DocxTemplate
from docx.shared import Mm
from docxtpl.inline_image import InlineImage
from ExcelUtil import excel2dict

metaData_path = "../data/metaData.xlsx"
metaData_dict = excel2dict(metaData_path)

tpl_path = "../data/tpl.docx"
for student in zip(*list(metaData_dict.values())):
    doc = DocxTemplate(tpl_path)
    data = {
        "s_grade": student[0],
        "s_title": student[1],
        "s_name": student[2],
        "s_num": student[3],
        "s_subject1": student[4],
        "s_subject2": student[5],
        "s_subject3": student[6],
        "t_img": InlineImage(doc, "../data/zj.jpg", width=Mm(18), height=Mm(8))
    }
    doc.render(data)
    doc.save(f"../output/{data['s_num']}_{data['s_name']}_{data['s_title']}.docx")

if __name__ == "__main__":
    run_code = 0
