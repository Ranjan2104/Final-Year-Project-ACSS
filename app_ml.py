import cv2
import matplotlib.pyplot as plt
import numpy as np
from pytesseract import pytesseract

def fun():
    img = cv2.imread('img3.jpg', 0)

    crop_1 = img[92:120, 0:650]
    cv2.imwrite('pay.jpg', crop_1)

    crop_2 = img[120:200, 0:650]
    cv2.imwrite('ruppes_in_word.jpg', crop_2)

    crop_3 = img[205:280, 110:370]
    cv2.imwrite('account_no.jpg', crop_3)

    crop_4 = img[250:330, 760:950]
    cv2.imwrite('sign.jpg', crop_4)

    crop_5 = img[19:55, 780:1000]
    cv2.imwrite('date.jpg', crop_5)

    crop_6 = img[150:210, 780:1000]
    cv2.imwrite('rupee_in_digit.jpg', crop_6)

    crop_7 = img[400:, 550:665]
    cv2.imwrite('cheque_no.jpg', crop_7)


    pytesseract.tesseract_cmd = "C:\\Users\\Amresh Ranjan\\Desktop\\WEB DEVLOPS\\Image to Text Project\\tesseract.exe"

    img_1 = cv2.imread("account_no.jpg")
    word_1 = pytesseract.image_to_string(img_1)

    img_2 = cv2.imread("cheque_no.jpg")
    word_2 = pytesseract.image_to_string(img_2)

    img_3 = cv2.imread("date.jpg")
    word_3 = pytesseract.image_to_string(img_3)

    img_4 = cv2.imread("pay.jpg")
    word_4 = pytesseract.image_to_string(img_4)

    img_5 = cv2.imread("rupee_in_digit.jpg")
    word_5 = pytesseract.image_to_string(img_5)

    img_6 = cv2.imread("ruppes_in_word.jpg")
    word_6 = pytesseract.image_to_string(img_6)

    # to save this model in o/p.

    l1 = {'Account Number ' : word_1, 'Cheque Number ' : word_2, 'Date ' : word_3, 
            'Payer ' : word_4, 'Ruppes in Digits ' : word_5, 'Ruppes in Word ' : word_6}
    with open("data.txt", 'w') as f: 
        for key, value in l1.items(): 
            f.write('%s:%s\n' % (key, value))