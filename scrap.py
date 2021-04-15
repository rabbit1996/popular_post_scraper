import requests
from bs4 import BeautifulSoup

# 페이지
page = '1'

#주 소
url = f'https://www.dogdrip.net/?mid=dogdrip&sort_index=popular'

# 사용자 위장 헤더
requests_headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; ; NCLIENT50_AAP5EF3046787B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
}


response = requests.get(url,headers = requests_headers)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    post_list = {}

    # 게시글 제목
    title = soup.select_one('#main > div > div.eq.section.secontent.background-color-content > div > div > table > tbody > tr:nth-child(1) > td.title > span > a > span.ed.title-link')
    post_list['title'] = title

    # 게시글 링크
    link = 'https://www.dogdrip.net/' + soup.find_all('a',{'class':'ed link-reset'})[0]['href']
    post_list['link'] = link

    # 게시글 컨텐츠


    print("title:",title.text)
    print("link:",link)
else:
    print(response.status_code)