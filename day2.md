# 특강 2일차

.gitignore : 

*.XXX XXX형식 파일 모두(와일드 카드)

workplace area -> stage area로 이동

git add 파일(.하면 현재파일 모두)

###### 원격 저장소 등록

git remote add 'origin' 'address'
주소를 대신할 이름 -> origin

###### 원격 저장소 조회

git remote -v

###### 원격저장소 연결 삭제

git remote rm 'origin'

git 
git push 주소 master(기본 : main)
: github 서버에 업로드
git push -u 주소 master
: 추후에 업로드 할때 git push만 입력해도 업로드됨
git clone 주소
: 주소에 있는 파일을 가져옴

git clone (-u) 주소
: 폴더가 없을 때 폴더 통쨰로 가져오는것
git pull (주소)
: 변경사항만 가져오는 것



pull 안해서 error 발생시
vscode에서 파일을 열어서 선택
git add 을 한 후 git commit 을 하고 난 뒤에 나오는 vim문서에서 저장을 한 뒤에 git push
git허브에서 변경하면 안됨
로컬에서만 변경해야함