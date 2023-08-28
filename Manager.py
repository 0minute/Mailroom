#-*- coding: utf-8 -*-

URL_jp = 'http://127.0.0.1:8000'


#아래 라이브러리 먼저 설치 필요\
#pip install openpyxl
#pip install justpy
#pip install pandas
#pip install Pillow
#pip install tabulate
#pip install pywebview
#pip install demjson3
#pip install pymysql
#pyinstaller --add-data "./data/*;./data" --add-data "./justpy/*.py;./justpy" --add-data "./justpy/templates/*;./justpy/templates" --key=Samil31Forever! --onefile --clean --noconfirm "Manager.py"
#pyinstaller --add-data "./data/*;./data" --add-data "./justpy/*.py;./justpy" --add-data "./justpy/templates/*;./justpy/templates" --key=Samil31Forever! --clean --noconfirm "Manager.py"
#pyinstaller --add-data "./data/*;./data" --add-data "./justpy/*.py;./justpy" --add-data "./justpy/templates/*;./justpy/templates" --collect-all "justpy" --collect-all "demjson3" --collect-all "pywebview"  --key=Samil31Forever!  --clean --noconfirm "Manager.py"
#pyinstaller --add-data "data/*;." --add-data "./justpy/.py;./justpy" --add-data "./justpy/templates/;./justpy/templates" --key=Samil31Forever! --clean --noconfirm --hidden-import justpy "Manager.py"


def start_appStartLogo(q):
    from AppStartLogo import AppStartLogo

    print('start_appStartLogo', 'start')

    app_startLogo = AppStartLogo(q)

    app_startLogo.root.mainloop()

    print('start_appStartLogo', 'finished')


def start_justpy(q):
    import AppJustpy as app_justpy

    print('start_justpy', 'start')

    app_justpy.run_jp(q)

    print('start_justpy', 'finished')


def start_jpWebview(q):
    from AppWebviewer import AppWebviewer
    app_webViewer = AppWebviewer()

    print('start_justpy', 'start')

    app_webViewer.run_webview(q)

    print('start_justpy', 'finished')


def start_checkLogin_Webview(q):
    from AppWebviewer import AppWebviewer
    app_webViewer = AppWebviewer()

    print('start_check_login', 'start')

    app_webViewer.check_login(q)

    print('start_check_login', 'finished')


def start_logout_Webview(q):
    from AppWebviewer import AppWebviewer
    app_webViewer = AppWebviewer()

    print('start_logout', 'start')

    app_webViewer.logout(q)

    print('start_logout', 'finished')


def set_expire_date(expire_date, q_startlogo):

    url = 'https://www.naver.com/'

    try:

        month = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
                 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

        res = urllib.request.urlopen(url)

        date = res.headers['Date'][5:-4]

        d, m, y, hour, min, sec = date[:2], month[date[3:6]], date[7:11], date[12:14], date[15:17], date[18:]

        print(f'[{url}]의 서버시간\n{y}년 {m}월 {d}일 {hour}시 {min}분 {sec}초')

        from datetime import datetime as dt

        server_date = dt.strptime(f'{y}{m}{d}', '%Y%m%d')

        ### 유효기간 입력
        expire_date = dt.strptime(expire_date, '%Y%m%d')

        remaining_date = int((expire_date - server_date).days) + 1

        server_date_str = f'{y}년 {m}월 {d}일'

        expire_date_str = dt.strftime(expire_date, "%Y년 %m월 %d일")

        if server_date > expire_date:

            print('프로그램 유효기간이 경과되었습니다.')
            print(f'유효기간 : {expire_date_str}')
            print(f'현재시간 : {server_date_str}')
            q_startlogo.put(f'expired_date;{expire_date_str};{server_date_str};{str(remaining_date)}')
            time.sleep(5)
            exit()

        else:
            q_startlogo.put(f'valid_date;{expire_date_str};{server_date_str};{str(remaining_date)}')
            time.sleep(1)

    except urllib.error.URLError as e:
        print(e)
        print('온라인 상태가 아닐 수 있습니다. 네트워크 상태를 확인해 주세요')
        q_startlogo.put(f'offline')
        time.sleep(5)
        exit()

    except Exception as e:
        print('unknown error')
        print(e)
        print('close startlogo')
        q_startlogo.put(f'close startlogo')
        exit()
        pass


