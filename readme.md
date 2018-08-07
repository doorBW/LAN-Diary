## LAN_Diary



- Admin 페이지의 계정은 따로 만들어야 합니다.
- 새롭게 프로젝트를 clone하면 db에 데이터가 없습니다. 교환일기장 로직부분은 data가 있다는 가정하에 구성하였기 때문에 admin페이지를 통해 예시데이터를 만들지 않으면 오류가 발생합니다.
- **Front 파일과 models 파일들은 절대 수정하지 마세요.**
- **front 파일 및 models 파일 수정이 필요할땐 슬랙방에서 논의해주세요.
- **git clone 및 프로젝트 설정 후에 꼭 branch 따서 작업하세요**



**python-version: 3.6.5**

**django-version: 2.0**

**postgreSQL: 10.4**

### 프로젝트 시작 방법
필요한 환경: postgreSQL

굳이 가상환경은 필요없으나, 가상환경이 아닌 분들은 pip freeze 명령어 수행하지 말것.

추가적으로 pip로 설치한 패키지이름은 꼭 slack방에 남겨주세요.

### 순서
1. **db설정**

  postgresql 에서 landiary 라는 database 생성

  **id: landiary, password: landiary 의 user 생성**

  (http://doorbw.tistory.com/183?category=711722)

  db 이름 및 user id와 password를 위와 동일하게 하지 않으면 db 접속 오류가 발생합니다.

  

2. **project 시작하기**

  이제 해당 git repository를 git clone 합니다.

  git clone을 하면 LAN-Diary 라는 폴더가 생깁니다.

  LAN-Diary/ 위치에서 다음 명령어를 통해 패키지 설치를 진행합니다.

  pip install -r requirements.txt

  

이후 LAN-Diary/landiary/ 위치로 이동하여 다음 명령어를 통해 migration을 진행합니다.

python3 manage.py makemigrations diary

python3 manage.py makemigrations login

python3 manage.py migrate



이후 서버를 시작하시면 됩니다.

python3 manage.py runserver



###-> 이후 아래 사이트를 참고하여 꼭 branch를 딴 후 작업 진행하세요.

그렇지 않을 경우 추후 복잡해질 수 있습니다.

http://doorbw.tistory.com/185?category=687756



* Admin 페이지의 계정은 따로 만들어야 합니다.
* 새롭게 프로젝트를 clone하면 db에 데이터가 없습니다. 교환일기장 로직부분은 data가 있다는 가정하에 구성하였기 때문에 admin페이지를 통해 예시데이터를 만들지 않으면 오류가 발생합니다.
* **Front 파일과 models 파일들은 절대 수정하지 마세요.**
* **front 파일 및 models 파일 수정이 필요할땐 슬랙방에서 논의해주세요.**
* **git clone 및 프로젝트 설정 후에 꼭 branch 따서 작업하세요**



## 잘 못하겠다 하시는 분들은 목요일날 도와드릴게요.. 그럴 일은 잘 없지만 애매하게 하다 master 건드리면 슬퍼집니다 :-(

