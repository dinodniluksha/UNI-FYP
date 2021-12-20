from csv import writer
import csv
import re
import textstat


contractions = {
    "I'm": "I am",
    "I'm'a": "I am about to",
    "I'm'o": "I am going to",
    "I've": "I have",
    "I'll": "I will",
    "I'll've": "I will have",
    "I'd": "I would",
    "I'd've": "I would have",
    "Whatcha": "What are you",
    "amn't": "am not",
    "ain't": "are not",
    "aren't": "are not",
    "'cause": "because",
    "can't": "can not",
    "can't've": "can not have",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "daren't": "dare not",
    "daresn't": "dare not",
    "dasn't": "dare not",
    "didn't": "did not",
    "don't": "do not",
    "doesn't": "does not",
    "e'er": "ever",
    "everyone's": "everyone is",
    "finna": "fixing to",
    "gimme": "give me",
    "gon't": "go not",
    "gonna": "going to",
    "gotta": "got to",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "he've": "he have",
    "he's": "he is",
    "he'll": "he will",
    "he'll've": "he will have",
    "he'd": "he would",
    "he'd've": "he would have",
    "here's": "here is",
    "how're": "how are",
    "how'd": "how did",
    "how'd'y": "how do you",
    "how's": "how is",
    "how'll": "how will",
    "isn't": "is not",
    "it's": "it is",
    "'tis": "it is",
    "'twas": "it was",
    "it'll": "it will",
    "it'll've": "it will have",
    "it'd": "it would",
    "it'd've": "it would have",
    "kinda": "kind of",
    "let's": "let us",
    "luv": "love",
    "ma'am": "madam",
    "may've": "may have",
    "mayn't": "may not",
    "might've": "might have",
    "mightn't": "might not",
    "mightn't've": "might not have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "ne'er": "never",
    "o'": "of",
    "o'clock": "of the clock",
    "ol'": "old",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "o'er": "over",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shalln't": "shall not",
    "shan't've": "shall not have",
    "she's": "she is",
    "she'll": "she will",
    "she'd": "she would",
    "she'd've": "she would have",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "so've": "so have",
    "so's": "so is",
    "somebody's": "somebody is",
    "someone's": "someone is",
    "something's": "something is",
    "sux": "sucks",
    "that're": "that are",
    "that's": "that is",
    "that'll": "that will",
    "that'd": "that would",
    "that'd've": "that would have",
    "em": "them",
    "there're": "there are",
    "there's": "there is",
    "there'll": "there will",
    "there'd": "there would",
    "there'd've": "there would have",
    "these're": "these are",
    "they're": "they are",
    "they've": "they have",
    "they'll": "they will",
    "they'll've": "they will have",
    "they'd": "they would",
    "they'd've": "they would have",
    "this's": "this is",
    "those're": "those are",
    "to've": "to have",
    "wanna": "want to",
    "wasn't": "was not",
    "we're": "we are",
    "we've": "we have",
    "we'll": "we will",
    "we'll've": "we will have",
    "we'd": "we would",
    "we'd've": "we would have",
    "weren't": "were not",
    "what're": "what are",
    "what'd": "what did",
    "what've": "what have",
    "what's": "what is",
    "what'll": "what will",
    "what'll've": "what will have",
    "when've": "when have",
    "when's": "when is",
    "where're": "where are",
    "where'd": "where did",
    "where've": "where have",
    "where's": "where is",
    "which's": "which is",
    "who're": "who are",
    "who've": "who have",
    "who's": "who is",
    "who'll": "who will",
    "who'll've": "who will have",
    "who'd": "who would",
    "who'd've": "who would have",
    "why're": "why are",
    "why'd": "why did",
    "why've": "why have",
    "why's": "why is",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "you're": "you are",
    "you've": "you have",
    "you'll've": "you shall have",
    "you'll": "you will",
    "you'd": "you would",
    "you'd've": "you would have"
}


def cont_count(word_bag):
    count = 0
    for word in word_bag:
        if word in contractions:
            count += 1
            print(word)

        elif word.lower() in contractions:
            count += 1
            print(word)

    # print("Number of contractions =", count)
    return count


def search_binary(xs, target):
    """ Find and return the index of key in sequence xs """
    lb = 0
    ub = len(xs)
    while True:
        if lb == ub:  # If region of interest (ROI) becomes empty
            return -1

        # Next probe should be in the middle of the ROI
        mid_index = (lb + ub) // 2

        # Fetch the item at that position
        item_at_mid = xs[mid_index]

        # How does the probed item compare to the target?
        if item_at_mid == target:
            return mid_index  # Found it!
        if item_at_mid < target:
            lb = mid_index + 1  # Use upper half of ROI next time
        else:
            ub = mid_index  # Use lower half of ROI next time


def abbre_count(input_words, available_file):
    input_words.sort(key = lambda x: x.lower())
    print(str(input_words), "\n")

    if input_words:
        count = 0
        temp = []
        abb_temp = []
        start = input_words[0]
        letters_start = re.findall("\A[a-z|A-Z]", start)
        LS = letters_start[0]

        for item in input_words:
            letters_item = re.findall("\A[a-z|A-Z]", item)
            LI = letters_item[0]
            if LS == LI or f"{LS}".lower() == LI or f"{LS}".upper() == LI:
                # print(item)
                temp.append(item)
                # input_words.remove(item)
                # print(temp)
                # point += 1

        with open(available_file, encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = -1

            for row in csv_reader:
                if line_count == -1:
                    line_count += 1
                elif row[0] == f"{LS}".upper():
                    # print(row[1])
                    abb_temp.append(row[1])
                    line_count += 1

        print(LS, ":", temp)

        for word in temp:
            if search_binary(abb_temp, word) != -1:
                print(word)
                count += 1

        print(count, "\n")

        for rem in temp:
            input_words.remove(rem)

        return count + abbre_count(input_words, available_file)

    else:
        return 0


clean_Q_text = "Enter Test Text Here OS"

cont_bag = []
contractions_count = 0
abb_bag = []
abbreviations_count = 0

text = re.sub(r",|\?|\[|\]|<|>|\{|\}|\(|\)", ' ', clean_Q_text)
text = re.sub(r"\.\s+", ' ', text)
print(clean_Q_text, ":", text)

for txt in text.split():
	x = re.search("['a-zA-Z]['a-zA-Z]+", txt)
	if x:
		y = re.findall("'", txt)

		if txt == x.group() and len(y) != 0 and len(y) != len(txt):
			cont_bag.append(txt)
		else:
			# out1 = re.findall("'", txt)
			word = re.findall(r'^[a-zA-Z]+[a-zA-Z`~\-!\\@#$%^&*_+=\.\'|":;/0-9]*$', txt)
			if word:
				abb_bag.append(txt)
	else:
		word = re.findall(r'^[a-zA-Z]+[a-zA-Z`~\-!\\@#$%^&*_+=\.\'|":;/0-9]*$', txt)
		print(word)
		if word:
			abb_bag.append(txt)


print("Contractions Word Bag :", cont_bag)
if cont_bag:
    contractions_count = cont_count(cont_bag)


print("Number of contractions =", contractions_count)

print("Abbreviations Word Bag :", abb_bag)
# print("Abbriations Bag Size :", len(abb_bag))
if abb_bag:
	abbreviations_count = abbre_count(abb_bag, "abbreviations.csv")


print("Number of contractions =", contractions_count)
print("Number of Abbreviations =", abbreviations_count)

print("Total Short Words count =", (contractions_count + abbreviations_count))
