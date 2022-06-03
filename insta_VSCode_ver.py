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
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # 2. driver 생성하기
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
   
    return driver


driver = get_chrome_driver()

def searching_tag(word):
    url = "https://www.instagram.com/explore/tags/" + str(word)
    return url

def first_click(driver):
    first = driver.find_element(By.CSS_SELECTOR, '._aagw')
    first.click()
    time.sleep(5)
  
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
        like_pattern = '여러'
        like = soup.select_one('div._aacl._aaco._aacw._aacx._aada._aade').text
        re.match(like_pattern, like).group()
        
        print('match=ok')  # 오류를 확인하기 위한 출력
        
        # '여러 명'이 좋아합니다. 클릭
        many = driver.find_element(By.CSS_SELECTOR, '._aacl._aaco._aacw._aacx._aada._aade')
        print('click=error')  # 오류를 확인하기 위한 출력
        many.click()
        print('click=ok')  # 오류를 확인하기 위한 출력
        time.sleep(3)
        
        # '좋아요' 목록에서 유저id 추출후 좋아요수 세기
        like = len(soup.select('span._aacl._aaco._aacw._aacx._aad7._aade').text)
        print(like)  # 오류를 확인하기 위한 출력
        like = f'좋아요 {like}개'
        view = 0
        
        # 창 닫기
        close = driver.find_element(By.CSS_SELECTOR, '._ab9y')
        print('close=error')  # 오류를 확인하기 위한 출력
        close.click()
        print('close=ok')  # 오류를 확인하기 위한 출력
        time.sleep(3)

    except:
        try:
            # 5번경우
            like = 0
            view = soup.select('div._aacl._aaco._aacw._aacx._aad6._aade')[1].text
        except:
            try:
                # 1,4번 경우
                like = soup.select_one('div._aacl._aaco._aacw._aacx._aada._aade').text
                view = 0
            except:
                like = 0
                view = 0

    data = [date, like, view, hashtags, content]
    
    return data

# 다음 게시물 클릭
def move_next(driver):
    right = driver.find_element(By.CSS_SELECTOR, 'div._aaqg._aaqh > ._abl-')
    right.click()
    time.sleep(3)
    
# 크롤링 시작
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
print('login success')  # 오류를 확인하기 위한 출력

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
print(word_url)  # 오류를 확인하기 위한 출력

# 검색 결과 페이지 열기
driver.get(word_url)
print('page_open')  # 오류를 확인하기 위한 출력
time.sleep(10)


# 첫 번째 게시물 클릭
first_click(driver)
print('click')  # 오류를 확인하기 위한 출력

# 데이터 수집
results = []

## 수집할 게시물의 수
target = 100
for i in range(target):
    try:   
        data = get_content(driver)
        print(data)  # 오류를 확인하기 위한 출력
        print('data')  # 오류를 확인하기 위한 출력
        results.append(data)
        print('append')  # 오류를 확인하기 위한 출력
        move_next(driver)
        print('next')  # 오류를 확인하기 위한 출력
       
    except:
        print('error')  # 오류를 확인하기 위한 출력
        time.sleep(2)
        move_next(driver)


import pandas as pd

results_df = pd.DataFrame(results)
results_df.columns = ['date', 'like', 'view', 'tag', 'content']
results_df.to_csv('insta.csv')
