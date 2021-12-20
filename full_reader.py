#coding=utf-8
import csv
import re
import textstat
# import json
import jsonlines

row_list = [['Q-ID', '', 'Title', 'Tags', 'QC Body', '', 'Filtered Question', '', 'Title Length', 'Tag Count', 'Pop Tag Count',
             'Code Lines', 'Code Length', 'Body Length', 'Num Sentences', 'ARI', 'CLI',	'FKF', 'FRE', 'GF',	'SMOG',	'Char Count', 'Num words'
            ]]

row_json = []


def content_length(text):
    add_ele = re.findall("([a-z|A-Z|0-9]\.[a-z|A-Z|0-9]|[a-z|A-Z|0-9]\'[a-z|A-Z|0-9])", text)
    # print(add_ele)
    clean_text = re.sub(r"\W", ' ', text)
    # print(clean_text)
    count1 = len(add_ele)
    count2 = textstat.char_count(clean_text, ignore_spaces=True)
    # print("Content Length : ", count1 + count2)
    return count1 + count2


languages = ['javascript', 'java', 'python', 'c#', 'php', 'android', 'html', 'jquery', 'c++', 'css', 'ios', 'mysql',
             'sql', 'r', 'node.js', 'asp.net', 'arrays', 'c', 'ruby-on-rails', 'json', '.net', 'sql-server',
             'objective-c', 'swift', 'reactjs', 'python-3.x', 'angularjs', 'django', 'angular', 'excel', 'regex',
             'iphone', 'ruby', 'ajax', 'linux', 'xml', 'asp.net-mvc', 'pandas', 'vba', 'spring', 'database',
             'wordpress', 'laravel', 'string', 'wpf', 'xcode', 'windows', 'mongodb', 'typescript', 'vb.net', 'bash',
             'postgresql', 'git', 'oracle', 'multithreading', 'eclipse', 'list', 'amazon-web-services', 'firebase',
             'algorithm', 'macos', 'forms', 'image', 'scala', 'visual-studio', 'azure', 'spring-boot',
             'twitter-bootstrap', 'react-native', 'python-2.7', 'docker', 'function']  # add all languages to this list


