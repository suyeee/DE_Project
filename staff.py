import requests
import re

API_KEY = "key"
API_URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key={}&prdtStartYear=2012&prdtEndYear=2022&curPage={}'

# 영화코드 뽑아내기
# 개봉일이 없는 영화들도 있으므로 제작연도로 가져오기
movie_data = []
    
def movie_list(data):
    
    # 각 페이지당 영화 10개씩 들어가있음.
    for i in range(10):
        try:
            movieListResult =  data['movieListResult']
            movieList = movieListResult['movieList'][i]
            
            # 한국 영화만 뽑게끔 에러 발생시키기
            nation_pattern = '한국'
            text = movieList['repNationNm']
            re.match(nation_pattern, text).group()
            
            code = movieList['movieCd']
            name = movieList['movieNm']
            prdtyear = movieList['prdtYear']
            
        except:
            pass
    
        data = [code, name, prdtyear]
        
        movie_data.append(data)
    
    return movie_data

# datas = []

# 일단 10페이지까지만 확인
for page in range(10):
    
    res = requests.get(API_URL.format(API_KEY, page))
    data = res.json()

    code_data = movie_list(data)
    
#     datas.append(code_data)
    
movie_data 
