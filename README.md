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
- 다이어그램<br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/faff60d0-c9cc-45ca-a6a7-89db95e8a3f1/%EC%A0%9C%EB%AA%A9_%EC%97%86%EB%8A%94_%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.drawio_(1).png?id=5b1a57c5-5e6c-4cca-bb41-7bd2ffefe1ec&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=IkzUXDXmy-uWV4Ns9YY5G2Qs_olijqKOH7g-13v7h4s&downloadName=%EC%A0%9C%EB%AA%A9+%EC%97%86%EB%8A%94+%EB%8B%A4%EC%9D%B4%EC%96%B4%EA%B7%B8%EB%9E%A8.drawio+%281%29.png" width="50%" height="150px"></img><br>

---
### 구현 기능
#### 1.회원기능
- 회원가입 : 기본 페이지->회원가입<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/dde5bf69-4a96-47f6-be8b-d37a68e0cca6/%EA%B8%B0%EB%B3%B8_%ED%8E%98%EC%9D%B4%EC%A7%80.png?id=b9b52b67-cece-4ba3-9907-d257c2780844&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=7Z37f5NG474qOmr2gFTF4YTORXOh-JOjrDvU_rVgs3c&downloadName=%EA%B8%B0%EB%B3%B8+%ED%8E%98%EC%9D%B4%EC%A7%80.PNG.png" width="50%" height="150px"></img> 기본 페이지<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/6210f05f-1696-4687-baf0-9987040d9ece/%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.png?id=2eb5332a-fd2f-4e3f-afeb-bee686a38832&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=5DDU5cqmIZ9_Zt2gDB1Jjzupf_8JB_MMMGkPGzEa94E&downloadName=%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85.PNG.png" width="50%" height="150px"> 회원 가입 페이지</img>
- 로그인 : 세션이 들어간 것을 확인(쿠키)<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/5228a2e0-e95a-4320-85dc-a56c53b7a91a/%EB%A1%9C%EA%B7%B8%EC%9D%B8.png?id=d0f98cc6-73a0-4e88-ba41-622ab06eac3e&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=sMHsQyw655S3zMSXanKjZf0go8CulIAGaRAZcwXeBPc&downloadName=%EB%A1%9C%EA%B7%B8%EC%9D%B8.PNG.png" width="50%" height="150px"></img> 로그인 페이지<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/49a6b1f0-228c-4d70-9ab6-e00185c95c41/%EB%A1%9C%EA%B7%B8%EC%9D%B8_%ED%9B%84.png?id=32a9729c-eb7b-45d5-9511-daee35812995&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=AvX7jfzYnPmSnY0p4doukOqvP1uGQsSXmXffU7wvUWs&downloadName=%EB%A1%9C%EA%B7%B8%EC%9D%B8+%ED%9B%84.PNG.png" width="50%" height="150px"> 로그인 완료 후 세션 쿠키 확인</img>
- 로그아웃 : 세션이 빠진 것을 확인(쿠키)<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/71742203-bd3e-4303-bfd6-36610c359609/%EB%A1%9C%EA%B7%B8%EC%95%84%EC%9B%83.png?id=7628310c-e4bb-466d-8378-d27cfca65bd1&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713592800000&signature=fmeo-drDAhTVFoceXV2ZjCfawPxkJGlrVdg4MBTQOGM&downloadName=%EB%A1%9C%EA%B7%B8%EC%95%84%EC%9B%83.PNG.png" width="50%" height="150px"> 로그아웃 후 세션 쿠키 확인</img><br>

#### 2.유저기능
- 유저별 프로필 페이지 : username, 가입일자, 내가 등록한 물건, 찜한 물건
  - 리스트는 없으면 물건 없다고 뜬다.
  - 페이지 자체에서 찜하기, 이동 가능
