# KMPNS
메일룸

# 주의사항
pyinstaller로 exe 제작 시 반드시 파이선 3.8.10버전 사용.
3.10 버전은 카카오 내부 보안 프로그램이 차단하고있음.

# github
- 브랜치 링크 : https://github.com/0minute/Mailroom

# exe만들기
#pyinstaller --add-data "data/*;." --add-data "./justpy/.py;./justpy" --add-data "./justpy/templates/;./justpy/templates" --key=Samil31Forever! --clean --noconfirm #--hidden-import justpy "Manager.py"
#justpy 안쓸거라서 필요없을듯하기도..