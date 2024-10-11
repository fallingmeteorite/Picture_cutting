#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image

def sort_by_first_three_chars(s):
    return s[:6]

def pdf_main():
    path = 'Images_save'
    name = 'output'
    img_open_list = []
    sorted_file_list = sorted(os.walk(path), key=sort_by_first_three_chars)
    for root, dirs, files in sorted_file_list:
        for i in files:
            file = os.path.join(root, i)
            img_open = Image.open(file)
            if img_open.mode != 'RGB':
                img_open = img_open.convert('RGB')
            img_open_list.append(img_open)
    pdf_name = name + '.pdf'
    img_1 = img_open_list[0]
    img_open_list = img_open_list[1:]
    img_1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=img_open_list)

