import re

clean_Q_text = 'I want to capture and save a number of images from my webcam using OpenCV. This is my code currently:. The problem with this is that I do not know when the images are being taken, so a lot of them end up blurry. My question is: Is there a way to have the image taken on the click of a keyboard key?. Also is there a better way to take multiple images, instead of range?.'

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', clean_Q_text)
# urls = re.findall('http[s]?://stackoverflow.com', text)
print("Original string: ", clean_Q_text, "\n")

if urls:
	print("Urls :", urls)

url_count = len(urls)
print("------------------------------------ Url Count: ", url_count, "\n")  # ------------------------------------------------------------

stack_url_count = 0

for url in urls:
	out = re.findall(r'http[s]?://stackoverflow.com', url)
	if out:
		print("Stack URLs :", out)
		stack_url_count += 1

print("------------------------------------ Stackoverflow Url Count: ", stack_url_count)  # ----------------------------------------------

find = re.findall(".-+.", clean_Q_text)
print(len(find))
dh_count = len(find)

test_clean = re.sub("\s+", " ", clean_Q_text)
print(test_clean)

remained1 = re.sub('[\sA-Za-z0-9]', '', test_clean)
print("All Spe Char :  ", remained1, "\n")
print("Spe Char Count : ", len(remained1))
spe_char_count = len(remained1)  # -------------------------------------------------------------------store into csv file

remained2 = re.sub(r'[`~@#$%^&*\\_+=|>{}\[\]()<\-"]', '', remained1)
#print("remained word :", remained2)
print("Single Punc count : ", len(remained2))

remained3 = re.sub(r'[`~!@#$%^&*\\_+=|><\-\':;?/.,]', '', remained1)
#print("remained word :", remained3)
print("Couple Punc count : ", len(remained3) // 2)
print("Hypen + Dash Count :", dh_count)
punct_count = (dh_count + len(remained2) + len(remained3) // 2)  # -------------------------------------store into csv file

print("------------------------------------ Total Special Char count : ", spe_char_count)
print("------------------------------------ Total Punctuation count : ", punct_count)

up_char = re.findall(r"[A-Z]", clean_Q_text)
print("------------------------------------ Total Upper-case count = ", len(up_char), ":", up_char)
up_char_count = len(up_char)  # ----------------------------------------------------------------------store into csv file

low_char = re.findall(r"[a-z]", clean_Q_text)
print("------------------------------------ Total Lower-case count = ", len(low_char), ":", low_char)
low_char_count = len(low_char)  # --------------------------------------------------------------------store into csv file