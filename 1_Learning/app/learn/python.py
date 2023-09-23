import requests


def get_full_name(first_name: str, last_name="insoo"):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def process_times(items: list[str]):
    # print(list(enumerate(items)))  # index, value 형태 변환
    for index, item in enumerate(items, start=1):  # enumerate(리스트 객체, 인덱스 시작 값 설정)
        print(index, item)


def process_item(item: int | str):  # << 3.10 , 3.6+ >> Union[int, str], from typing import Union
    print(item)


def learn_list():
    a = [1, 2, 3, 4, 5]
    print('숫자 리스트: ', a)
    b = ['a', 'b', 'c', 'd', 'e']
    print('문자 리스트: ', b)
    c = [1, 'a', 2, 'b', 3, 'c']
    print('혼합 리스트: ', c)
    d = [[1, 2, 3], [4, 5, 6], 'a', 2, {'name': 'insoo'}]
    print('다중 리스트:', d)


def website_tuple():
    website_list = (
        "kkuisland.com",
        "google.com",
        "https://naver.com",
        "daum.net",
    )
    return website_list


def learn_dict():
    a = {'name': 'insoo', 'age': 30, 'job': 'developer'}
    print('딕셔너리: ', a)
    print('딕셔너리 키: ', a.keys())
    print('딕셔너리 값: ', a.values())
    print('딕셔너리 키/값: ', a.items())


def learn_set():
    a = {1, 2, 3, 4, 5}
    print('숫자 셋: ', a)
    b = {'a', 'b', 'c', 'd', 'e'}
    print('문자 셋: ', b)
    c = {1, 'a', 2, 'b', 3, 'c'}
    print('혼합 셋: ', c)
    d = {1, 2, 3, 4, 5, 5, 5, 5, 5}
    print('중복 셋: ', d)


def request_website():
    websites = website_tuple()
    # r = requests.get('https://google.com', auth=('user', 'pass'))
    # print(r.status_code)
    # print(r.headers['content-type'])
    # print(r.encoding)
    # print(r.text)
    # print(r.json())
    print("🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻 웹 사이트 요청 시작 🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻🏃🏻")
    for website in websites:
        if not website.startswith('https://'):
            website = f"https://{website}"
        response = requests.get(website)
        if response.status_code == 200:
            print(f"{website} is up!")
        else:
            print(f"{website} is down!")
    print("🧎🏻🧎🏻🧎🏻🧎🏻🧎🏻🧎🏻🧎🏻 웹 사이트 요청 완료 🧎🏻🧎🏻🧎🏻🧎🏻🧎🏻🧎🏻🧎🏻")


def learn_scraper():
    print("scraper")


def say_hello():
    print("2. scraper 학습")
    learn_scraper()

    # print("1. list, tuple, dict 학습")
    # learn_list()
    # request_website()  # learn tuple
    # learn_dict()
