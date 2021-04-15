# popular_post_scraper

## popular_post_scraper란?
커뮤니티의 인기글을 실시간으로 스크래핑 및 포스팅하는 서비스입니다.

## 이런걸 왜 만드나요?
각종 커뮤니티에는 유머글, 정보글, 최근 핫한 이슈, 혐오글, 바이럴 마케팅 등 다양한 형태의 글이 올라옵니다.
재밌는 사실은 커뮤니티 별 성향에 따라 같은 글이라도 반응이 다르다는 것입니다.
이에 흥미를 느끼게 됬고 이 서비스를 만들고자 결심하게 됬습니다.

## 파일 설명
latest.txt : 최신글 제목을 저장합니다. 글 업데이트를 확인하는 장치입니다.
scrap.py : 각 사이트 글을 스크래핑하는 function을 저장할 모듈입니다.
popular_post_scrap : scrap.py 작성 전 코드를 테스트하는 jupyter 파일입니다.

dogdrip.html : 스크래핑이 된 개드립 최신글입니다. 차후 다른 커뮤니티 글의 파일도 추가될 예정입니다.

## 목표 사이트
1. 개드립
2. 오유
3. 웃대
4. 에펨코
5. 클리앙
6. MLB

선정 조건 : 없음. 이 외에도 추가될 수 있습니다.
