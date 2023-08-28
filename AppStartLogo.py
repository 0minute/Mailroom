#-*- coding: utf-8 -*-
import multiprocessing
from multiprocessing import Queue

print('AppStartLogo', 'import ctypes')
# from pyautogui import size
import ctypes

print('AppStartLogo', 'load ctypes')
print('AppStartLogo', 'import queue')
import queue

print('AppStartLogo', 'load queue')
print('AppStartLogo', 'import PIL')
from PIL import Image, ImageTk

print('AppStartLogo', 'load PIL')
print('AppStartLogo', 'import tkinter')
from tkinter import Tk, Label, font

print('AppStartLogo', 'load tkinter')
print('AppStartLogo', 'import itertools')
from itertools import count

print('AppStartLogo', 'load itertools')
print('AppStartLogo', 'import sys')
import sys

print('AppStartLogo', 'load sys')
print('AppStartLogo', 'import os')
import os

print('AppStartLogo', 'load os')
print()

try:
    wd = sys._MEIPASS
except AttributeError:
    wd = os.getcwd()


class ImageLabel(Label):
    """a label that displays images, and plays them if they are gifs"""

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
        self.delay = 20

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])

            if not self.loc + 1 == len(self.frames):
                self.after(self.delay, self.next_frame)
            else:
                print('gif end')


class AppStartLogo:

    def __init__(self, q):
        self.q = q
        self.root = None
        self.size = (445, 250)
        self.x, self.y = self.calculate_xy()

        self.q_count = 0

        self.bg = None
        self.label_bg = None
        self.font_noto = None
        self.label_progress = None

        self.flag_init_dif = 0

        self.make_page()
        self.get_q()
        self.stay_on_top()

    def calculate_xy(self):
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)

        x = int(screen_width / 2 - self.size[0] / 2)
        y = int(screen_height / 2 - self.size[1] / 2)

        return x, y

    def get_q(self):

        self.q_count += 1
        try:
            msg = self.q.get(0)
            print('q listened:', msg)
            if msg == 'close startlogo':
                self.root.destroy()

            elif msg.split(';')[0] == 'valid_date':
                expire_date = msg.split(';')[1]
                now_date = msg.split(';')[2]
                remaining_date = msg.split(';')[3]
                self.label_progress.place(x=20, y=180)
                self.label_progress['text'] = f'유효날짜 : {expire_date}\n현재날짜 : {now_date}\n잔여 사용가능일 : {remaining_date} 일'
                self.label_progress['justify'] = 'left'
                self.root.after(100, self.get_q)

            elif msg.split(';')[0] == 'expired_date':
                expire_date = msg.split(';')[1]
                now_date = msg.split(';')[2]
                remaining_date = msg.split(';')[3]
                self.label_progress.place(x=20, y=180)
                self.label_progress[
                    'text'] = f'프로그램 사용가능일이 경과되었습니다. 5초 후 프로그램을 종료합니다\n유효날짜 : {expire_date}\n현재날짜 : {now_date}\n'
                self.label_progress['justify'] = 'left'
                self.root.after(100, self.root.destroy)

            elif msg == 'offline':
                self.label_progress.place(x=20, y=200)
                self.label_progress['text'] = '인터넷에 연결되지 않을 수 있습니다. 네트워크 상태를 확인해 주세요.\n5초 후 프로그램을 종료합니다'
                self.label_progress['justify'] = 'left'
                self.root.after(5000, self.root.destroy)
            else:
                self.label_progress.place(x=20, y=210)
                self.label_progress['text'] = msg
                self.root.after(100, self.get_q)

        except queue.Empty:  # MK: 만약 message가 없으면 expect를 통하여 해당 함수 연산을 다시 수행함
            self.root.after(100, self.get_q)
            # print('nothing', self.q_count)

        # while 1:
        #     msg = self.q.get()
        #     try:
        #         if msg:
        #             print('q listened:', msg)
        #             self.label_progress['text'] = msg
        #         else:
        #             time.sleep(0.1)
        #             print('nothing', self.q_count)
        #     except Exception as e:
        #         print(e)

    def stay_on_top(self):
        # self.root.lift()
        # self.root.after(2000, self.stay_on_top)
        # self.root.attributes('-topmost', True)
        pass

    def make_page(self):
        try:
            self.root = Tk()
            self.root.geometry(f"{self.size[0]}x{self.size[1]}+{self.x}+{self.y}")

            # self.bg = PhotoImage(file="./data/DSDWizardLogo.gif", format=f'gif -index 4')
            # self.label_bg = Label(self.root, image=self.bg, bg='#D04A02')
            # self.label_bg.place(x=0, y=0)
            self.label_bg = ImageLabel(self.root, bg='#FAE100', width=self.size[0])
            print(os.listdir(wd))
            # 환경에 따라 경로가 다름
            if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
                file_path = os.path.join(wd, 'data', 'Logo_s.gif')   #CU 수정함
            else:
                file_path = os.path.join(wd, 'data', 'Logo_s.gif')

            self.label_bg.load(file_path)
            self.label_bg.place(x=0, y=0)
            # label_bg.pack()

            self.font_noto = font.Font(family="Noto Sans CJK KR Regular", size=10)
            # font_noto = font.Font(family="맑은 고딕", size=10)
            self.label_progress = Label(self.root, text='Progress', font=self.font_noto, fg='#000000', bg='#FAE100')
            self.label_progress.place(x=20, y=210)
            # label_progress.pack()

            # lab = Label(root, text="Hello World", font=('Time New Roman', 35), fg="green", anchor="c").pack()
            self.root.overrideredirect(True)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    app_startLogo = AppStartLogo(Queue())
    app_startLogo.root.mainloop()
