# spartamarket  
### 프로젝트명 : 우리를 위한 중고거래(스파르타 마켓)
### 프로젝트 소개 : 우리가 아는 'ㄷㄱ' 홈페이지의 백엔드의 CRUD 구현과 프론트 엔드를 구현해본 프로젝트이다.  
### 프로젝트 기간 : 2024.04.12 ~ 2024.04.19(8일)
---
### 사용 기술 :
백엔드([Django](https://docs.djangoproject.com/ko/4.2/), [Python](https://docs.python.org/ko/3.8/)) : Django=4.2, Python=3.8

프론트엔드([HTML](https://developer.mozilla.org/ko/docs/Web/HTML),[CSS](https://developer.mozilla.org/ko/docs/Web/CSS))

DB([SQLite3](https://www.sqlite.org/docs.html))

### ERD<br>
<img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/faff60d0-c9cc-45ca-a6a7-89db95e8a3f1/%EC%A0%9C%EB%AA%A9_%EC%97%86%EB%8A%94_%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.drawio_(1).png?id=5b1a57c5-5e6c-4cca-bb41-7bd2ffefe1ec&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=IkzUXDXmy-uWV4Ns9YY5G2Qs_olijqKOH7g-13v7h4s&downloadName=%EC%A0%9C%EB%AA%A9+%EC%97%86%EB%8A%94+%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.drawio+%281%29.png" width="50%" height="150px"></img><br>

---
### 구현 기능
##### 1.회원기능
- 회원가입 : 기본 페이지->회원가입<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/dde5bf69-4a96-47f6-be8b-d37a68e0cca6/%EA%B8%B0%EB%B3%B8_%ED%8E%98%EC%9D%B4%EC%A7%80.png?id=b9b52b67-cece-4ba3-9907-d257c2780844&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=7Z37f5NG474qOmr2gFTF4YTORXOh-JOjrDvU_rVgs3c&downloadName=%EA%B8%B0%EB%B3%B8+%ED%8E%98%EC%9D%B4%EC%A7%80.PNG.png" width="50%" height="150px"></img><br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/6210f05f-1696-4687-baf0-9987040d9ece/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.png?id=2eb5332a-fd2f-4e3f-afeb-bee686a38832&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=5DDU5cqmIZ9_Zt2gDB1Jjzupf_8JB_MMMGkPGzEa94E&downloadName=%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.PNG.png" width="50%" height="150px"></img>
- 로그인 : 세션이 들어간 것을 확인(쿠키)<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/5228a2e0-e95a-4320-85dc-a56c53b7a91a/%EB%A1%9C%EA%B7%B8%EC%9D%B8.png?id=d0f98cc6-73a0-4e88-ba41-622ab06eac3e&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=sMHsQyw655S3zMSXanKjZf0go8CulIAGaRAZcwXeBPc&downloadName=%EB%A1%9C%EA%B7%B8%EC%9D%B8.PNG.png" width="50%" height="150px"></img><br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/49a6b1f0-228c-4d70-9ab6-e00185c95c41/%EB%A1%9C%EA%B7%B8%EC%9D%B8_%ED%9B%84.png?id=32a9729c-eb7b-45d5-9511-daee35812995&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=AvX7jfzYnPmSnY0p4doukOqvP1uGQsSXmXffU7wvUWs&downloadName=%EB%A1%9C%EA%B7%B8%EC%9D%B8+%ED%9B%84.PNG.png" width="50%" height="150px"></img>
- 로그아웃 : 세션이 빠진 것을 확인(쿠키)<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/71742203-bd3e-4303-bfd6-36610c359609/%EB%A1%9C%EA%B7%B8%EC%95%84%EC%9B%83.png?id=7628310c-e4bb-466d-8378-d27cfca65bd1&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=fmeo-drDAhTVFoceXV2ZjCfawPxkJGlrVdg4MBTQOGM&downloadName=%EB%A1%9C%EA%B7%B8%EC%95%84%EC%9B%83.PNG.png" width="50%" height="150px"></img>
##### 2.유저기능
- 유저별 프로필 페이지 : username, 가입일자, 내가 등록한 물건, 찜한 물건
  - 리스트는 없으면 물건 없다고 뜬다.
  - 페이지 자체에서 찜하기, 이동 가능
- 팔로우,팔로워 숫자 : 자기 자신은 안뜨고 다른 페이지는 팔로우, 언팔로우가 뜬다.<br>
- 프로필 사진 초기화 및 수정(추가) : 초기값 존재, 클리어->초깃값, 파일선택 교체<br>
  - 클리어와 선택을 동시에 불가능<br>  

  
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/1832e843-afa4-44d9-b3d1-58c0cda3c0b2/%ED%94%84%EB%A1%9C%ED%95%84_%ED%8E%98%EC%9D%B4%EC%A7%80.png?id=b399d137-021b-4ca4-a6b0-fe1249ea9295&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=8ofWp_sVPA5UNpgbq8BUz3XkjdTz2EAMxxfPc2r2BFo&downloadName=%ED%94%84%EB%A1%9C%ED%95%84+%ED%8E%98%EC%9D%B4%EC%A7%80.PNG.png" width="50%" height="150px"></img><br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/e17781c2-dcc5-444e-8c1b-6a7645c1014e/%EB%8B%A4%EB%A5%B8%EC%82%AC%EB%9E%8C_%ED%94%84%EB%A1%9C%ED%95%84_%ED%8E%98%EC%9D%B4%EC%A7%80.png?id=c71d0071-8d55-4529-98f6-964233731a58&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=0KZzqcK4T4wKZYMiWOJV9EVFOHs5O51y_Xw0qO6Q5zM&downloadName=%EB%8B%A4%EB%A5%B8%EC%82%AC%EB%9E%8C+%ED%94%84%EB%A1%9C%ED%95%84+%ED%8E%98%EC%9D%B4%EC%A7%80.PNG.png" width="50%" height="150px"></img><br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/71d8d096-4360-4897-a915-6ec4c7d60c3e/%ED%94%84%EB%A1%9C%ED%95%84_%EC%88%98%EC%A0%95.png?id=0d262258-eb8b-4193-b8bd-217106c4550a&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=TqC2h028h2pWnaL0J21yDAs-WrV5lAK3ThbgVxcipTM&downloadName=%ED%94%84%EB%A1%9C%ED%95%84+%EC%88%98%EC%A0%95.PNG.png" width="50%" height="150px"></img><br>

##### 3.게시기능
- 게시글 CRUD<br>

- 찜하기
  - 찜하기 수 보여주기(추가)<br>

- 상세 페이지<br>

- 정렬(찜순 1순위, 최신순 2순위, 기본 최신순)(추가)<br>

<br>

##### PIP LIST
- requirements.txt 파일을 참고
<img src="" width="50%" height="150px"></img>