- 팔로우,팔로워 숫자 : 자기 자신은 안뜨고 다른 페이지는 팔로우, 언팔로우가 뜬다.<br>
- 프로필 사진 초기화 및 수정(추가) : 초기값 존재, 클리어->초깃값, 파일선택 교체<br>
  - 클리어와 선택을 동시에 불가능<br>  

  
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/1832e843-afa4-44d9-b3d1-58c0cda3c0b2/%ED%94%84%EB%A1%9C%ED%95%84_%ED%8E%98%EC%9D%B4%EC%A7%80.png?id=b399d137-021b-4ca4-a6b0-fe1249ea9295&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=8ofWp_sVPA5UNpgbq8BUz3XkjdTz2EAMxxfPc2r2BFo&downloadName=%ED%94%84%EB%A1%9C%ED%95%84+%ED%8E%98%EC%9D%B4%EC%A7%80.PNG.png" width="50%" height="150px"></img> 프로필 페이지(목록)<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/e17781c2-dcc5-444e-8c1b-6a7645c1014e/%EB%8B%A4%EB%A5%B8%EC%82%AC%EB%9E%8C_%ED%94%84%EB%A1%9C%ED%95%84_%ED%8E%98%EC%9D%B4%EC%A7%80.png?id=c71d0071-8d55-4529-98f6-964233731a58&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=0KZzqcK4T4wKZYMiWOJV9EVFOHs5O51y_Xw0qO6Q5zM&downloadName=%EB%8B%A4%EB%A5%B8%EC%82%AC%EB%9E%8C+%ED%94%84%EB%A1%9C%ED%95%84+%ED%8E%98%EC%9D%B4%EC%A7%80.PNG.png" width="50%" height="150px"></img> 다른 유저 프로필 페이지, 팔로우 확인<br>
    <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/71d8d096-4360-4897-a915-6ec4c7d60c3e/%ED%94%84%EB%A1%9C%ED%95%84_%EC%88%98%EC%A0%95.png?id=0d262258-eb8b-4193-b8bd-217106c4550a&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=TqC2h028h2pWnaL0J21yDAs-WrV5lAK3ThbgVxcipTM&downloadName=%ED%94%84%EB%A1%9C%ED%95%84+%EC%88%98%EC%A0%95.PNG.png" width="50%" height="150px"></img> 프로필 사진 교체 클리어하면 기본값<br>

##### 3.게시기능
- 게시글 CRUD<br>
- 찜하기
  - 찜하기 수 보여주기(추가)<br>
