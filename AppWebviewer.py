#-*- coding: utf-8 -*-
import webview

print('AppWebViewer', 'load webview')
import os

print('AppWebViewer', 'load os')
import time

print('AppWebViewer', 'load time')
import sys

print('AppWebViewer', 'load sys')
print()


class AppWebviewer:

    def __init__(self):
        self.URL_jp = 'http://127.0.0.1:8000'
        self.login_success = False

    @staticmethod
    def print_except(e):
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('ERR', e)
        print(exc_type, fname, exc_tb.tb_lineno)

    def run_webview(self, q):

        def on_loaded():
            q.put('적정 계정 확인 후 프로그램 실행: DOM is ready')

        def on_closed():
            print('webview window closed')
            print('bye')

        window = webview.create_window(
            'KMPNS Mail Room 정산서 자동화',
            url=self.URL_jp,
            x=0,
            y=0,
            width=1000,
            height=800,
            min_size=(1000, 800)        
        )

        window.events.loaded += on_loaded
        window.events.closed += on_closed

        print('start webview')

        webview.start()
        

    def check_login(self, q):

        def on_shown():

            code = 'alert("회사 그룹웨어 아래 주소에 접속하여 계정 적정성을 확인합니다.\\n\\nhttps://direct.dongwon.com/WebSite/Common/Personal/MyInfo/PersonConnectHistoryView.aspx?system=mypage&alias=PersonConnectHistoryView&mnid=370\\n\\n아이디와 패스워드를 입력 후 로그인 버튼을 눌러주십시오")'

            window.evaluate_js(code, callback=None)

        def on_loaded():

            print('DOM is ready')

            q.put(f'적정 계정 여부 확인 중: DOM is ready')
            print(window.get_current_url())

            time.sleep(3)

            if 'https://direct.dongwon.com/WebSite/Login.aspx' in window.get_current_url():
                print('https://direct.dongwon.com/WebSite/Login.aspx is in url')

                # google account 로그인 필요한지 확인

            elif 'https://direct.dongwon.com/WebSite/Common/Personal/MyInfo/PersonConnectHistoryView.aspx' in window.get_current_url():
                print('https://www.google.com/ is url')

                # code = 'alert("로그인 성공")'

                # window.evaluate_js(code, callback=None)

                q.put(f'적정 계정 여부 확인 중: 로그인 하였습니다')
                self.login_success = '적정 계정 여부 확인 중: 로그인 되어 있습니다'
                window.destroy()

            print('on_loaded event end')

        def on_closing():
            q.put(self.login_success)

        def log_in():
            # window.load_url(
            #     r'https://accounts.google.com/ServiceLogin?hl=ko&passive=true&continue=https://www.google.com/&ec=GAZAmgQ')
            window.load_url(
                'https://accounts.google.com/ServiceLogin?hl=ko&passive=true&continue=https://www.google.com/&ec=GAZAmgQ')

        window = webview.create_window(
            '계정 확인',
            url='https://direct.dongwon.com/WebSite/Common/Personal/MyInfo/PersonConnectHistoryView.aspx?system=mypage&alias=PersonConnectHistoryView&mnid=370',
            x=0,
            y=0,
            min_size=(800, 800)
        )

        window.events.shown += on_shown
        window.events.loaded += on_loaded
        window.events.closing += on_closing

        webview.start()

    def logout(self, q):
        window = webview.create_window(
            '계정 확인',
            url=r'https://accounts.google.com/ServiceLogin?hl=ko&passive=true&continue=https://www.google.com/&ec=GAZAmgQ',
            x=1010,
            y=0,
            min_size=(800, 800)
        )

        webview.start()


if __name__ == '__main__':
    from multiprocessing import Queue

    web = AppWebviewer()
    web.run_webview(Queue())