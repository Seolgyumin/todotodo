# todotodo
SNU Likelion 10th hackerthon

작업이 진행 중일 때는 작업에 필요한 노션, 피그마, 그리고 그 외 참고하면 좋은 사이트 링크를 넣어두면 좋습니다.
작업이 완료된 후에는 여기에 프로젝트 UI뷰, 서비스 개요, 주요 기능, 팀 소개 같은 것을 넣어두면 좋아요!


### 자주 필요한 리눅스 커맨드
- 가상환경 만들기: python -m venv .venv
- 가상환경 활성화: source .venv/bin/activate
- 활성화된 가상환경에 필요한 라이브러리 설치하기: pip install -r requirements.txt
- 필요 라이브러리 설치: pip install [라이브러리명]
- 폴더 지우기 rm -rf [폴더명]

### 자주 필요한 깃 커맨드
- 원격 레포 로컬로 클론 받아오기: git clone [클론 받을 주소]
- 브랜치 변경: git checkout [브랜치명]
- 브랜치 강제 변경: git checkout -f [브랜치명] (주의: 커밋하지 않은 작업은 날아갑니다)
- 현재 브랜치에서 분기되는 브랜치 생성하며 브랜치 변경: git checkout -b [생성할 브랜치 명]

### 자주 필요한 장고 커맨드
- 장고 프로젝트 시작: django-admin startproject [프로젝트명]
- 장고 앱 추가
- 장고 서버 키기: python manage.py runserver
- 모델 변경했을 때: python manage.py makemigrations(마이그레이션 파일 생성하고) -> python manage.py migrate(실제 데이터베이스에 적용)
- 슈퍼유저 만들기: python manage.py createsuperuser
- 장고 쉘 키기: python manage.py shell

### 주의사항
- 새로운 라이브러리를 pip install [라이브러리명]으로 설치했을 경우, 꼭 pip freeze > requirements.txt 명령어를 통해 해당 라이브러리가 우리 프로젝트에 포함되어 있음을 명시해줍시다.
- env 파일은 깃이 아닌 다른 방법(카톡 등)을 통해 관리합시다.
