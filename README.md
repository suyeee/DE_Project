

<br/>

<div align="center">
    <h1>
        영화 흥행요소 분석 포트폴리오
    </h1>
</div>


<br/>

<div align="center">
    <img src="README.assets/image-20220625000728348.png" alt="image-20220625000728348" width="70%" />
</div>


<br/><br/>

# ✏목차

1. [주제선정](https://github.com/suyeee/DE_Project#%EC%A3%BC%EC%A0%9C-%EC%84%A0%EC%A0%95)

2. [프로젝트 기간](https://github.com/suyeee/DE_Project#%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B8%B0%EA%B0%84)

3. [역할분담](https://github.com/suyeee/DE_Project#%EC%97%AD%ED%95%A0%EB%B6%84%EB%8B%B4)

4. [기술 스택](https://github.com/suyeee/DE_Project#%EA%B8%B0%EC%88%A0-%EC%8A%A4%ED%83%9D)

5. [전체 아키텍쳐](https://github.com/suyeee/DE_Project#%EC%A0%84%EC%B2%B4-%EC%95%84%ED%82%A4%ED%85%8D%EC%B3%90)

   + [ERD](https://github.com/suyeee/DE_Project#erd)

6. [협업 관리](https://github.com/suyeee/DE_Project#%ED%98%91%EC%97%85%EA%B4%80%EB%A6%AC)

7. [데이터 수집 과정](https://github.com/suyeee/DE_Project#%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%88%98%EC%A7%91-%EA%B3%BC%EC%A0%95)

   ​	i. [네이버 영화 크롤링](https://github.com/suyeee/DE_Project#%EB%84%A4%EC%9D%B4%EB%B2%84-%EC%98%81%ED%99%94-%ED%81%AC%EB%A1%A4%EB%A7%81-%EA%B3%BC%EC%A0%95)

   ​	ii. [인스타그램 크롤링](https://github.com/suyeee/DE_Project#%EC%9D%B8%EC%8A%A4%ED%83%80%EA%B7%B8%EB%9E%A8-%ED%81%AC%EB%A1%A4%EB%A7%81-%EA%B3%BC%EC%A0%95)

   ​	iii. [영화진흥위원회 OpenAPI](https://github.com/suyeee/DE_Project#%EC%98%81%ED%99%94%EC%A7%84%ED%9D%A5%EC%9C%84%EC%9B%90%ED%9A%8C-openapi)

8. [데이터 분석결과](https://github.com/suyeee/DE_Project#%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D-%EA%B2%B0%EA%B3%BC)

   ​	i. [한국 영화시장](https://github.com/suyeee/DE_Project#%ED%95%9C%EA%B5%AD-%EC%98%81%ED%99%94%EC%8B%9C%EC%9E%A5)

   ​	ii. [사회적 거리두기 기간의 영화시장](https://github.com/suyeee/DE_Project#%EC%82%AC%ED%9A%8C%EC%A0%81-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%EA%B8%B0%EA%B0%84%EC%9D%98-%EC%98%81%ED%99%94%EC%8B%9C%EC%9E%A5)

   ​	iii. [흥행요인1 : 영화시장의 활성화](https://github.com/suyeee/DE_Project#%ED%9D%A5%ED%96%89%EC%9A%94%EC%9D%B81--%EC%98%81%ED%99%94-%EC%8B%9C%EC%9E%A5%EC%9D%98-%ED%99%9C%EC%84%B1%ED%99%94)

   ​	iv. [흥행요인2 : 러닝타임과 상영기간](https://github.com/suyeee/DE_Project#%ED%9D%A5%ED%96%89%EC%9A%94%EC%9D%B82--%EB%9F%AC%EB%8B%9D%ED%83%80%EC%9E%84%EA%B3%BC-%EC%83%81%EC%98%81%EA%B8%B0%EA%B0%84)

   ​	v. [흥행요인3 : 영화의 평점](https://github.com/suyeee/DE_Project#%ED%9D%A5%ED%96%89%EC%9A%94%EC%9D%B83--%EC%98%81%ED%99%94-%ED%8F%89%EC%A0%90)

   ​	vi. [흥행요인4 : 스크린수](https://github.com/suyeee/DE_Project#%ED%9D%A5%ED%96%89%EC%9A%94%EC%9D%B84--%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%88%98)

   ​	vii. [흥행요인5 : 배급사](https://github.com/suyeee/DE_Project#%ED%9D%A5%ED%96%89%EC%9A%94%EC%9D%B85--%EB%B0%B0%EA%B8%89%EC%82%AC)

   ​	viii. [흥행요인6 : 출연배우](https://github.com/suyeee/DE_Project#%ED%9D%A5%ED%96%89%EC%9A%94%EC%9D%B86--%EC%B6%9C%EC%97%B0%EB%B0%B0%EC%9A%B0)

   ​	ix. [최종결론(범죄도시2에 흥행요인 적용해보기)](https://github.com/suyeee/DE_Project#%EC%B5%9C%EC%A2%85%EA%B2%B0%EB%A1%A0)

9. [한계점 및 아쉬운점](https://github.com/suyeee/DE_Project#%ED%95%9C%EA%B3%84%EC%A0%90-%EB%B0%8F-%EC%95%84%EC%89%AC%EC%9A%B4%EC%A0%90)

<br/><br/><br>

# 💡**주제 선정**

코로나 이후 첫 천만관객 영화인 범죄도시2를 보며 영화를 흥행하게 만드는 흥행요소는 어떤것일지 알아보고자 분석을 진행하였다.

<br/><br/><br>

# 🗓프로젝트 기간

**22.05.25 ~ 22.06.20 (15days)**

- 주제 선정 및 기획 설계 : 22.05.25 ~ 22.05.28
- ProDS 특강 : 22.05.30 ~ 22.05.31
- 알고리즘 특강 : 22.06.09 ~ 22.06.10
- 프로젝트 구현 : 22.06.01 ~ 22.06.16
- 산출물 및 발표자료 정리 : 22.06.16 ~ 22.06.19
- 프로젝트 발표 : 22.06.20

<br/><br/><br>

# 🔧역할분담

<br/>

<div class = 'name'>
    <table>
        <tr>
            <td height="140px" align="center">
            	<img src="README.assets/image-20220626232752925.png" width="200px" /> 
                <br><br>김흥민<br>👑조장
            </td>
        	<td height="140px" align="center">
            	<img src="README.assets/image-20220626232823352.png" width="200px" />
                <br><br>박상권<br>팀원			
            </td>
        	<td height="140px" align="center">
            	<img src="README.assets/image-20220626232759157.png" width="200px" /> 
                <br><br>최진호<br>팀원	
            </td>
        	<td height="140px" align="center"><a href="https://github.com/suyeee">
            	<img src="README.assets/image-20220626232746820.png" width="200px" /> 
                <br><br>황수연<br>팀원</a>
            </td>
        </tr>
        <tr>
            <div class = 'role', align = 'left'>
                <td bgcolor = '#f5f5f5'>
                    <ul>
                        <li>네이버영화 사이트 크롤링</li>
                        <li>네이버 영화 데이터 전처리</li>
                        <li>MySQL 파이프라인 구축</li>
                        <li>통합 데이터 분석 및 시각화</li>
                        <li>발표자료 편집</li>
                    </ul>
                </td>
                <td bgcolor = '#f5f5f5'>
                    <ul>
                        <li>네이버영화 사이트 크롤링</li>
                        <li>네이버 영화 데이터 전처리</li>
                        <li>MySQL 파이프라인 구축</li>
                        <li>통합 데이터 분석 및 시각화</li>
                        <li>발표자료 편집</li>
                    </ul>
                </td>
                <td bgcolor = '#f5f5f5'>
                    <ul>
                        <li>인스타그램 크롤링</li>
                        <li>영화진흥위 데이터 수집</li>
                        <li>영화진흥위 데이터 전처리</li>
                        <li>통합 데이터 분석 및 시각화</li>
                        <li>발표자료 편집</li>
                    </ul>
                </td>
                <td bgcolor = '#f5f5f5'>
                    <ul>
                        <li>인스타그램 크롤링</li>
                	    <li>영화진흥위 데이터 수집</li>
                	    <li>인스타그램 데이터 전처리</li>
                	    <li>인스타그램 데이터 시각화</li>
                	    <li>통합 데이터 분석 및 시각화</li>
                	    <li>발표자료 초안 작성</li>
                    </ul>
                </td>
            </div>
        </tr>
    </table>
</div>

<br/><br/><br/><br><br>

# 💻기술 스택

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src = "https://img.shields.io/badge/json-000000?style=for-the-badge&logo=json&logoColor=white"> <img src = "https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"> <img src = "https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white"> <img src = "https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white"> <img src = "https://img.shields.io/badge/VSCode-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white"> <img src = "https://img.shields.io/badge/colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white"> <img src = "https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white">

<img src = "https://img.shields.io/badge/spark-E25A1C?style=for-the-badge&logo=Apache Spark&logoColor=white"> <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> <img src = "https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=Amazon AWS&logoColor=white"> <img src="https://img.shields.io/badge/seaborn-0B2C4A?style=for-the-badge&logo=seaborn&logoColor=white"> <img src="https://img.shields.io/badge/slack-4A154B?style=for-the-badge&logo=slack&logoColor=white">

<br/><br/><br><br><br>

# 🗂전체 아키텍쳐

![Untitled](README.assets/Untitled.png)

<br/><br/><br>

## ERD

<br>

![image-20220627012128299](README.assets/image-20220627012128299.png)

<br><br><br><br><br>

# 📋협업관리

> **슬랙, 노션, 줌으로 진행상황 공유**

<br/>

**노션**

<img src="README.assets/Untitled 1.png" alt="Untitled" style="zoom:50%;" />

<br/><br/>

# 🧲데이터 수집 과정

> **네이버 영화 크롤링 과정**
>
> **인스타그램 크롤링 과정**
>
> **영화진흥위원회 OpenAPI 수집 과정**

<br><br><br>

## 네이버 영화 크롤링 과정

1. 영화 코드번호 수집

![image-20220627012406770](README.assets/image-20220627012406770.png)

<br><br><br><br>

![image-20220627013445344](README.assets/image-20220627013445344.png)

<br><br><br><br>

![image-20220627013625033](README.assets/image-20220627013625033.png)

+ 위 과정을 반복하는 코드를 작성

<br><br><br><br>

![image-20220627013831968](README.assets/image-20220627013831968.png)

<br><br><br><br>

2. 영화별 세부데이터 수집

![image-20220627014500314](README.assets/image-20220627014500314.png)

<br><br><br><br><br>

## 인스타그램 크롤링 과정

<br>

<div align='center'>
    <img src="README.assets/Untitled 2.png" alt="Untitled" width="50%" />
</div>
<br/><br/><br><br>

![image-20220627015200840](README.assets/image-20220627015200840.png)

<br>

+ 함수 6개를 만든다.
  + 인스타그램을 크롤링하기위해 크롬에 대한 옵션세팅과 드라이버를 생성하는 함수
  + 검색어에 대한 링크를 호출해주는 함수
  + 검색후 나온 첫번째 게시글을 클릭해주는 함수
  + 게시글의 내용을 추출해주는 함수
  + 다음 게시글을 클릭해주는 함수
  + 크롤링하는데 걸리는 시간 측정을 위해 슬랙으로 진행상황과 시간을 같이 보내주는 함수

<br><br><br><br>

![image-20220627015909460](README.assets/image-20220627015909460.png)

<br>

+ 드라이버를 실행시키면 슬랙으로 '크롤링 시작' 메시지와 함께 현재날짜와 시간이 같이 전송됨.
+ 드라이버 실행후엔 인스타그램 로그인을 하고 검색어를 입력하게 해주는 input 함수가 실행됨. 검색할 검색어를 터미널에 입력을 해주게 되면 사전에 만들어둔 함수로 인해 해당 검색어에 대한 링크가 호출된다.
+ 검색어에 대한 링크로 페이지가 이동되면 해당 페이지의 첫번째 게시글을 클릭을 한 후 게시글 내용을 추출해주는 함수로 인해 게시글 내용이 추출된다.
  + 게시글 내용 : 좋아요수, 조회수, 해시태그, 해시태그를 포함한 전체 게시글 내용
+ 첫번째 게시글에 대한 추출이 끝나면 다음페이지로 이동하는 버튼을 클릭하여 이동하는데 이동하고 나서부턴 for 문에 의해 원하는 게시글의 갯수에 맞게 for문이 실행된다.
+ 게시글 수집이 전부 완료되면 자동으로 드라이버가 종료되고 '드라이버 종료' 메세지와 함께 현재날짜와 시간이 같이 출력. 그 후에는크롤링한 결과물을 csv로 저장하거나 MySQL 데이터베이스에 저장하는데 저장이 완료되면 마찬가지로 슬랙에 '결과 저장' 메시지와 날짜, 시간이 같이 전송된다.

<br><br><br><br>

<div align = 'center'>
    <img src="README.assets/image-20220627020839912.png", width=70% /><br><br>
    <p>
        <
        slack으로 온 메세지 (진행상황, 날짜, 시간)>
    </p>
</div>

<br><br><br><br><br>

### 인스타그램 크롤링 과정 영상

![final_insta_crawling](README.assets/final_insta_crawling.gif)

<br>

- Selenium 활용
- 좋아요수와 조회수, 해시태그, 게시글 내용 추출
- 좋아요수가 비공개인 경우 좋아요를 누른 유저수를 추출

<br/><br/><br><br>

## 영화진흥위원회 OpenAPI

1. 데이터 수집 요청

![image-20220627022356708](README.assets/image-20220627022356708.png)

<br><br><br><br><br>

2. 영화별 세부데이터 수집

![image-20220627022600180](README.assets/image-20220627022600180.png)

<br><br><br><br><br><br>

# 📊데이터 분석 결과

<br/>

## 한국 영화시장

<br/>

<div align = 'center'>
    <img src="README.assets/Untitled 3.png" alt="Untitled" width="60%" />
</div>

 <br/>

- 최근 10년간의 한국영화만 본것
- 최근 10년간 영화관에서 상영한 영화의 갯수는 693개 이며, 이 영화들중 500만 이상의 영화는 49개, 700만 이상은 31개, 천만영화의 경우 14개
- 전체 영화중 소수의 영화들만 흥행한다.

<br/><br/>

## 사회적 거리두기 기간의 영화시장

<br/>

<div align = 'center'>
    <img src="README.assets/Untitled 4.png" alt="Untitled" width="60%" />
</div>

<br/>

- 코로나 기간동안 (2020.04~2022.03) 개봉한 영화들의 흥행 실적
- 코로나 발생기간동안에는 500만 이상으로 흥행한 영화는 없는것으로 나왔다.
- 코로나 기간에는 대부분의 영화가 흥행에 실패한것으로 보인다.

<br/><br/>

## 흥행요인1 : 영화 시장의 활성화

> **여러 흥행요인들중 영화시장의 활성화에 따라 흥행에 영향을 미치는지를 분석**

<br/>

<div align = 'center'>
    <표 : 연도별 영화 개봉수><br>
    <img src="README.assets/image-20220628231827456.png" alt="Untitled" width="60%" />
</div>

<br>

- 대체로 비슷한 개봉수를 보인다.
- 개봉 횟수와 작품의 흥행은 항상 비례하지는 않는다.

<br><br><br>

<div align = 'center'>
    <img src="README.assets/image-20220628232446127.png" alt="Untitled" width="60%" />
</div>

<br>

- 코로나로 인한 사회적거리두기 시기인 2020년도 이후를 제외하고 보면 대체로 1억명대의 관객수를 유지하고있다.
- 즉, 영화의 활성화 정도는 영화흥행에 영향을 주지않는다. 

<br><br><br>

<div align = 'center'>
    <표 : 연도별 흥행도><br>
    <img src="README.assets/image-20220628232944729.png" alt="Untitled" width="60%" />
</div>

<br>

- 영화시장이 부진한 해 : 12, 14, 19년
- 영화시장이 흥행한 해 : 13, 16년

<br><br>

그렇다면 영화 시장이 활성화가 되는 특정 시기가 존재할까?

<br><br><br>

<div align = 'center'>
    <img src="README.assets/Untitled 5.png" alt="Untitled" width="60%" />
    <br/><br/>
    <img src="README.assets/Untitled 6.png" alt="Untitled" width="60%" />
    <br><br><br>
    <표 : 10년간 월별로 개봉한 영화수의 합계 (흥행영화 vs 흥행저조 영화)>
</div>


<br/>

- 흥행한 영화들의 기준을 누적 관객수 500만 이상으로 잡고 분석한 결과 흥행영화들의 개봉시기는 7,8,12월에 집중되어 있었으며, 흥행이 저조한 영화 (누적관객수 100만 미만)의 경우 11월을 가장 많이 선택했고 8월은 가장 적게 선택한 모습을 볼수있다.

<br/><br/><br/>

<div align = 'center'>
    <img src="README.assets/Untitled 7.png" alt="Untitled" width="70%" />
</div>

<br/>

- 누적관객수 500만 이상의 영화들은 11월을 가장 적게 선택하는데에 반해 100만 미만의 영화들은 11월을 가장 많이 선택했다.
- 누적관객수 300만 이상의 영화들은 8월을 많이 선택했는데 100만 미만의 영화는 8월을 가장 적게 선택했다.

<br/><u>결론: 영화의 활성화 정도는 영화의 흥행에 영향을 주지않으며, 영화의 흥행에 자신있다면 7,8,12월을 선택하고, 흥행에 자신이 없다면 4,11월을 선택하는게 좋다.</u>

<br/><br/>

## 흥행요인2 : 러닝타임과 상영기간

> **러닝타임과 상영시간이 영화의 흥행에 영향을 미치는지를 분석**

<br/>

<div align = 'center'>
    <img src="README.assets/Untitled 8.png" alt="Untitled" width="60%" />
</div>

<br/>

- 영화의 평균 러닝타임은 약 109분 정도이다.
- 표준편차는 17.05 정도이다.

<br/><br/>

<div align = 'center'>
    <img src="README.assets/Untitled 9.png" alt="Untitled" width="60%"/>
</div>

<br/>

- 대체로 상영시간과 누적관객수는 비례하는 형태를 띄고있다는것을 확인할수있다.
- 누적관객수를 100만 미만으로 보유하고있는 영화의 평균상영시간이 제일 적다는것을 알수있다.

<br/><br/>

<div align = 'center'>
    <table border='1'>
        <thead>
            <tr>
                <th>audience</th>
                <th>time</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>전체 평균</td>
                <td>108.09</td>
            </tr>
            <tr>
                <td>100만 미만</td>
                <td>102.91</td>
            </tr>
            <tr>
                <td>100~300만</td>
                <td>116.12</td>
            </tr>
            <tr>
                <td>300~500만</td>
                <td>121.21</td>
            </tr>
            <tr>
                <td>500~700만</td>
                <td>120.17</td>
            </tr>
            <tr>
                <td>700만 이상</td>
                <td>127.13</td>
            </tr>
        </tbody>
    </table><br/>
    <p>
        <표 : 누적 관객수에 따른 영화의 평균 러닝타임(DataFrame)>
    </p>
</div>
<br/><br/><br/>

<div align = 'center'>
    <img src="README.assets/Untitled 10.png" alt="Untitled" width="65%" />
</div>

<br/>

- 컬럼명 ''상영시간'' =  러닝타임을 의미함.
- 전체 컬럼들의 상관관계를 보면 위와 같다.
- 일일 관객수와 일일 매출액의 상관계수가 가장 크다.

<br/><br/><br>

러닝타임과 누적관객수, 둘의 상관관계를 확인해보면

<br><br><br>

<div align = 'center'>
    <img src="README.assets/Untitled 11.png" alt="Untitled" width="50%" />
</div>

<br/>

- 러닝타임과 누적관객수의 상관계수가 0.41로 나왔다.
- 뚜렷한 양적 상관관계를 가진다.
- 즉, 상영시간이 평균러닝타임 이상일경우 러닝타임이 길수록 관객들이 선호한다는 얘기가 된다.
    - 보통의 퀄리티 높은 영화들은 보여줄 내용이 많기에 러닝타임이 길것이므로 결국은 내용이나 퀄리티가 좋아야 흥행한다고 생각한다.
    - 그렇지만 무조건 러닝타임이 길다고해서 모든 영화가 흥행하는것은 아니다.
    

<br/><br/>

<div align = 'center'>
    <img src="README.assets/Untitled 12.png" alt="Untitled" width="60%" />
</div>

<br/>

- 누적관객수 100만 미만은 대체로 상영기간이 짧다
- 누적관객수 500만 이상의 영화들은 우상향하는 형태를 보인다.

<br/>

<u>결론 : 러닝타임은 평균 이상으로 하는게 좋고 영화가 흥행을 하고있다면 상영기간을 늘리자.</u>

<br/><br/>

## 흥행요인3 : 영화 평점

> **영화의 평점이 흥행에 영향을 미치는지를 분석**

<br>

<div align = 'center'>
    <누적관객수별 평점의 평균을 나타낸것><br><br>
    <img src="README.assets/image-20220628235407190.png" alt="Untitled" />
</div>

<br>

+ 전체적으로 관람객수가 많은 영화일수록 평점의 평균이 올라가고 있다.
+ 우측의 버블차트로도 동일한 내용을 확인할수있다.
+ 우측의 버블차트를 보면 누적관객수가 100만 이하인 영화들중에서 높은 평점을 받은 영화들도 꽤 있는걸로 보아 평점이 높다고 해서 무조건 흥행하는것은 아니란걸 알수있다.

<br><br><br>

영화의 평점과 누적관객수의 상관관계를 확인해보면

<br><br>

<div align = 'center'>
    <img src="README.assets/image-20220628235850979.png" alt="Untitled" width="60%" />
</div>

<br>

+ 누적관객수와 영화의 평점은 아주 약한 양의 상관관계를 가진다.

<br><br>

<u>결론 : 영화의 평점이 높다고 해서 영화가 흥행하는것은 아니다.</u> 

<br><br>

## 흥행요인4 : 스크린수

> **영화가 개봉된 후 영화관에서 상영을 할때 스크린수가 많다면 흥행에 유리할것인지를 분석한다**

<br>

<div align = 'center'>
    <img src="README.assets/image-20220629232414412.png" alt="Untitled" width="60%" />
</div>

<br>

+ 파란색으로 표시된 막대그래프는 전체영화의 평균 스크린수를 나타낸것이며, 그 수는 9724개로 대략 만개 정도이다.
+ 누적관객수가 증가함에 따라 스크린수도 증가하는것을 알수있다.
+ 수집한 데이터만으로 이러한 현상의 인과관계를 명확히하기는 어려우나(영화가 흥행을 하고있어서 스크린을 많이 확보해준것인지 스크린을 많이 확보했기때문에 영화가 흥행한것인지 등등) 영화관에서 스크린수를 많이 제공한다하더라도 관객입장에선 영화가 재미가 없었다면 700만 이상으로 흥행하기는 어려웠을것이므로 스크린수 확보도 중요하지만 관객을 사로잡을수 있을만한 영화를 만들어야 흥행에 성공할것이다.

<br><br><br>

그렇다면 혹시 청소년 관람불가 등급의 영화도 앞서나온 현상 (누적관객수가 증가함에 따라 스크린수도 증가한다)이 적용이 될까?

<br><br>

<div align = 'center'>
    <img src="README.assets/image-20220629233533019.png" alt="Untitled"/>
</div>

<br>

+ 청소년 관람불가 등급의 영화는 연령제한으로 인해 최근 10년 기준, 관객수가 500만 이상인 영화가 없으므로 조금 더 정확한 비교를 위해 전체 영화의 평균을 기준으로 각각의 비율을 막대그래프로 나타내었다.
+ 청불 그룹의 경우 250만 이상이면 흥행한 영화로 보고 분석을 진행하였다.
+ ''청불 제외'' 그룹에서 300만 이상으로 흥행한 영화들의 스크린 비율은 평균보다 2.4~3.6배 높게 나타났고 ''청불'' 그룹에서 250만 이상 흥행한 영화들의 스크린 비율은 평균보다 3.4배 높게 나타났다.
+ 흥행한 영화들 그룹은 보통 평균보다 약 3배 정도 높은 스크린수 비율을 보였으며 스크린수가 많을수록 영화의 흥행에 어느정도 도움을 준다고 판단할수있다.

<br><br><br>

<div align = 'center'>
    <img src="README.assets/image-20220630233308905.png" alt="Untitled" width="90%" />
    <br><br>
    <흥행영화(관객수 500만 이상)기준, 누적관객수와 누적스크린수의 상관관계를 나타낸것>
</div>

<br>

+ 흥행영화들만 봤을시 관객수와 스크린수의 상관계수는 `0.79`로 강한 양의 상관관계를 가지고 있다는것을 알수있다.

<br><br>

흥행이 저조한 영화의 경우

<br><br><br>

<div align = 'center'>
    <img src="README.assets/image-20220630233953407.png" alt="Untitled" width="90%" />
    <br><br>
    <흥행저조 영화(관객수 100만 미만)기준, 누적관객수와 누적스크린수의 상관관계를 나타낸것>
</div>

<br>

+ 흥행이 저조한 영화들의 경우에도 흥행에 성공한 영화들과 마찬가지로 상관계수가 높게 나타났다.
+ 흥행저조 영화의 관객수와 스크린수의 상관계수는 `0.69`로 높은 상관관계를 가짐.
+ 흥행저조 영화들의 관객수와 스크린수간의 상관관계가 높다는 의미는 스크린수가 적으면 적을수록 영화의 흥행은 쉽지않을거란 의미로 해석할수있다.
+ 즉, 스크린수는 영화의 흥행요인이라고 판단할수있다.

<br><br><br>

<div align = 'center'>
    <img src="README.assets/image-20220701231859449.png" alt="Untitled" width="60%" />
    <br><br>
    <청소년관람불가 등급의 영화들을 제외한 영화들에대한 누적관객수와 누적스크린수를 나타낸 그래프>
</div>

<br>

+ 산점도 그래프에서 관객수와 스크린수는 모든 분류에서 강한 양의 상관관계를 나타내고있다.

<br><br><br>

<u>결론 : 스크린수도 영화의 흥행에 영향을 미치는것으로 판단할수있다. 그러므로 영화의 흥행을 위해서는 스크린수를 확보하는것도 중요하다!</u>

<br><br><br>

스크린수를 많이 확보하기위해선 배급사의 영향도 무시할수없을것이다. 그래서 배급사는 어느정도의 영향력을 지니고있는지에 대해서도 분석을 진행하였다.

<br><br>

## 흥행요인5 : 배급사

>**배급사가 영화의 흥행에 영향을 주는지 분석한다.**

<br>

<div align = 'center'>
    <img src="README.assets/image-20220701232840497.png" alt="Untitled" width="60%" />
    <br><br>
    <전체 배급사들이 배급한 영화의 비율에 대한 파이차트>
</div>

<br>

- 파이차트의 절반 가까이를 차지한건 유명한 4대 배급사이다.
- 4대 메이저 배급사는 'CJ ENM', '롯데', 'NEW', '(주)쇼박스' 이다.
- 전체 배급사 시장에서 4대 배급사의 점유율은 41.3% 정도이다.

<br><br><br>

4대 배급사가 배급하는 영화의 수를 살펴보면

<br><br>

<div align = 'center'>
    <img src="README.assets/image-20220701233503612.png" alt="Untitled" width="60%" />
</div>

<br>

- 최근 10년간의 데이터를 기준으로 분석하였으며 4대 배급사의 누적관객수별 배급영화수를 나타낸것이다.
- 4대 메이저 배급사들이 10년간 배급한 영화들중 실제 상영한 영화는 평균적으로 80건 정도 된다.
- 4대 배급사 중 가장 많이 영화를 배급한건 'CJ ENM' 이다.

<br><br><br>

4배 배급사의 관객수 비율을 보면

<br><br>

<div align = 'center'>
    <img src="README.assets/image-20220701234039827.png" alt="Untitled" width="90%" />
    <br><br><br>
    <img src="README.assets/image-20220701234312779.png" alt="Untitled" width="90%" />
    <br><br>
    <왼쪽 위부터 순서대로 파란색: CJ,  빨간색: 롯데,  보라색: NEW,  주황색: 쇼박스>
</div>

<br>

- 관객수 500만 이상으로 흥행한 영화의 비율은 CJ 는 19%, 쇼박스는 16.7%, NEW는 11.4%, 롯데는 8.6% 였으며 누적관객수 300만 이상의 영화들까지 범위를 확대하면 4대 배급사들이 배급한 영화들의 상당수가 영화 흥행에 성공했다는것을 알수있다.

<br><br><br>

흥행한 영화들이 선택한 배급사들을 확인해보았다.

<br><br>

<div align = 'center'>
    <img src="README.assets/image-20220704231951941.png" alt="Untitled" width="90%" />
</div>

<br>

- 최근 10년 기준의 데이터 이며, 흥행영화의 기준은 누적관객수 500만 이상으로 설정하였다.
- 흥행한 영화의 88.1% 가 4대 배급사를 통해 영화를 배급한것을 확인할수있다. 하나의 영화에 여러개의 배급사가 존재하는경우를 제외하면 퍼센트는 더욱 늘어날것이다.
- 중소 배급사에서 누적관객수 500만 이상으로 흥행한 영화는 4개이다. 
  - 범죄도시1, 2, 밀정, 백두산 등

<br><br><br>

그렇다면 4대 배급사는 영화시장을 얼마나 장악하고 있을까?

<br><br>

<div align = 'center'>
    <img src="README.assets/image-20220707232751106.png" alt="Untitled" width="90%" />
</div>

<br>

+ 4대 배급사가 보급하는 스크린 수는 다른 배급사들에 비해 약 2.9배 높다.

<br><br><br>

4배 배급사마다 주로 배급하는 특정 장르가 있을것이다. 

<br><br>

<div align = 'center'>
    <img src="README.assets/image-20220707233319633.png" alt="Untitled" width="50%" />
</div>

<br>

- 가장 많이 배급하는 장르는 '드라마' 다.
- '드라마' 다음으로 4대 배급사가 주로 배급한 장르는 CJ ENM 과 쇼박스는 범죄와 액션, NEW는 애니메이션과 코미디, 롯데는 코미디와 멜로/로맨스 쪽의 장르를 주로 배급했다.
- 4대 배급사 모두 드라마, 액션, 범죄, 코미디 장르가 많은 지분을 차지하고있다.
- 같은 4대 배급사라 하더라도 각 배급사마다 배급장르의 선호도 차이가 존재하는것으로 보인다.

<br><br>

4대 배급사들의 주 배급장르는 약간씩은 다르지만 공통적으로는 모두 드라마, 액션, 범죄, 코미디 장르가 많은 지분을 차지하고있었다. 그건 대중성 때문일까? 

<br><br>

드라마, 액션, 범죄, 코미디 장르가 대중성이 있어 흥행에 영향을 미치는지를 알아보기 위해, 누적관객수 500만 이상을 찍은 영화들의 모든 장르를 확인해보았다.

<br><br>

<div align = 'center'>
    <img src="README.assets/image-20220707234601730.png" alt="Untitled" width="60%" />
</div>

<br>

- 최근 10년 기준 누적관객수 500만 이상의 영화는 총 49개
- 네이버 영화에 등록된 장르의 갯수는 총 26개이나 누적관객수 500만 이상 영화들의 장르만 확인해보면 높은 비율을 차지하고 있는건 드라마, 액션, 범죄, 코미디다.
- 4대 배급사는 대중성이 있는 장르에 특히 더 큰 투자를 하고 있다는 점을 확인할수있었다.

<br>

<u>결론: 영화를 흥행시키고 싶다면 4대 배급사의 파워를 무시할수없다. 4대 배급사별 주 배급장르를 확인하여 영화의 장르와 잘 맞는 배급사를 선택하자.</u>

<br><br>

## 흥행요인6 : 출연배우

> **영화에 출연하는 배우가 영화의 흥행에 영향을 미치는지 분석한다.**

<br>

<div align = 'center'>
    <img src="README.assets/image-20220709230655880.png" alt="Untitled" width="90%" />
    <br><br>
    <천만배우들 중 3회이상 천만관객 영화에 출연한 배우(파이차트), 작품횟수(막대그래프)>
</div>

<br>

- 막대그래프는 3회이상 1000만 영화에 출연한 영화배우를 기준으로 삼아 특정 배우들을 뽑아낸 후 누적관객수 500만 이상의 영화에 출연한 횟수를 나타냈다.

- 누적관객수 500만 이상의 영화 출연진으로 하면 너무 많아 추리기가 힘드므로 천만영화에 3회이상 출연한 배우들을 확인하였고 그 결과 9명의 배우를 확인할수있었다.

- 추려진 특정 배우들이 출연한 작품들중에 누적관객수가 500만 이상이였던 영화의 비율이 높아 막대그래프에 500만 이상의 작품에 출연한 횟수를 비교 그래프로 넣어 시각화하였다.

- 누적관객수 500만 이상의 작품 비율은 오달수 50%, 류승룡 30% 송강호 63% 하정우는 57%, 마동석 23%<br>

  라는 결과 값이 도출되었고, 이처럼 배우는 영화 흥행에 있어서 큰 영향을 미친다는 점을 확인할수있었다.

<br><br>

위 결과로 인해 특정 몇 배우들은 ''흥행보증수표'' 라는 수식어가 붙기도한다.

<br><br>

출연배우들의 영향력을 확인하기위해 인스타 크롤링 결과물을 이용해 워드클라우드를 만들었다.

<br><br><br>

<div align = 'center'>
    <img src="README.assets/Untitled 13.png" alt="Untitled" width="90%" />
    <br><br>
    <출연배우의 영향력을 알아보기 위해 최근개봉 영화들중 1000만 관객수를 돌파한 범죄도시2를 키워드로 인스타그램을 크롤링한것>
</div>

<br>

- 인스타그램 크롤링 데이터를 이용해 해시태그를 워드 클라우드로 나타낸 결과 영화에 출연한 배우들이 같이 태그되어있는걸 볼수있다.

<br/>

<u>결론 : 영화의 흥행에 도움이 되는 배우를 캐스팅한다면 영화가 흥행할 확률이 높아질것이다.</u>

<br/><br/><br>

## 최종결론

> **'영화의 흥행요소 분석 '이라는 주제선정을 하게 만든 영화인 '범죄도시2' 에 지금까지 분석한 흥행요인들을 적용시켜본다.**

<br>

<div>
    <img src="README.assets/image-20220709233500416.png" alt="Untitled" width="70%" align ='left'/>
</div>

<br>

흥행요인 1 : 영화시장 활성화 x 

흥행요인 2-1 : 러닝타임 x

흥행요인 2-2 : 상영기간 o

흥행요인 3 : 영화평점 o 

흥행요인 4-1 : 스크린 수 o

흥행요인 4-2 : 관람등급 o

흥행요인 5-1 : 배급사 x

흥행요인 5-2 : 장르 o

흥행요인 6 : 출연배우 o

<br><br><br><br><br>

- 개봉시기는 흥행에 성공한 영화들이 흔히 선택하는 월은 아니였다.
- 영화의 러닝타임 또한 평균 러닝타임(109분)에 근접한 것을 보인다.
- 영화 평점은 높은 평점을 띄고 있다.
- 관람등급은 청소년 관람불가가 아니었으며, 배급사는 4대 배급사는 아니었으나 그 다음으로 가장 유명한 메가박스 배급사로 확인되었다.
  - 그로인해 스크린 수는 상당히 많은 지분을 차지하고 있었다.
- 영화의 장르는 대중성이 있는 범죄,액션 장르이다.
- 출연 배우 또한 앞서 분석한 유명 배우 마동석이 출연하였고, 최근 인기 절정인 손석구 배우도 출연하고 있는 모습을 볼 수 있다.

<br><br>

<u>결론 : 분석하였던 흥행 요소들이 맞는 경우도 상당히 존재했고, 적용되지 않는 경우도 있었다. 최근 코로나 제한 이후 500만 이상 영화가 나오지 않았으나, 이 영화에 대한 큰 관심을 시작으로, 앞으로의 영화 시장을 기대해보아도 좋을 것같다.</u>

<br><br><br>

# ⏳한계점 및 아쉬운점

- 프로젝트 일정중에 특강이나 휴강일들이 많아서 실제로 프로젝트를 진행한 기간은 15일 정도인데 기간이 너무 짧아 다양한 분석을 시도해보지 못한게 아쉬웠고
- 영화진흥위에서 스텝에 관한 데이터를 수집해오기 위해 코드를 짜뒀는데 6월 15일 이후부터 수집이 막혀서 스텝 데이터를 분석에 활용하지 못한게 아쉬웠다.
- Spark나 Airflow를 많이 활용하지 못한점도 아쉽다.
- 인스타그램 데이터를 출연배우가 영향력을 미치는지에 관한 워드클라우드로만 활용한점이 아쉽긴했다. 인스타그램에서 락을 걸어둔건지 1000개 이상부터는 크롤링 진행이 안되서 1000개만 크롤링하는걸로 만족해야했다.
- Django를 이용해 웹브라우저를 구현한뒤 브라우저에서 검색어를 입력하면 해당 내용에 관한 인스타 크롤링을 진행하고 그 결과에 대한 워드 클라우드를 보여준다던지 머신러닝을 이용해 최근에 개봉한 영화들이 흥행에 성공할지를 예측하는 모델을 만들어보고싶었는데 프로젝트 기간내에 하기는 힘들어서 포기했는데 아쉽다.
- 카카오톡 챗봇으로 영화의 실시간 예매율이나 좌석점유율 등을 알려주는 서비스를 구현하는것도 해봤으면 좋았을거같다.

<br/><br/>

-------------------------------------------------

