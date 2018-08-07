## LAN_Diary

python-version: 3.6.5

django-version: 2.0

postgreSQL: 10.4

### 프로젝트 시작 방법
필요한 환경: postgreSQL
굳이 가상환경은 필요없으나, 가상환경이 아닌 분들은 pip freeze 명령어 수행하지 말것.
추가적으로 pip로 설치한 패키지이름은 꼭 slack방에 남겨주세요.

### 순서
1. db설정
postgresql 에서 landiary 라는 database 생성
id: landiary, password: landiary 의 user 생성
(http://doorbw.tistory.com/183?category=711722)

2. project 시작하기
이제 해당 git repository를 git clone 합니다.
git clone을 하면 LAN-Diary 라는 폴더가 생깁니다.
LAN-Diary/ 위치에서 다음 명령어를 통해 패키지 설치를 진행합니다.
pip install -r requirements.txt

이후 LAN-Diary/landiary/ 위치로 이동하여 다음 명령어를 통해 migration을 진행합니다.
python3 manage.py makemigration diary
python3 manage.py makemigration login
python3 manage.py migrate

이후 서버를 시작하시면 됩니다.
python3 manage.py runserver