with open('insert.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:

            # first-preprocessing
            clean_row = re.sub(r"[\\|]", '~', row[2])

            code_filter = []
            para_len = 0
            code_len = 0

            print(row[0])

            Sline_quesion_code = re.findall(r'<pre.*><code>.*?</code></pre>', clean_row)
            print("Single line codes :", Sline_quesion_code)

            if len(Sline_quesion_code) != 0:
                for Sline_ele in Sline_quesion_code:
                    code_filter.append(Sline_ele)

            row_new1 = re.sub("<pre.*><code>.*?</code></pre>", "", clean_row)

            print("Row New :\n", row_new1)

            question_code = re.findall("<pre.*><code>[>=().,\-:;@#$%^&*\[\]\"'+–/®°⁰!?{}|´`~\w\s]*|.*</code></pre>", row_new1)  # required
            print(question_code)
            row_new2 = re.sub("<pre.*><code>[>=().,\-:;@#$%^&*\[\]\"'+–/®°⁰!?{}|´`~\w\s]*|.*</code></pre>", "", row_new1)  # required

            i = 0
            store = []
            if len(question_code) != 0:
                for part in question_code:
                    full_code = question_code[i] + question_code[i + 1]
                    print(full_code)
                    store.append(full_code)
                    i = i + 2
                    if i == len(question_code):
                        break

            print("combined codes :", store)
            print()

            for chunk in store:
                cln_chunk = re.sub("\n", "", chunk)
                code_len = code_len + len(cln_chunk)
                print(code_len, ":", cln_chunk)

            print()

            bag = []

            for code in store:
                splits = re.findall(r'.*\n*', code)
                print(splits)

                if len(splits) != 0:
                    for split in splits:
                        if split != '':
                            bag.append(split)

            print(bag)

            show = []

            store_req = []
            for statement in bag:
                print(statement)
                inner_ele = re.sub('<pre.*><code>.*|.*</code></pre>', "", statement)
                show.append(inner_ele)  # retriev perpose
                store_req.append(inner_ele)

                store_start = re.findall(r'<pre.*><code>[^\n]+', statement)
                for x in store_start:
                    code_filter.append(x)
                store_end = re.findall(r'.+</code></pre>', statement)
                for y in store_end:
                    code_filter.append(y)

            print(show)

            # print(inner_ele)
            for seg in store_req:
                # store_parts = re.split('\n', seg)
                remo_n = re.sub("\n", "", seg)
                if remo_n != '':
                    code_filter.append(remo_n)

                store_parts = re.findall(r'\n', seg)

                count = 0
                print(store_parts)
                for z in store_parts:
                    if count == 0:
                        count += 1
                    else:
                        code_filter.append(z)

            print(code_filter)
            code_lines = len(code_filter)  # ~~~~~~~~~~~~~~~~~~~~~~ number of line in code part ~~~~~~~~~~~~~~~~~
            print('No of code line =', code_lines)
            print()

            print("Remain Para :\n", row_new2)  # goto paraghap analysis process
            row_new3 = re.sub("<code>|</code>", "", row_new2)

            print("Remain Clean Para :\n", row_new3)

            para_filter = []

            row_new4 = row_new3

            question_para_store = re.findall(r"<p>[>=().,\-:;@#$%^&*\[\]\"'+–/®°⁰!?{}|´`~\w\s]*|.*</p>", row_new4)
            print(question_para_store)

            i = 0
            Mline_question_para = []
            if len(question_para_store) != 0:
                for part in question_para_store:

                    # output = re.findall(r'<p.*>.*?</p>', question_para_store[i])
                    output = re.findall(r'<p>.*?</p>', question_para_store[i])

                    if len(output) != 0:
                        print(question_para_store[i])
                        Mline_question_para.append(question_para_store[i])
                        i = i + 1
                        if i == len(question_para_store):
                            break

                    else:
                        full_para = question_para_store[i] + question_para_store[i + 1]
                        print(full_para)
                        Mline_question_para.append(full_para)
                        i = i + 2
                        if i == len(question_para_store):
                            break

            print("Combined Para Q :", Mline_question_para)

            if len(Mline_question_para) != 0:
                for seg in Mline_question_para:
                    remo_n = re.sub("\n+", ' ', seg)
                    para_len = para_len + len(remo_n)
                    print(para_len, ":", remo_n)
                    para_filter.append(remo_n)

            print("All Question Para :\n", para_filter)
            print()
            print(row_new4)
            print()

            question_ele = []
            for line in para_filter:
                text_1 = re.sub("<p>", "", line)
                text_2 = re.sub("\s*</p>", ".", text_1)
                print(text_2)
                question_ele.append(text_2)

            print(question_ele)
            print(len(question_ele))

            question_text = ' '.join([str(elem) for elem in question_ele])
            print("Full Question Text :\n", question_text)
            print()

            clean_out_1 = re.sub("\s+", " ", question_text)  # removing multiple white spaces
            clean_Q_text = re.sub("<strong>|</strong>", "", clean_out_1)  # removing <strong> tags

            print("Full Clean Question Text :\n", clean_Q_text)
            print()

            if clean_Q_text:

                tags = []

                list_a = re.split('[><]', row[3])

                for seg in list_a:
                    if seg != "":
                        tags.append(seg)  # only store tag attributes
                print(tags)

                tag_count = 0

                for given_tag in tags:
                    bag = []
                    for lang in languages:
                        if given_tag == lang:
                            print(given_tag)
                            # temp.append(row[0]+" : "+given_tag)
                            tag_count += 1

                store = [row[0], '', row[1], row[3], row[2], '', clean_Q_text, '', len(row[1]), len(tags), tag_count, code_lines, code_len, (code_len + para_len),
                         textstat.sentence_count(clean_Q_text),
                         textstat.automated_readability_index(clean_Q_text),
                         textstat.coleman_liau_index(clean_Q_text),
                         textstat.flesch_kincaid_grade(clean_Q_text),
                         textstat.flesch_reading_ease(clean_Q_text),
                         textstat.gunning_fog(clean_Q_text),
                         textstat.smog_index(clean_Q_text),
                         content_length(clean_Q_text),
                         textstat.lexicon_count(clean_Q_text, removepunct=True),
                         ]
                row_list.append(store)

                detail = {"id": row[0], "root": row[0], "text": clean_Q_text}
                row_json.append(detail)

csv.register_dialect('myDialect', delimiter=',', quoting=csv.QUOTE_ALL)

with open('filtered_question_new.csv', 'w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file, dialect='myDialect')
    writer.writerows(row_list)

#use for politenes anlysis task
with open('filtered_question.txt', 'w', encoding="utf-8") as f:
    for item in row_json:
        f.write("{} +++$+++ u0 +++$+++ asking +++$+++ programming +++$+++ {}\n".format(item['id'], item['text']))

