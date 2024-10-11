#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, shutil
from tqdm import tqdm
from Picture_cutting import cut_main
from PDF_produced import pdf_main


def run():
    files = os.listdir('./Pretreatment')
    num_png = len(files)
    for i in tqdm(range(num_png), desc=r"处理进度", ncols=150):
        file_one = ('./Pretreatment/' + files[i])
        try:
            cut_main(image_path=file_one, width_incise=3, height_incise=5, file_name=((files[i]).rsplit('.', 1)[0]), quality_save=10)
        except:
            print("损坏文件名称:" + str(file_one))

run()
print('正在把文件夹内所有图片转换为一个pdf文档,请稍等(图片需按顺序命名)')
pdf_main()
print('转换成功,开始清理缓存文件,请稍等')

#shutil.rmtree('Images_save')
#os.mkdir('Images_save')

