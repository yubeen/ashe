# git이란?

* 버전 관리 도구 / 버전 관리 시스템
	* 파일 변화를 시간에 따라 기록했다가 나중에 특정 시점의 버전을 다시 꺼내올 수 있는 시스템

* git의 장점
	* 빠른 속도 : 모든 파일이 로컬 장비에 있으므로 통신에 따른 부하가 없고, 커밋, 브랜치, 머지등 모든 처리가 빠름
	* 비선형적인 개발 : 수천 수백개의 동시 다발적인 브랜치
	* 완벽한 분산 : 중앙 서버 저장소가 없고, 각자의 로컬 서버에 저장소가 존재, 일시적인 작업을 저장하기 유용

* git과 SVN의 차이
	* git은 분산 버전 관리 시스템, SVN은 중앙 집중식 버전 관리
	* git은 데이터를 스냅샷의 스트림 처럼 취급한다.svn은 델타 방식으로 저장

* 특징
	* 무결성 : SHA-1 해시를 사용하여 체크섬을 구한다.
	* git의 모든 활동은 데이터로 추가된다. 이 데이터는 삭제할 방법이 없다.
	* 모든 기능을 지원하는 것은 CLI뿐이다. 

# git의 최초 설정

* 'git config' : 환경 설정
	* 1) .git/config : 이 파일은 Git 디렉토리에 있고 특정 저장소(혹은 현재 작업 중인 프로젝트)에만 적용된다. --local 옵션을 사용하면 이 파일을 사용하도록 지정할 수 있다. 하지만 기본적으로 이 옵션이 적용되어 있다. (당연히, 이 옵션을 적용하려면 Git 저장소인 디렉토리로 이동 한 후 적용할 수 있다.)
	* 2) ~/.gitconfig, ~/.config/git/config 파일: 특정 사용자(즉 현재 사용자)에게만 적용되는 설정이다. git config --global 옵션으로 이 파일을 읽고 쓸 수 있다. 특정 사용자의 모든 저장소 설정에 적용된다.
	* 3) /etc/gitconfig 파일: 시스템의 모든 사용자와 모든 저장소에 적용되는 설정이다. git config --system 옵션으로 이 파일을 읽고 쓸 수 있다. (이 파일은 시스템 전체 설정파일이기 때문에 수정하려면 시스템의 관리자 권한이 필요하다.)

* 사용자 정보
	* git config --global user.name "이름"
	* git config --global user.email "이메일@piolink.com"
	* --global 옵션 설정은 한번만 하면 된다.

* 도움말
	* git help 명령어 ex)git help config
	* man git-명령어
	* -h, --help : 사용가능한 명령어들에 대한 간단 도움말

# git의 기초

* 저장소의 사용
	* git clone : 기존의 저장소 사용
	* git init : 현재 로컬 디렉토리에 새로운 저장소 생성
	* git status : 변경사항 조회

* 저장소는 작업 디렉토리(working directory) / 인덱스(Index) / HEAD로 구분되어 있다.
	* git add "파일이름" or *(전체) : 인덱스에 추가
	* git commit -m "설명" : 확정본을 HEAD에 반영
	* git push origin "branch name(master)" : HEAD의 내용을 원격 저장소에 반영
	* git checkout -- "파일이름" : 로컬의 변경내용 되돌리기(HEAD)

* 가지(branch) 관리
	* git branch : 브랜치 조회
	* git checkout -b "branch name" : 브랜치 생성 및 브랜치 전환
	* git checkout "branch name" : 브랜치 전환
	* git branch -d "branch name" : 브랜치 삭제	
	* git push origin "branch name" : 브랜치 원격 저장소 반영

* 갱신과 병합
	* git pull : 원격 저장소에 맞춰 갱신
	* git merge "branch name" : 다른 브랜치에 있는 변경 내용을 현재 가지에 병합
		* git diff "A branch name" "B branch name" : A,B 브랜치 비교
	* 충돌(Conflict)
		* git은 충돌이 일어나면 자동으로 merge하지 못해 커밋할 수 없다.
		* git status -> 충돌이 일어난 파일은 unmerged 상태 -> 충돌 사항 해결 -> add
	* 주의사항 : 항상 push/pull 전에 상태 확인

* 꼬리표(tag) 달기
	* git log : 확정본 식별자 얻기
	* git tag "꼬리표이름" "식별자" : 새로운 꼬리표 생성

# 원격 저장소

* git remote : 현재 프로젝트에 등록된 리모트 저장소를 확인
* git remote show "원격 저장소" : "원격 저장소"의 구체적인 정보 확인
* git remote rename A B : A저장소를 B저장
* git remote remove "원격 저장소" : "원격 저장소"를 삭제함

# 원격 저장소에 커밋 제외하기

* gitignore
	* 아무것도 없는 라인이나, '#'으로 시작하는 라인 무시
	* 표준 Glob패턴을 사용 (전체 프로젝트에 적용)
	* 슬래시(/)로 시작하면 하위 디렉토리에 적용(Recursivity)되지 않음
	* 디렉토리는 슬래시(/)를 끝에 사용하는 것으로 표현
	* 느낌표'!'로 시작하는 패턴의 파일은 무시하지 않음

# rebase

* 커밋의 베이스를 다시 정하기 위함
	* 협업 레포지토리에 이미 push한 경우 사용 지양
	* https://suhwan.dev/2018/01/21/Git-Rebase-1/ 참고
* git rebase : 브랜치A에 없는 브랜치B의 커밋을 브랜치A로 옮긴다.

# cherry pick (5.3 내용)

* cherry pick : 다른 브랜치에 있는 커밋을 선택적으로 내 브랜치에 적용시킬 때 사용하는 명령어
	* git cherry-pick "commit_hash" : 현재 브랜치에 commit_hash 적용. 적용하고 싶은 해쉬 나열 가능 

참고자료 : https://imasoftwareengineer.tistory.com/7

# 되돌리기 (7.8 내용)
* git reset --"옵션" "커밋 해쉬값" : 커밋 해쉬값으로 리파지토리 재설정
	* 옵션 : hard(돌아간 시점 이후 모든 내용 삭제) | soft(시점은 돌아가지만 인덱스는 남아있는 상태) | mixed(default/시점은 돌아가지만 변경사항만 남아있는 상태)
* git revert "커밋 해쉬값" : 이전 커밋 해쉬값의 내용을 불러옴

참고자료 : https://www.devpools.kr/2017/02/05/%EC%B4%88%EB%B3%B4%EC%9A%A9-git-%EB%90%98%EB%8F%8C%EB%A6%AC%EA%B8%B0-reset-revert/

IQ 140 실4 유저 신유빈 알찔님
