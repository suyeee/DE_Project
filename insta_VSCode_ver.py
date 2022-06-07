from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def get_chrome_driver():
    # 1. 크롬 옵션 세팅
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")  # 시크릿모드로 접속
    chrome_options.add_argument("--no-sandbox")  # 대부분의 리소스에 대한 액세스 방지
    chrome_options.add_argument("--disable-setuid-sandbox")  # 크롬 드라이버에 setuid를 하지않음으로써 크롬의 충돌 방지
    chrome_options.add_argument('--disable-dev-shm-usage')  # 메모리 부족으로 인한 에러 방지
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 로그 숨기기

    # 2. driver 생성하기
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
   
    return driver


driver = get_chrome_driver()

# 브라우저 창 한개 더 열기
driver.execute_script('window.open("about:blank", "_blank");')

# 브라우저 인덱스
tabs = driver.window_handles

# 검색어에 대한 링크 추출
def searching_tag(word):
    url = "https://www.instagram.com/explore/tags/" + str(word)
    return url

# 검색후 나온 첫번째 게시글 클릭
def first_click(driver):
    first = driver.find_element(By.CSS_SELECTOR, '._aagw')
    first.click()
    time.sleep(5)
  
# 게시글 내용 추출
def get_content(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
       
    # 본문 내용 추출
    try:
        content = soup.select_one('div._a9zs > span').text
        
    except:
        content = ' '
        
    # 해시태그 추출
    hashtags = re.findall(r'#[^\s#,\\]+', content)
    
    # 작성일자 추출
    date = soup.select('time._aaqe')[0]['datetime'][:10]
    
    # 좋아요수 추출
    # 좋아요수 표시 케이스
    # 1. 좋아요가 한개일때
    # 2. 좋아요수가 없을때
    # 3. 좋아요수를 비공개로 설정해둔 경우
    # 4. 좋아요수가 공개, 2개 이상인 경우
    # 5. 좋아요수는 없고 조회수만 있는 경우
    try:
        # 3번 경우(좋아요수 비공개인것들 처리)
        # 좋아요수 비공개인것들만 실행하도록 필터링
        like_pattern = '여러'
        like = soup.select_one('div._aacl._aaco._aacw._aacx._aada._aade').text
        re.match(like_pattern, like).group()  # error 발생시키기(3번경우가 아닌경우 error 발생)
        
        # 링크 추출
        link = soup.select('._aacl._aaco._aacu._aacx._aad6._aade > a')[1]['href']
        like_link = 'https://www.instagram.com' + str(link)
        
        # 두번째 브라우저 창으로 이동
        driver.switch_to.window(tabs[1])
        driver.get(like_link)
        time.sleep(5)
        
        # 두번째 브라우저의 html 코드 가져오기
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        
        # 좋아요를 누른 유저수 추출
        like = len(soup.select('._aacl._aaco._aacw._aacx._aada._ab58'))
        like = f'좋아요 {like}개'
        view = '조회 0회'
        
        # 다시 메인 브라우저 (첫번째 브라우저로 이동)
        driver.switch_to.window(tabs[0])
        time.sleep(4)
        
    except:
        try:
            # 5번경우
            # 조회수만 추출
            like = '좋아요 0개'
            view = soup.select('div._aacl._aaco._aacw._aacx._aad6._aade')[1].text
        except:
            try:
                # 1,4번 경우
                like = soup.select_one('div._aacl._aaco._aacw._aacx._aada._aade').text
                view = '조회 0회'
            except:
                # 2번 경우
                # 좋아요수, 조회수 둘다 없는 경우
                like = '좋아요 0개'
                view = '조회 0회'

    data = [date, like, view, hashtags, content]
    
    return data

# 다음 게시물 클릭
def move_next(driver):
    right = driver.find_element(By.CSS_SELECTOR, 'div._aaqg._aaqh > ._abl-')
    right.click()
    time.sleep(5)
    
# 슬랙-웹훅으로 크롤링에 걸리는 시간 체크하기
def send_slack(text):
    import requests
    import json
    import datetime

    WEBHOOK_URL = "url"

    # 현재시간도 출력
    now = datetime.datetime.now()
    now = now.strftime("%Y/%m/%d, %H:%M:%S")
    
    # text와 현재시간을 같이 슬랙 메세지로 전송
    text = text + f', 시간: {now}'
    
    payload = {
        'username' : '크롤링봇',
        "text" : text
        }
    
    requests.post(WEBHOOK_URL, json.dumps(payload))
     
    
# 크롤링 시작
send_slack('크롤링 시작')

# 메인 브라우저
driver.switch_to.window(tabs[0])
driver.get('https://www.instagram.com')
time.sleep(3)

# 인스타그램 로그인
email = '인스타그램 로그인 아이디'
input_id = driver.find_elements(By.CSS_SELECTOR, '._2hvTZ')[0]
input_id.clear()
input_id.send_keys(email)

password = '인스타그램 로그인 비번'
input_pw = driver.find_elements(By.CSS_SELECTOR, '._2hvTZ')[1]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()

time.sleep(5)

# 로그인 정보 저장 묻는거
driver.find_elements(By.CSS_SELECTOR, '.sqdOP')[1].click()
time.sleep(3)

# 알림설정 묻는거
driver.find_elements(By.CSS_SELECTOR, '._a9--')[1].click()
time.sleep(3)

# 검색 키워드 입력
word = input("검색어를 입력하세요 : ")
word = str(word)
word_url = searching_tag(word)

# 검색 결과 페이지 열기
driver.get(word_url)
time.sleep(10)


# 첫 번째 게시물 클릭
first_click(driver)

# 데이터 수집
results = []

# 수집할 게시물의 수
target = 10

# def crawling(target):
for i in range(target):
    try:   
        data = get_content(driver)
        print(data)  # 오류를 확인하기 위한 출력
        results.append(data)
        move_next(driver)
        print('next',i)  # 오류를 확인하기 위한 출력
    
    except:
        # 게시글에 사진만있고 글 내용이 아무것도 없는경우
        print('error',i)  # 오류를 확인하기 위한 출력
        time.sleep(5)
        move_next(driver)

    # print(i)  # 오류를 확인하기 위한 출력
      
# # thread
# import threading  
       
# for target in range(10):
#     th = threading.Thread(target=crawling, args=(target, ))
#     th.start()

# 드라이버 종료
driver.quit()

send_slack('드라이버 종료')

# 결과물 저장 
# 지금은 일단 csv로 저장, 나중엔 sql로 저장
import pandas as pd

results_df = pd.DataFrame(results)
# results_df.columns = ['date', 'like', 'view', 'tag', 'content']
# results_df.to_csv('insta.csv')

# SQL로 저장하기
from sqlalchemy import *
# import MySQLdb

HOST = "aws"
DB_USER   = "0000"
DB_PASSWD = "0000"
DB_NAME = "insta"

conn = f"mysql://{DB_USER}:{DB_PASSWD}@{HOST}/{DB_NAME}?charset=utf8"
engine = create_engine(conn, encoding='utf-8')

results_df.to_sql(name='insta_crawling', con=engine, index = False, if_exists='replace')

conn.close()

print('save : ok')  # 오류를 확인하기 위한 출력

send_slack('결과 저장')