def check_is_login():
    pass


if __name__ == '__main__':
    print('Manager', 'import os')
    import os
    print('Manager', 'load os')
    print('Manager', 'import sys')
    import sys
    print('Manager', 'load sys')
    print('Manager', 'import time')
    import time
    print('Manager', 'load time')
    print('Manager', 'import signal')
    import signal
    print('Manager', 'load signal')

    print('Manager', 'import multiprocessing')
    import multiprocessing
    print('Manager', 'load multiprocessing')
    print('Manager', 'import Queue, Process')
    from multiprocessing import Queue, Process
    print('Manager', 'load Queue, Process')
    print('Manager', 'import urllib.request')
    import urllib.request, urllib.error
    print('Manager', 'load urllib.request')

    multiprocessing.freeze_support()

    q_startlogo = Queue()
    q_jp = Queue()
    q_jpWebview = Queue()
    q_checkLogin_Webview = Queue()

    print('start p_app_startlogo process')

    p_app_startlogo = Process(target=start_appStartLogo, args=(q_startlogo,))
    p_app_startlogo.start()

    ### 유효기간 설정 : 삭제함
    #set_expire_date('20991231', q_startlogo)

    # 로그인 여부 확인

    q_startlogo.put('적정 계정 여부 확인 중')
    
    print('start app_checkLogin process')

    # 로그아웃
    # p_app_checkLogin = Process(target=start_logout_Webview, args=(q_checkLogin_Webview,))
    # p_app_checkLogin.start()

    # 아래 주석화는 로그인 생략
    """
    p_app_checkLogin = Process(target=start_checkLogin_Webview, args=(q_checkLogin_Webview,))
    p_app_checkLogin.start()

    while 1:
        res = q_checkLogin_Webview.get()
        if res:
            if res == '적정 계정 여부 확인 중: 로그인 되어 있습니다':
                print(res)
                q_startlogo.put(res)
                break
            else:
                print(res)
                q_startlogo.put(res)
        else:
            time.sleep(0.1)
    """
    # 아래 주석화는 로그인 생략 - 여기까지

    q_startlogo.put('적정 계정 확인 후 프로그램 실행: start app_jp process')
    print('start app_jp process')

    p_app_jp = Process(target=start_justpy, args=(q_jp,))
    app_jp_pid = 0

    p_app_jp.start()

    while 1:
        res = q_jp.get()
        if res:
            app_jp_pid = res
            print('app_jp pid: ', res)
            q_startlogo.put(f'적정 계정 확인 후 프로그램 실행: app_jp pid is {res}')
            break
        else:
            time.sleep(0.1)

    index = 0
    while 1:
        try:
            print('manager try', index)
            q_startlogo.put(f'적정 계정 확인 후 프로그램 실행: manager try {index}')

            index += 1

            time.sleep(0.5)

            print('request to', URL_jp)
            q_startlogo.put(f'적정 계정 확인 후 프로그램 실행: request to {URL_jp}')

            import requests
            print('Manager', 'load requests')

            res = requests.get(url=URL_jp)

            print(res.status_code)

            if res.status_code == 200:

                print('request success', res.status_code)
                q_startlogo.put(f'적정 계정 확인 후 프로그램 실행: request success {res.status_code}')

                app_webview = Process(target=start_jpWebview, args=(q_jpWebview,))
                app_webview.start()
                break

            else:

                print('request failed', res.status_code)
                q_startlogo.put(f'적정 계정 확인 후 프로그램 실행: request failed {res.status_code}')

            if index == 10:
                break

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('ERR', e)
            print(exc_type, fname, exc_tb.tb_lineno)

    while 1:
        res = q_jpWebview.get()
        if res:
            msg = res
            if msg == '적정 계정 확인 후 프로그램 실행: DOM is ready':
                print('close startlogo')
                q_startlogo.put(f'close startlogo')
                break
            else:
                print('ERR: odd event')
        else:
            time.sleep(0.1)

    app_webview.join()
    print('app_webview closed')

    os.kill(app_jp_pid, signal.SIGTERM)

    print('app_jp killed')
 