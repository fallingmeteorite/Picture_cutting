#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image


def cut_main(image_path, width_incise, height_incise, file_name, quality_save):
    img = Image.open(image_path)
    width, height = img.size
    crop_width = width // width_incise
    crop_height = height // height_incise
    number_save = 0
    for i in range(height_incise):
        for j in range(width_incise):
            number_save += 1
            left = j * crop_width
            top = i * crop_height
            right = left + crop_width
            bottom = top + crop_height
            crop_img = img.crop((left, top, right, bottom))
            crop_img.save(f'Images_save/{file_name}{str(number_save).zfill(3)}.jpg', quality=quality_save)
