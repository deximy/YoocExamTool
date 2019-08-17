from html.parser import HTMLParser
import requests
import json
import os
import re

question_count = 0

class QuestionPage(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.question_id_array = []
 
    def handle_starttag(self, tag, attrs):
        if tag == "div":
            for (variable, value) in attrs:
                if variable == "id":
                    if "question-" in value:
                        self.question_id_array.append(value[-8:])



class AnswerOpinions(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.want_next_data = False
        self.opinions_array = []
 
    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.want_next_data = True
 
    def handle_data(self, data):
        if self.want_next_data:
            self.want_next_data = False
            if "正确答案：" in data:
                opinions = data[5:].split("、")
                self.opinions_array.append(opinions)
             


class AnswerID(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.want_next_data = False
        self.question_value = ""
        self.question_name = ""
        self.opinions_array = []
        self.count = 0
        self.answer_id_array = []
        self.answers_array = []
        self.has_found_correct_answer = False
    
    def handle_starttag(self, tag, attrs):
        if tag == "li":
            for (variable, value) in attrs:
                if variable == "data-question-value":
                    self.want_next_data = True
                    self.question_value = value
                elif variable == "data-question-name":
                    self.want_next_data = True
                    self.question_name = value[0:8]
    
    def handle_data(self, data):
        if self.want_next_data:
            self.want_next_data = False
            if self.count >= 100:
                return
            if data[0] == "A":
                self.has_found_correct_answer = False
            if data[0] in self.opinions_array[self.count]:
                if self.has_found_correct_answer:
                    return
                self.answer_id_array.append(self.question_value)
            if len(self.answer_id_array) == len(self.opinions_array[self.count]):
                self.answers_array.append(self.answer_id_array)
                self.answer_id_array = []
                self.count += 1
                self.has_found_correct_answer = True



def GetLoginInfo():
    print("请输入您的邮箱/爪机号:")
    email = input()
    print("请输入您的密码:")
    password = input()
    print("请输入总题数:")
    question_count = input()
    form_data = {"email": email, "password": password, "remember": True}
    return form_data



def GetCookies():
    login_url = "https://www.yooc.me/login"
    response = requests.get(login_url)
    return_cookie = {}
    for key,value in response.cookies.items():  
        return_cookie[key] = value 
    return return_cookie



def Login(form_data, cookies):
    login_url = "https://www.yooc.me/yiban_account/login_ajax"
    request_headers = {"X-CSRFToken": cookies["csrftoken"]}
    response = requests.post(login_url, data = form_data, headers = request_headers, cookies = cookies)
    return_cookie = {}
    for key,value in response.cookies.items():  
        return_cookie[key] = value 
    return return_cookie



def RepeatExam(cookies):
    exam_url = "https://www.yooc.me/group/39666/exams"
    repeat_url = re.compile("repeat-url=\"(.*?)\"").findall(requests.get(exam_url, cookies = cookies).text)[0]
    request_headers = {"X-CSRFToken": cookies["csrftoken"], "Cookie": "csrftoken=" + cookies["csrftoken"] + "; sessionid=" + cookies["sessionid"]}
    form_data = {"csrfmiddlewaretoken": cookies["csrftoken"]}
    response = requests.post(repeat_url, headers = request_headers, data = form_data, cookies = cookies)



def SubmitAnswer(cookies, answers):
    submit_url = "https://www.yooc.me/group/39666/exam/77777/answer/submit"
    request_headers = {"X-CSRFToken": cookies["csrftoken"], "Cookie": "csrftoken=" + cookies["csrftoken"] + "; sessionid=" + cookies["sessionid"]}
    form_data = {"csrfmiddlewaretoken": cookies["csrftoken"], "answers": json.dumps(answers), "completed": "1", "auto": "0"}
    response = requests.post(submit_url, headers = request_headers, data = form_data, cookies = cookies)



def GetExamPage(cookies):
    exam_url = "https://www.yooc.me/group/39666/exam/77777/detail"
    return requests.get(exam_url, cookies = cookies).text



def ParseQuestion(page):
    parser = QuestionPage()
    parser.feed(page)
    return parser.question_id_array



def BuildAnswer(question_id_array):
    with open(os.path.abspath('.') + "\\answer.txt", 'r') as answer_file:
        answer = json.loads(answer_file.read())
        answers = []
        for question_id in question_id_array:
            answer_chunk = {}
            answer_chunk[question_id] = {}
            answer_chunk[question_id]["1"] = answer.get(question_id, [0])
            answers.append(answer_chunk)
    return answers



def ParseAnswer(page):
    parse = AnswerOpinions()
    parse.feed(page)
    opinions_array = parse.opinions_array
    parse = AnswerID()
    parse.opinions_array = opinions_array
    parse.feed(page)
    return parse.answers_array



def BuildAnswerFile(page):
    with open(os.path.abspath('.') + "\\answer.txt", 'r+') as answer_file:
        question_id_array = ParseQuestion(page)
        answers_array = ParseAnswer(page)
        answer = json.loads(answer_file.read())
        for i in range(0, 99):
            answer[question_id_array[i]] = answers_array[i]
        print("当前题库答案数: " + str(len(answer)))
        answer_file.seek(0)
        answer_file.write(json.dumps(answer))
        if(len(answer) == question_count):
            print("答案已收集完毕，程序退出。")
            exit()



def main():
    cookies = GetCookies()
    form_data = GetLoginInfo()
    cookies = Login(form_data, cookies)
    RepeatExam(cookies)
    page = GetExamPage(cookies)
    question_id_array = ParseQuestion(page)
    answers = BuildAnswer(question_id_array)
    SubmitAnswer(cookies, answers)
    page = GetExamPage(cookies)
    BuildAnswerFile(page)



if __name__ == "__main__":
    main()