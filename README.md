# pracJango
django 연습을 위한 레포지토리

## `2020/05/23`
가상환경에서 django 설치 후 django-admin을 통한 프로젝트 및 앱 생성
admin 기능 활용하여 데이터베이스 연동 슈퍼유저 및 유저 생성 삭제

## `2020/05/24`

view.py에서 register.html에서 전달된 정보를 user 데이터베이스에 저장되는 코드 작성
jango admin을 통해 확인 완료.
view.py 회원가입 비밀번호 확인과 값 입력에 대한 예외처리 로직 추가.
email 모델 추가.

## `2020/05/25`

static url을 설정하여 장고 안에서 css,js 파일을 관리하는 방법
login기능 구현
세션처리
데이터베이스에 저장되있는 사용자 중복가입 방지 로직 생성하려 했으나
쿼리가 닫히질 않음
로그인의 로직도 아이디가 다를경우 쿼리가 닫히지 않는 문제
세션값을 없애서 로그아웃 구현