- 정렬(찜순 1순위, 최신순 2순위, 기본 최신순)(추가)<br>
- 상세 페이지 : 제목 내용 가격 작성자 수정일<br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/edad77d0-ceba-46ad-b173-ec5445680d64/%EA%B2%8C%EC%8B%9C%EA%B8%80.png?id=b9821f52-ebe0-4aee-88b6-eac2983df09e&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=zb-RVrLZ5ZvR7ZJ-cVxwjZpyuD7DEtJadI9wUUPUhCg&downloadName=%EA%B2%8C%EC%8B%9C%EA%B8%80.PNG.png" width="50%" height="150px"></img> 게시글 조회 + 기본 정렬(최신순)+ 찜 수 보여주기<br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/0e97faa6-6d39-41a1-8fa1-cc21aecd9d44/%EC%A0%95%EB%A0%AC_%EC%88%9C%EC%9C%84.png?id=a5c80759-3dd7-44f4-b00d-c8c17f0530ae&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=s3_cQQSP1peqBIdL-W_RzmVoOhvLG8BQfkUStjV7a6A&downloadName=%EC%A0%95%EB%A0%AC+%EC%88%9C%EC%9C%84.PNG.png" width="50%" height="150px"></img> 정렬 인기순<br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/d1e4cf20-395e-478c-becf-bf31dfed7392/%EC%A0%95%EB%A0%AC_%EC%B5%9C%EC%8B%A0%EC%88%9C.png?id=91382ce7-e0cf-44ca-8438-94e7963bf354&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=ISNFBFZXEAlerXaYokNRMnk6dLiWZnC3OgagZz3gzjs&downloadName=%EC%A0%95%EB%A0%AC+%EC%B5%9C%EC%8B%A0%EC%88%9C.PNG.png" width="50%" height="150px"></img> 정렬 1순위 인기순, 2순위 최신순<br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/54c02f6a-9cdb-4f5a-a28a-224a2ed458c4/%EC%83%9D%EC%84%B1.png?id=9b13024a-5028-4abf-b650-6be1e2c849b5&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=WBfZwKGFcAStv6HfvmZ0xtfqqIFdsS-aWYv9s33HqVw&downloadName=%EC%83%9D%EC%84%B1.PNG.png" width="50%" height="150px"></img> 게시글 생성하기<br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/c0da67f8-e13b-4ac4-8ce9-25e8dde09657/%EC%88%98%EC%A0%95.png?id=eb07f36e-ba2d-4ab6-8713-d54798045fda&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=gcYNsZ5YBY_GporPlgnFE9d4mIkDAhA7lz92q7Yk1Fs&downloadName=%EC%88%98%EC%A0%95.PNG.png" width="50%" height="150px"></img> 게시글 자기가 한 것만 수정<br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/45b39661-09dd-4ed3-b337-76e83dbfcbfd/%EC%88%98%EC%A0%95%EC%99%84%EB%A3%8C.png?id=7f4a52a6-0954-433a-835d-1c4b60f9aec2&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=c5H9Ev6W8BTcU1Zu4Or0EAltFE2eAT5UQCm9o3dPdag&downloadName=%EC%88%98%EC%A0%95%EC%99%84%EB%A3%8C.PNG.png" width="50%" height="150px"></img> 수정 완료 후 (자기가 작성한)상세페이지<br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/cecc837b-5577-4d1a-819a-6d415a17b371/%EC%83%9D%EC%84%B1%EB%90%9C_%EB%AA%A9%EB%A1%9D%EC%97%90%EC%84%9C_%EC%82%AD%EC%A0%9C%EA%B0%80%EA%B8%B0%EC%A0%84.png?id=f98870fc-9cd1-4af4-a322-38e12c416453&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=AVPgMycgwME7Cq1tmTadaOxmujQLsHUIXFEmt6if1vI&downloadName=%EC%83%9D%EC%84%B1%EB%90%9C+%EB%AA%A9%EB%A1%9D%EC%97%90%EC%84%9C+%EC%82%AD%EC%A0%9C%EA%B0%80%EA%B8%B0%EC%A0%84.PNG.png" width="50%" height="150px"> 삭제 전 목록</img><br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/3cb941fb-7658-4138-b4dd-857c10f97404/%EC%82%AD%EC%A0%9C%EC%99%84.png?id=a9ff6c11-a6a6-401f-ba3b-7490f0cfd117&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=Qjq71q9aELWI0tXM88MArVW5JZaHL_J6B84MjFAOb8c&downloadName=%EC%82%AD%EC%A0%9C%EC%99%84.PNG.png" width="50%" height="150px"></img> 삭제 완료 후 목록<br>
  <img src="https://file.notion.so/f/f/c6f85bed-6385-4f92-a30c-49e507bf2add/31d2d2cd-02ed-4e48-8204-b0566689fd3e/%EB%8B%A4%EB%A5%B8%EC%82%AC%EB%9E%8C_%EC%83%81%EC%84%B8%ED%8E%98%EC%9D%B4%EC%A7%80.png?id=36fe3cce-1c60-4c50-9789-6f1749e755a8&table=block&spaceId=c6f85bed-6385-4f92-a30c-49e507bf2add&expirationTimestamp=1713600000000&signature=NE8OSlmVg9aQ7PVFNkZywQT8sMG9DknOga1w5qJE2lo&downloadName=%EB%8B%A4%EB%A5%B8%EC%82%AC%EB%9E%8C+%EC%83%81%EC%84%B8%ED%8E%98%EC%9D%B4%EC%A7%80.PNG.png" width="50%" height="150px"></img> 다른 사람의 상세 페이지(삭제 수정 불가)<br>
<br>

##### PIP LIST
- requirements.txt 파일을 참고