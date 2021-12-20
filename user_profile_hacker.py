import time
import requests
from csv import writer

Question_ID = "34798967"


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='', encoding="utf-8") as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

row_content = ['Question_ID', '', 'Account Age', 'Total Badge Count', 'Negative Badge Count', '', 'Question_Type', 'Answer_Type', 'Score', 'Question_Quality']
append_list_as_row('user-profile_data-final.csv', row_content)

try:
	question_id = Question_ID  # parametre is question id
	print(question_id)

	respo1 = requests.get(f"https://api.stackexchange.com/2.2/questions/{question_id}?order=desc&sort=activity&site=stackoverflow&key=NikmDOJYENcaG2uzN2iCdw((")
	print(respo1.status_code)
	time.sleep(1)

	print("User ID :", respo1.json()['items'][0]['owner']['user_id'])
	user_id = respo1.json()['items'][0]['owner']['user_id']

	respo2 = requests.get(f"https://api.stackexchange.com/2.2/users/{user_id}/questions?order=desc&sort=activity&site=stackoverflow&key=NikmDOJYENcaG2uzN2iCdw((")
	print(respo2.status_code)
	time.sleep(1)

	respo3 = requests.get(f"https://api.stackexchange.com/2.2/users/{user_id}?order=desc&sort=reputation&site=stackoverflow&key=NikmDOJYENcaG2uzN2iCdw((")
	print(respo3.status_code)
	time.sleep(1)

	print("Question Created Date :", respo1.json()['items'][0]['creation_date'])
	print("User Creation Date  :", respo3.json()['items'][0]['creation_date'])

	ques_creation = respo1.json()['items'][0]['creation_date']
	prof_creation = respo3.json()['items'][0]['creation_date']
	print("---------------------------------------------Age of Account :", (ques_creation - prof_creation),
		  'seconds')

	print(respo3.json()['items'][0]['badge_counts'])

	badge_dic = respo3.json()['items'][0]['badge_counts']

	total_badge_count = 0

	for badge in badge_dic:
		# print(badge_dic[badge])
		total_badge_count = total_badge_count + badge_dic[badge]

	print("---------------------------------------------Total Badge Count :", total_badge_count, "\n")

	neg_count = 0

	print(respo2.json()['items'])
	for item in respo2.json()['items']:
		if item['score'] < 0:
			neg_count += 1
			print(item['score'])

	print("---------------------------------------------Negative Score post count :", neg_count, "\n")

	first_dic = respo1.json()['items'][0]
	score = first_dic['score']

except:
	print("Something went wrong")
	#row_detail = [row[0], 'Error']
	#append_list_as_row('remove-id_data-final.csv', row_detail)

else:
	question_type = "Non-Closed"
	question_quality = ""
	answer_type = "NC"

	accepted_answer = "no"

	search_key1 = 'closed_date'
	search_key2 = 'accepted_answer_id'

	if search_key1 in first_dic.keys():
		print("Closed question is detected.\n")
		question_quality = "Very Bad"
		question_type = "Closed"
	elif score < 0:
		print("Bad question is detected.\n")
		question_quality = "Bad"
	elif search_key2 in first_dic.keys():
		print("not a closed question is not Bad")
		answer_type = "AA"  # not a accepted answer
		if 0 < score < 7:
			print("Good question is detected.\n")
			question_quality = "Good"
		else:
			print("Very good question is detected.\n")
			question_quality = "Very Good"
	else:
		print("not accepted answer for question and not Bad\n")
		answer_type = "NAA"  # not a accepted answer

		if score > 0:
			print("Good question is detected.\n")
			question_quality = "Bad"
		else:
			print("Very good question is detected.\n")
			question_quality = "UnDefined"

	print(first_dic, "\n")

	print(question_type, answer_type, score, question_quality)

	if question_quality != "UnDefined":
		row_content = [Question_ID, '', (ques_creation - prof_creation), total_badge_count, neg_count, '', question_type, answer_type, score, question_quality]
		append_list_as_row('user-profile_data-final.csv', row_content)

	else:
		row_detail = [Question_ID, answer_type, score, question_quality]
		append_list_as_row('remove-id_data-final.csv', row_detail)

time.sleep(1)