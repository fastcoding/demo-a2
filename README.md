OCR Function Demo
======================

This implementation simply uses pytesseract to recognize the text in the picture and then use regular expression to extract all fields. 

For the given 2 pictures, the result is 100% correct. it looks much better than the normal way in that dnn detection is firstly used to find  text region and then call tesseract to recognise it. The EAST algorithm is worse than directly using tesseract to search full picture.

Setup on macbook
-------------------
```shell
  conda install pytesseract opencv
  conda activate
```

Run demo
-------------------
```shell
  python ocr.py input/paw_ic1.png
```

