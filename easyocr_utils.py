import cv2
import numpy as np

import easyocr

from constants import LANGUAGE_MAPPING

def show_uploaded_file(uploaded_image):
    opencv_image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)
    
    return opencv_image

def language_mapping(selected_language_list):
    final_language_mapping = []
    #key, val = next(iter(LANGUAGE_MAPPING.items()))

    for eachLangMap in LANGUAGE_MAPPING:
        each_language_name = eachLangMap
        for eachSelectedLang in selected_language_list:
            if eachSelectedLang == each_language_name:
                each_language_mapping = LANGUAGE_MAPPING[each_language_name]
        
                final_language_mapping.append(each_language_mapping)
    
    return final_language_mapping


def ocr_reader(lang_list):
    reader = easyocr.Reader(lang_list, gpu=True)
    return reader

def read_image(reader,image,with_detail=False):
    result = None

    if with_detail is True:
        result = reader.readtext(image, detail=0)
    else:
        result = reader.readtext(image) 
    return result