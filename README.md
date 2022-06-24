# 영화흥행요소 포트폴리오

> 팀원들의 분석결과는 제외  

<br/>

# 💡**주제 선정**

코로나 이후 첫 천만관객 영화인 범죄도시2를 보며 영화를 흥행하게 만드는 흥행요소는 어떤것일지 알아보고자 분석을 진행하였다.



# 🗓프로젝트 기간

**22.05.25 ~ 22.06.20 (15days)**

- 주제 선정 및 기획 설계 : 22.05.25 ~ 22.05.28
- ProDS 특강 : 22.05.30 ~ 22.05.31
- 알고리즘 특강 : 22.06.09 ~ 22.06.10
- 프로젝트 구현 : 22.06.01 ~ 22.06.16
- 산출물 및 발표자료 정리 : 22.06.16 ~ 22.06.19
- 프로젝트 발표 : 22.06.20



# 🔧담당 파트

- 인스타그램 크롤링
- 영화진흥위 데이터 수집
- 인스타그램 데이터 전처리
- 인스타그램 데이터 시각화
- 통합 데이터 분석 및 시각화
- 발표자료 초안 작성



# 💻기술 스택

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src = "https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src = "https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src = "https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"> <img src = "https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white"> <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> <img src="https://img.shields.io/badge/seaborn-0B2C4A?style=for-the-badge&logo=seaborn&logoColor=white">






# 🗂전체 아키택쳐

![Untitled](README.assets/Untitled.png)





# 📋협업관리

> **슬랙, 노션, 줌으로 진행상황 공유**



**노션**

![Untitled](README.assets/Untitled 1.png)



# 🎮**인스타그램 크롤링 과정**

![Untitled](README.assets/Untitled 2.png)



![final_insta_crawling](README.assets/final_insta_crawling.gif)



- Selenium 활용
- 좋아요수와 조회수, 해시태그, 게시글 내용 추출
- 좋아요수가 비공개인 경우 좋아요를 누른 유저수를 추출

# 📊데이터 분석 결과

> 내 파트부분만 정리



## 한국 영화시장

<img src="README.assets/Untitled 3.png" alt="Untitled" style="zoom:50%;" />

- 최근 10년간의 한국영화만 본것
- 최근 10년간 영화관에서 상영한 영화의 갯수는 693개 이며, 이 영화들중 500만 이상의 영화는 49개, 700만 이상은 31개, 천만영화의 경우 14개
- 전체 영화중 소수의 영화들만 흥행한다.



## 코로나 기간의 영화시장

<img src="README.assets/Untitled 4.png" alt="Untitled" style="zoom:50%;" />

- 코로나 기간동안 (2020.04~2022.03) 개봉한 영화들의 흥행 실적
- 코로나 발생기간동안에는 500만 이상으로 흥행한 영화는 없는것으로 나왔다.
- 코로나 기간에는 대부분의 영화가 흥행에 실패한것으로 보인다.



## 흥행요인: 영화 시장의 활성화

여러 흥행요인들중 영화시장의 활성화에 따라 흥행에 영향을 미치는지를 분석

<img src="README.assets/Untitled 5.png" alt="Untitled" style="zoom:50%;" />

<img src="README.assets/Untitled 6.png" alt="Untitled" style="zoom:50%;" />

- 흥행한 영화들의 기준을 누적 관객수 500만 이상으로 잡고 분석한 결과 흥행영화들의 개봉시기는 7,8,12월에 집중되어 있었으며, 흥행이 저조한 영화 (누적관객수 100만 미만)의 경우 11월을 가장 많이 선택했고 8월은 가장 적게 선택한 모습을 볼수있다.

<img src="README.assets/Untitled 7.png" alt="Untitled" style="zoom:50%;" />

- 누적관객수 500만 이상의 영화들은 11월을 가장 적게 선택하는데에 반해 100만 미만의 영화들은 11월을 가장 많이 선택했다.
- 누적관객수 300만 이상의 영화들은 8월을 많이 선택했는데 100만 미만의 영화는 8월을 가장 적게 선택했다.



결론: 영화의 흥행에 자신있다면 7,8,12월을 선택하고, 흥행에 자신이 없다면 4,11월을 선택하는게 좋다.



