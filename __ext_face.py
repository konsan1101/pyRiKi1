#!/usr/bin/env python
# -*- coding: utf-8 -*-

# COPYRIGHT (C) 2014-2020 Mitsuo KONDOU.
# This software is released under the MIT License.
# https://github.com/konsan1101
# Thank you for keeping the rules.



import sys
import os
import time
import datetime
import codecs
import glob

import cv2



# 共通ルーチン
import  _v5__qGuide
qGuide= _v5__qGuide.qGuide_class()



if __name__ == '__main__':

    # パラメータ
    imgPath = '_icons/'
    imgFile = 'detect_face.png'

    if (len(sys.argv) >= 2):
        imgPath = str(sys.argv[1])
        if (imgPath[:-1] != '/'):
            imgPath += '/'
    if (len(sys.argv) >= 3):
        imgFile  = str(sys.argv[2])

    # 画像表示
    imgFile = imgPath + imgFile
    img = cv2.imread(imgFile)
    qGuide.init(panel='auto', title='detect_face', image=img,)
    qGuide.open()

    # メッセージ
    time.sleep(0.25)
    qGuide.setMessage(txt='detect', )

    # 待機
    chkTime = time.time()
    while ((time.time() - chkTime) < 3):
        event, values = qGuide.read()
        if event in (None, 'Exit'):
            break

    # 画像消去
    qGuide.close()
    qGuide.terminate()


