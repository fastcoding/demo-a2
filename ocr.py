import cv2
import pytesseract
import sys
import re
def extract_data(fn):
	img=cv2.imread(fn)
	img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	text=pytesseract.image_to_string(img_rgb)
	#print(text)		
	result=re.search(r'CARD\s*N[Oo].\s*([0-9 ]+)'
		+r'\s*Name\s*([a-zA-Z ]*)'
		+r'\s*.*\s*(Breed|Race)\s*([\w ]*)\s*'
		+r'D.*[Bb].*[xX]\s*([\d-]*)\s*'
		+r'(\w)\s*C.*th.*\n(\w+)'
		,text)
	if result is None:
		return 'no match'
	r=result.groups(1)
	return { "card_number": r[0],
		"name":r[1],
		r[2]:r[3],
		"date_of_birth":r[4],
		"gender":r[5],
		"country_of_birth":r[6]
		}

if __name__=='__main__':
	if len(sys.argv)<2:
		print('usage:'+sys.argv[0]+' input/paw_ic1.png')
		sys.exit(0)
	print(extract_data(sys.argv[1]))
	