## 흥행요인 : 러닝타임과 상영기간

<img src="README.assets/Untitled 8.png" alt="Untitled" style="zoom:50%;" />

- 영화의 평균 러닝타임은 약 109분 정도이다.
- 표준편차는 17.05 정도이다.

<img src="README.assets/Untitled 9.png" alt="Untitled" style="zoom:50%;" />

- 대체로 상영시간과 누적관객수는 비례하는 형태를 띄고있다는것을 확인할수있다.
- 누적관객수를 100만 미만으로 보유하고있는 영화의 평균상영시간이 제일 적다는것을 알수있다.

| index | level      | time    |
| ----- | ---------- | ------- |
| 0     | 전체 평균  | 108\.09 |
| 1     | 100만 미만 | 102\.91 |
| 2     | 100~300만  | 116\.12 |
| 3     | 300~500만  | 121\.21 |
| 4     | 500~700만  | 120\.17 |
| 5     | 700만 이상 | 127\.13 |



<img src="README.assets/Untitled 10.png" alt="Untitled" style="zoom:50%;" />

- 전체 컬럼들의 상관관계를 보면 위와 같다.
- 일일 관객수와 일일 매출액의 상관계수가 가장 크다.

<img src="README.assets/Untitled 11.png" alt="Untitled" style="zoom:50%;" />

- 러닝타임과 누적관객수의 상관계수가 0.41로 나왔다.
- 뚜렷한 양적 상관관계를 가진다.
- 즉, 상영시간이 평균러닝타임 이상일경우 러닝타임이 길수록 관객들이 선호한다는 얘기가 된다.
    - 보통의 퀄리티 높은 영화들은 보여줄 내용이 많기에 러닝타임이 길것이므로 결국은 내용이나 퀄리티가 좋아야 흥행한다고 생각한다.
    - 그렇지만 무조건 러닝타임이 길다고해서 모든 영화가 흥행하는것은 아니다.
    

<img src="README.assets/Untitled 12.png" alt="Untitled" style="zoom:50%;" />

- 누적관객수 100만 미만은 대체로 상영기간이 짧다
- 누적관객수 500만 이상의 영화들은 우상향하는 형태를 보인다.



결론 : 러닝타임은 평균 이상으로 하는게 좋고 영화가 흥행을 하고있다면 상영기간을 늘리자.



## 흥행요인 : 출연배우의 영향력

![Untitled](README.assets/Untitled 13.png)

- 인스타그램 크롤링 데이터를 이용해 해시태그를 워드 클라우드로 나타낸 결과 영화에 출연한 배우들이 같이 태그되어있는걸 볼수있다.



결론 : 영화의 흥행에 도움이 될만한 배우를 캐스팅하자



# ⏳한계점 및 아쉬운점

- 프로젝트 일정중에 특강이나 휴강일들이 많아서 실제로 프로젝트를 진행한 기간은 15일 정도인데 기간이 너무 짧아 다양한 분석을 시도해보지 못한게 아쉬웠고
- 영화진흥위에서 스텝에 관한 데이터를 수집해오기 위해 코드를 짜뒀는데 6월 15일 이후부터 수집이 막혀서 스텝 데이터를 분석에 활용하지 못한게 아쉬웠다.
- Spark나 Airflow를 많이 활용하지 못한점도 아쉽다.
- 인스타그램 데이터를 출연배우가 영향력을 미치는지에 관한 워드클라우드로만 활용한점이 아쉽긴했다. 인스타그램에서 락을 걸어둔건지 1000개 이상부터는 크롤링 진행이 안되서 1000개만 크롤링하는걸로 만족해야했다.
- Django를 이용해 웹브라우저를 구현한뒤 브라우저에서 검색어를 입력하면 해당 내용에 관한 인스타 크롤링을 진행하고 그 결과에 대한 워드 클라우드를 보여준다던지 머신러닝을 이용해 최근에 개봉한 영화들이 흥행에 성공할지를 예측하는 모델을 만들어보고싶었는데 프로젝트 기간내에 하기는 힘들어서 포기했는데 아쉽다.
- 카카오톡 챗봇으로 영화의 실시간 예매율이나 좌석점유율 등을 알려주는 서비스를 구현하는것도 해봤으면 좋았을거같다.