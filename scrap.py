import requests
from bs4 import BeautifulSoup
import os
import time


class scraper:

    def __init__(self):
        self.requests_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; ; NCLIENT50_AAP5EF3046787B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        }

class dogdrip_scrap(scraper):

    def __init__(self, scrap_type=0, page=1):

        """page : 페이지 넘버,
        scrap_type : 스크래핑 url 선택, 0 : 개드립 인기글, 1 : 개드립,
        2 : 유저 개드립 인기글, 3 : 유저 개드립
        index_type : 게시판 별 첫번째 글 순서, 공지가 추가될 시 변할 수 있음.
        """

        super().__init__()  # requests_headers
        url_list = [f'https://www.dogdrip.net/index.php?mid=dogdrip&sort_index=popular&page=',
                    f'https://www.dogdrip.net/index.php?mid=dogdrip&page=',
                    f'https://www.dogdrip.net/index.php?mid=userdog&sort_index=popular&page=',
                    f'https://www.dogdrip.net/index.php?mid=userdog&page=']

        self.url = url_list[scrap_type] + str(page)

        # 게시판별 첫번째 글 순서
        index_list = [1, 4, 1, 6]
        self.index_type = index_list[scrap_type]

        # 반환값, 스크랩된 포스트의 정보를 저장
        self.post_list = dict()

    def chk_latest_title(self, recent_title):
        """최신글 업데이트 확인 메소드, latest.txt에 최신글 제목을 저장"""

        try:
            latest = open('record/dog_latest.txt', 'r', -1, 'utf-8')
        except FileNotFoundError:
            latest = open('record/dog_latest.txt', 'w+', -1, 'utf-8')
            latest.close()
            return False
        else:
            title = latest.read()
            latest.close()

            if title == recent_title:
                # 글 업데이트 확인
                return True
            else:
                print('최신 글 :', recent_title)
                latest = open('record/dog_latest.txt', 'w+', -1, 'utf-8')
                latest.write(recent_title)
                return False

    def do_scrap(self):
        """개드립 커뮤니티 스크랩 메소드"""
        response = requests.get(self.url, headers=self.requests_headers)

        if response.status_code == 200:  # 사이트 정상 응답

            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 게시글 제목
            title = soup.select_one(
                f'#main > div > div.eq.section.secontent.background-color-content > div > div > table > tbody > tr:nth-child({self.index_type}) > td.title > span > a > span.ed.title-link')

            if self.chk_latest_title(title.text):
                # 글 업데이트 확인
                print("글이 올라오지 않았습니다.")
                return
            self.post_list['title'] = title.text

            # 게시글 링크
            if self.index_type % 2 != 0:
                link = 'https://www.dogdrip.net/' + soup.find_all('a', {'class': 'ed link-reset'})[self.index_type - 1][
                    'href']
            else:
                link = soup.find_all('a', {'class': 'ed link-reset'})[self.index_type - 1]['href']
            self.post_list['link'] = link

            # 게시글 컨텐츠
            content_response = requests.get(link, headers=self.requests_headers)
            content_html = content_response.text
            content_soup = BeautifulSoup(content_html, 'html.parser')
            content = content_soup.select_one('#article_1 > div')

            content_list = ""
            for i, content in enumerate(content):
                if content.next_element.name == 'img':
                    src = content.next_element['src']
                    content = '<p><img src=' + 'https://www.dogdrip.net' + src + '></p>'
                content_list += str(content)
            self.post_list['content'] = content_list

            # html 변환 및 저장
            html_file = open('html/dogdrip.html', 'w+', -1, 'utf-8')
            html_file.write(content_list)
            html_file.close()

            return self.post_list

        else:  # 비정상 응답
            print(response.status_code)
            return

    def __str__(self):
        return f"title : {self.post_list['title']} \nlink : {self.post_list['link']} \ncontent : {self.post_list['content']}"

if __name__ == '__main__':
    test = dogdrip_scrap()
    test.do_scrap()