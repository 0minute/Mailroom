#-*- coding: utf-8 -*-
print('AppJustpy', 'import justpy')
from justpy import Div, QCard, QCircularProgress, QTab, QTabs, QInput, QButton, QCardSection, QDialog, QSelect, \
    QuasarPage, QDiv, Img
from justpy import run_task, parse_html, justpy

print('AppJustpy', 'load justpy')
print('AppJustpy', 'import tkinter')
from tkinter import filedialog, Tk

print('AppJustpy', 'load tkinter')
print('AppJustpy', 'import pandas')
import pandas as pd

print('AppJustpy', 'load pandas')
print('AppJustpy', 'import sys')
import sys

print('AppJustpy', 'load sys')
print('AppJustpy', 'import os')
import os

print('AppJustpy', 'load os')
print('AppJustpy', 'import asyncio')
import asyncio

print('AppJustpy', 'load asyncio')
print('AppJustpy', 'import tabulate')
from tabulate import tabulate

print('AppJustpy', 'load tabulate')
print('AppJustpy', 'import webview')
import webview

print('AppJustpy', 'load webview')
print()

try:
    wd = sys._MEIPASS
except AttributeError:
    wd = os.getcwd()

#개발코드 import
import Mail_Room as la
# import AppExcelToXml
from AppWebviewer import AppWebviewer
from multiprocessing import Queue, Process

URL_jp = 'http://127.0.0.1:8000'

# load data
file_path = os.path.join(wd, 'data', 'work_process.csv')
work_process_df = pd.read_csv(file_path)

style_df = pd.DataFrame([
    {'name': 'div_toolBar', 'style_text': 'height: 50px;'},
    {'name': 'div_toolBar_title', 'style_text': 'font-family: "Times New Roman", Times, serif; font-size: 30px;'},
    {'name': 'div_toolBar_info',
     'style_text': 'font-family: "Times New Roman", Times, serif; font-size: 15px; white-space: pre-line; line-height: 1;'},
    {'name': 'div_mainWindow', 'style_text': 'margin-top: 50px;'},
    {'name': 'card_tabs', 'style_text': 'margin-top: 50px;'},

    {'name': 'div_checkEmployee', 'style_text': ''},
    {'name': 'div_checkEmployee_guidelineImg', 'style_text': 'width: 600px;'},
    {'name': 'div_checkEmployee_title', 'style_text': 'font-family: "Noto Sans KR";'},
    {'name': 'div_checkEmployee_container', 'style_text': 'min-height: 50px;'},
    {'name': 'div_checkEmployee_guideline', 'style_text': 'min-width: 300px; font-family: "Noto Sans KR";'},
    {'name': 'div_checkEmployee_label', 'style_text': 'min-width: 300px; font-family: "Noto Sans KR";'},
    {'name': 'div_checkEmployee_value',
     'style_text': 'min-width: 300px; font-family: "Noto Sans KR"; font-size: text-subtitle1;'},
    {'name': 'div_checkEmployee_button', 'style_text': ''},

    {'name': 'div_dsd_converter', 'style_text': ''},

    {'name': 'div_getFile_title', 'style_text': 'font-family: "Noto Sans KR";'},
    {'name': 'div_getFile_container', 'style_text': 'min-height: 30px;'},
    {'name': 'div_getFile_label', 'style_text': 'min-width: 300px; font-family: "Noto Sans KR";'},
    {'name': 'div_getFile_value',
     'style_text': 'min-width: 300px; font-family: "Noto Sans KR"; font-size: text-subtitle1;'},
    {'name': 'div_button_on', 'style_text': 'font-weight:bold; color:#1E1E1E; background: #FAE100'},
    {'name': 'div_button_off', 'style_text': ''},

    {'name': 'div_companyInfo_container', 'style_text': 'min-height: 50px;'},
    {'name': 'div_companyInfo_label', 'style_text': 'min-width: 300px;'},
    {'name': 'div_companyInfo_value', 'style_text': 'min-width: 300px; font-size: text-subtitle1;'},

    {'name': 'div_process_label', 'style_text': 'font-size: 15px; width: 180px; min-height: 30px; '},

    {'name': 'div_dsd_analyzer', 'style_text': ''},

    {'name': 'div_horizontal_2', 'style_text': 'max-width: 600px;'},
    {'name': 'div_horizontal_3', 'style_text': ''},
    {'name': 'div_title', 'style_text': 'font-size: 18px; min-height: 25px; font-weight: bold;'},
    {'name': 'div_companyInfo_title', 'style_text': ''},
    {'name': 'div_companyInfo_title', 'style_text': ''},
    # {'name': 'button_getFile', 'style_text': 'height: 25px;'},
    # {'name': 'button_getFile', 'style_text': 'height: 25px;'},
    # {'name': 'button_getFile', 'style_text': 'height: 25px;'},
    # {'name': 'button_getFile', 'style_text': 'height: 25px;'}
])

class_df = pd.DataFrame([
    {'name': 'div_toolBar', 'classes_text': 'q-pa-xs fixed-top z-top text-white bg-grey-9'},
    {'name': 'div_toolBar_title', 'classes_text': 'q-ml-md vertical-middle row inline text-bold'},
    {'name': 'div_toolBar_info', 'classes_text': 'q-mt-xs q-mr-md vertical-middle float-right row inline'},
    {'name': 'div_mainWindow', 'classes_text': 'q-pa-xs absolute-top'},
    {'name': 'card_tabs', 'classes_text': 'q-pa-xs fixed-top z-top'},

    {'name': 'div_checkEmployee', 'classes_text': 'q-pa-md'},

    {'name': 'div_checkEmployee_guidelineImg', 'classes_text': 'q-mt-xs'},
    {'name': 'div_checkEmployee_title', 'classes_text': 'q-ml-lg text-h5'},
    {'name': 'card_checkEmployee', 'classes_text': 'my-card q-mt-md'},
    {'name': 'div_checkEmployee_container', 'classes_text': 'q-ml-sm'},
    {'name': 'div_checkEmployee_guideline', 'classes_text': 'vertical-middle q-mt-md'},
    {'name': 'div_checkEmployee_label', 'classes_text': 'vertical-middle row inline text-bold'},
    {'name': 'div_checkEmployee_value', 'classes_text': 'vertical-middle row inline'},
    {'name': 'div_checkEmployee_button', 'classes_text': 'vertical-middle bg-red-8 text-white text-subtitle1'},

    {'name': 'div_dsd_converter', 'classes_text': 'q-pa-sm'},  #여기

    {'name': 'div_getFile_title', 'classes_text': 'q-ml-lg text-h5'},
    {'name': 'card_getFile', 'classes_text': 'my-card q-mt-md'},
    {'name': 'div_getFile_container', 'classes_text': 'q-ml-sm'},
    {'name': 'div_getFile_label', 'classes_text': 'vertical-middle row inline text-bold'},
    {'name': 'div_getFile_value', 'classes_text': 'vertical-middle row inline'},

    {'name': 'div_button_on', 'classes_text': 'q-mr-sm vertical-middle text-subtitle1'}, #bg-red-8
    {'name': 'div_button_off', 'classes_text': 'q-mr-sm vertical-middle bg-grey-6 text-white text-subtitle1'},

    {'name': 'div_companyInfo_title', 'classes_text': 'q-ml-lg q-mt-lg text-h5'},
    {'name': 'div_companyInfo_container', 'classes_text': 'q-ml-sm'},
    {'name': 'div_companyInfo_label', 'classes_text': 'vertical-middle row inline text-bold'},
    {'name': 'div_companyInfo_value', 'classes_text': 'vertical-middle row inline'},

    {'name': 'div_dsd_analyzer', 'classes_text': 'hidden q-pa-md'},
])

# app_excelToXml = AppExcelToXml.App('normal')

app_webViewer = AppWebviewer()

root = Tk()
root.attributes("-topmost", True)
root.lift()
root.withdraw()
root.overrideredirect(True)
root.attributes("-alpha", 0)


def load_filedialog():
    try:
        path_file = filedialog.askopenfilename(
            initialdir=os.path.abspath(__file__),
            title="파일을 선택 해 주세요",
            filetypes=(("*.xlsx | *.csv", "*xlsx; *csv"), ("*.xlsm", "*xlsm"), ("all files", "*.*")),
            parent=root
        )
        if path_file:
            file_name = path_file.split('/')[-1]
            path_dir = '/'.join(path_file.split('/')[:-1])

            return file_name, path_dir

        else:

            return '', ''

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('ERR', e)
        print(exc_type, fname, exc_tb.tb_lineno)



async def load_info_data(self, msg):
    print(self.name + '버튼 클릭')
    comp_nm = self.name
    
    file_name, path_dir = load_filedialog()
    print('check load_info', (file_name, path_dir))

    if file_name:

        msg.page.elements['div_getFile_fileName_value' + '_' +comp_nm].text = file_name
        msg.page.elements['div_getFile_filePath_value' + '_' +comp_nm].text = path_dir

        try:

            # get_defined_name_list
            if comp_nm == 'Raw_s':            
                la.Dir_Raw_s= f'{file_name}/{path_dir}'                        
            elif comp_nm == 'Raw_h':            
                la.Dir_Raw_h= f'{file_name}/{path_dir}'            
            elif comp_nm == 'Raw_t':            
                la.Dir_Raw_t= f'{file_name}/{path_dir}'
            elif comp_nm == 'Raw_o':
                la.Dir_Raw_o= f'{file_name}/{path_dir}'
            elif comp_nm == 'Raw_d':
                la.Dir_Raw_d= f'{file_name}/{path_dir}'
            elif comp_nm == 'mailTable':
                la.mailTableXl= f'{file_name}/{path_dir}'                  
            elif comp_nm == 'templateXl':
                la.dir_temp= f'{file_name}/{path_dir}'   


            #하나 불러왔을때 닫기
            msg.page.elements['button_getFile' + '_' +comp_nm].classes = get_from_df(class_df, 'name', 'div_button_off',
                                                                      'classes_text')
            msg.page.elements['button_getFile' + '_' +comp_nm].disable = True
            
            msg.page.elements['button_reset' + '_' +comp_nm].style = get_from_df(style_df, 'name', 'div_button_on', 'style_text')
            msg.page.elements['button_reset' + '_' +comp_nm].classes = get_from_df(class_df, 'name', 'div_button_on', 'classes_text')
            msg.page.elements['button_reset' + '_' +comp_nm].disable = False

            #모두다 불러왔을때 열리기
            
            if msg.page.elements['div_getFile_fileName_value_Raw_s'].text != '-' \
                and msg.page.elements['div_getFile_fileName_value_Raw_h'].text != '-' \
                    and msg.page.elements['div_getFile_fileName_value_Raw_t'].text != '-'\
                        and msg.page.elements['div_getFile_fileName_value_Raw_o'].text != '-' \
                            and msg.page.elements['div_getFile_fileName_value_Raw_d'].text != '-' \
                                and msg.page.elements['div_getFile_fileName_value_mailTable'].text != '-' \
                                    and msg.page.elements['div_getFile_fileName_value_templateXl'].text != '-' :
                msg.page.elements['button_Convert'].style = get_from_df(style_df, 'name', 'div_button_on', 'style_text')
                msg.page.elements['button_Convert'].classes = get_from_df(class_df, 'name', 'div_button_on', 'classes_text')
                msg.page.elements['button_Convert'].disable = False


            run_task(msg.page.update())
            await asyncio.sleep(0)

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('ERR', e)
            print(exc_type, fname, exc_tb.tb_lineno)

    return 1






async def getFileData_Convert(self, msg):


    msg.page.elements['dialog_workProcess_dialog'].value = True
    print('<<메일룸 정산 Start>>')

    try:

        msg.page.elements['circularProgress_workProgress'].indeterminate = True

        run_task(msg.page.update())
        await asyncio.sleep(0)


        msg.page.elements['div_workProgress_circularProgressComment'].text = 'Data 파일을 읽는 중'
        run_task(msg.page.update())
        await asyncio.sleep(0)



        #Input파일
        la.Dir_Raw_h = os.path.abspath(
            msg.page.elements['div_getFile_filePath_value_Raw_h'].text 
            + '/' 
            + msg.page.elements['div_getFile_fileName_value_Raw_h'].text
            ) #'\Data_24시화물.xlsx'
        
        la.Dir_Raw_d = os.path.abspath(
            msg.page.elements['div_getFile_filePath_value_Raw_d'].text 
            + '/' 
            + msg.page.elements['div_getFile_fileName_value_Raw_d'].text
            ) #'\Data_딜리버리.xlsx'
        
        la.Dir_Raw_s = os.path.abspath(
            msg.page.elements['div_getFile_filePath_value_Raw_s'].text 
            + '/' 
            + msg.page.elements['div_getFile_fileName_value_Raw_s'].text
            ) #'\Data_손자.csv'
        
        la.Dir_Raw_o = os.path.abspath(
            msg.page.elements['div_getFile_filePath_value_Raw_o'].text 
            + '/' 
            + msg.page.elements['div_getFile_fileName_value_Raw_o'].text
            ) #'\Data_신청내역.xlsx'
        
        la.Dir_Raw_t = os.path.abspath(
            msg.page.elements['div_getFile_filePath_value_Raw_t'].text 
            + '/' 
            + msg.page.elements['div_getFile_fileName_value_Raw_t'].text
            ) #'\Data_택배.xlsx'


        msg.page.elements['div_process_value_get_defined_name_list'].remove_class('hidden')
        msg.page.elements['div_workProgress_circularProgressComment'].text = 'Table 파일 읽는 중'       
        run_task(msg.page.update())
        await asyncio.sleep(0)



        #기본파일
        la.mailTableXl = os.path.abspath(
            msg.page.elements['div_getFile_filePath_value_mailTable'].text 
            + '/' 
            + msg.page.elements['div_getFile_fileName_value_mailTable'].text
            ) #= 'KMPNS_메일룸_Table_v1.xlsx'
        la.dir_temp = os.path.abspath(
            msg.page.elements['div_getFile_filePath_value_templateXl'].text 
            + '/' 
            + msg.page.elements['div_getFile_fileName_value_templateXl'].text
            ) #'\템플릿.xlsx'


        msg.page.elements['div_process_value_make_data_structure'].remove_class('hidden')
        msg.page.elements['div_workProgress_circularProgressComment'].text = 'DataFrame 생성 중'        
        run_task(msg.page.update())
        await asyncio.sleep(0)        
        


    
        la.Dir_Table_premium = la.getRngTable(la.mailTableXl, 'Company')    #'\Table_입주사.xlsx'
        la.Dir_Table_name = la.getRngTable(la.mailTableXl, 'GoogleName')    #'\Table_회사명.xlsx'
        la.Dir_Table_account = la.getRngTable(la.mailTableXl, 'Location')   #'\Table_소재지.csv'
        la.Dir_Table_setting = la.getRngTable(la.mailTableXl, 'Setting')    #'\Table_설정.xlsx'
        la.Raw_h = pd.read_excel(la.Dir_Raw_h)
        la.Raw_d = pd.read_excel(la.Dir_Raw_d)
        la.Raw_s = pd.read_csv(la.Dir_Raw_s, encoding='CP949')
        la.Raw_o = pd.read_excel(la.Dir_Raw_o)
        la.Raw_t = pd.read_excel(la.Dir_Raw_t)
        

        
        print('<<기본파일 INPUT 완료>>')
        
        
        la.Table_premium = la.Dir_Table_premium.input_to_df()    #pd.read_excel(Path_+Dir_Table_premium)
        la.Table_name = la.Dir_Table_name.input_to_df()          #pd.read_excel(Path_+Dir_Table_name)
        la.Table_account = la.Dir_Table_account.input_to_df()    #pd.read_csv(Path_+Dir_Table_account)
        la.Table_set = la.Dir_Table_setting.input_to_df()        #pd.read_excel(Path_+Dir_Table_setting)

        print('<<테이블 INPUT 완료>>')


        print(la.Table_name)        
        
        msg.page.elements['div_process_value_get_value_from_address'].remove_class('hidden')
        msg.page.elements['div_workProgress_circularProgressComment'].text = '폴더 생성 중 ('+la.datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+ ')'
        run_task(msg.page.update())
        await asyncio.sleep(0)


        
        la.Save_path_ = la.Save_path_app+'\\'+la.datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        la.createDirectory(la.Save_path_)
        
        
        print('<<폴더 생성 완료 : '+ la.Save_path_ +'>>')



        msg.page.elements['div_process_value_check_data_step_1'].remove_class('hidden')
        msg.page.elements['div_workProgress_circularProgressComment'].text = 'Excel 정산서 생성 중'
        run_task(msg.page.update())
        await asyncio.sleep(0)




        la.Date_, la.Report_Date, la.Flat_Rate, la.Ex_Rate, la.Ex_Count, la.Fee = la.Get_Setting_Data(la.Table_set)
        

        msg.page.elements['div_process_value_check_data_step_2'].remove_class('hidden')
        msg.page.elements['div_workProgress_circularProgressComment'].text = '마무리 중'
        run_task(msg.page.update())
        await asyncio.sleep(0)




        la.Raw_o, la.Raw_d, la.Table_premium, la.Table_premium_on = la.Get_Table_Mailroom(la.Raw_h,la.Raw_d,la.Raw_s,la.Raw_o,la.Raw_t,la.Table_premium,la.Table_name,la.Table_account)
    
        la.Mail_Room_def(la.Date_, la.Report_Date, la.Flat_Rate, la.Ex_Rate, la.Ex_Count, la.Fee, la.Raw_o, la.Raw_d, la.Table_premium, la.Table_premium_on)


        msg.page.elements['div_process_value_check_data_step_3'].remove_class('hidden')
        msg.page.elements['div_workProgress_circularProgressComment'].text = '완료'
        run_task(msg.page.update())
        await asyncio.sleep(0)



        msg.page.elements['circularProgress_workProgress'].indeterminate = False
        msg.page.elements['circularProgress_workProgress'].value = 100
        run_task(msg.page.update())
        await asyncio.sleep(0)

        # app_excelToXml.make_contentsXml(app_excelToXml.data_list)
        print('<<정산서 생성 완료>>')

        msg.page.elements['dialog_workProcess_dialog'].value = False
        await asyncio.sleep(0)
        run_task(msg.page.update())




        msg.page.elements[
            'div_workDone_text'].text = f'작업을 완료하였습니다.\n작업한 파일은 다음 경로에 있습니다.\n{la.Save_path_}'
        msg.page.elements['div_workDone_text'].style = 'white-space: pre-line;'
        msg.page.elements['dialog_workDone_dialog'].value = True
        await asyncio.sleep(1.5)
        run_task(msg.page.update())

        os.startfile(la.Save_path_)

        msg.page.elements['dialog_workProcess_dialog'].value = False
        msg.page.elements['circularProgress_workProgress'].indeterminate = False
        msg.page.elements['circularProgress_workProgress'].value = 0
        msg.page.elements['div_process_value_get_defined_name_list'].set_class('hidden')
        msg.page.elements['div_process_value_make_data_structure'].set_class('hidden')
        msg.page.elements['div_process_value_get_value_from_address'].set_class('hidden')
        msg.page.elements['div_process_value_check_data_step_1'].set_class('hidden')
        msg.page.elements['div_process_value_check_data_step_2'].set_class('hidden')
        msg.page.elements['div_process_value_check_data_step_3'].set_class('hidden')
        # msg.page.elements['div_process_value_make_style'].set_class('hidden')
        # msg.page.elements['div_process_value_check_known_character'].set_class('hidden')
        # msg.page.elements['div_process_value_make_line_break'].set_class('hidden')
        # msg.page.elements['div_process_value_make_tag'].set_class('hidden')
        msg.page.elements['div_workProgress_circularProgressComment'].text = 'Progress'



    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('ERR', e)
        print(exc_type, fname, exc_tb.tb_lineno)
        print(type(e))
        if str(e) == '확인되지 않은 고객명이 식별되었습니다. 회사명 테이블을 확인해주세요.' :
            msg.page.elements[
                'div_workDone_text'].text = "확인되지 않은 고객명이 식별되었습니다.\n'회사명 테이블과 아래 파일을 확인해주세요.\n" + la.Save_path_ + '\회사명확인.xlsx'
            msg.page.elements['div_workDone_text'].style = 'white-space: pre-line;'
            msg.page.elements['dialog_workDone_dialog'].value = True
            os.startfile(la.Save_path_)

        elif str(e) == '입주사 테이블에 누락된 고객명이 식별되었습니다. 입주사 테이블을 확인해주세요.' :
            msg.page.elements[
                'div_workDone_text'].text = "누락된 고객명이 식별되었습니다.\n입주사 테이블과 아래 파일을 확인해주세요.\n" + la.Save_path_ + '\입주사확인.xlsx'
            msg.page.elements['div_workDone_text'].style = 'white-space: pre-line;'
            msg.page.elements['dialog_workDone_dialog'].value = True
            os.startfile(la.Save_path_)
        elif str(e) == '소재지 테이블에 누락된 빌딩명이 식별되었습니다. 소재지 테이블을 확인해주세요.' :
            msg.page.elements[
                'div_workDone_text'].text = "소재지 테이블에 누락된 빌딩명이 식별되었습니다.\n소재지 테이블과 아래 파일을 확인해주세요.\n" + la.Save_path_ + '\소재지확인.xlsx'
            msg.page.elements['div_workDone_text'].style = 'white-space: pre-line;'
            msg.page.elements['dialog_workDone_dialog'].value = True
            os.startfile(la.Save_path_)
        else :
            msg.page.elements[
                'div_workDone_text'].text = f'오류가 발생하였습니다. Input된 파일들을 확인하여주시기 바랍니다.'
            msg.page.elements['div_workDone_text'].style = 'white-space: pre-line;'
            msg.page.elements['dialog_workDone_dialog'].value = True
        await asyncio.sleep(1.5)
        run_task(msg.page.update())
        
        
        msg.page.elements['dialog_workProcess_dialog'].value = False
        msg.page.elements['circularProgress_workProgress'].indeterminate = False
        msg.page.elements['circularProgress_workProgress'].value = 0
        msg.page.elements['div_process_value_get_defined_name_list'].set_class('hidden')
        msg.page.elements['div_process_value_make_data_structure'].set_class('hidden')
        msg.page.elements['div_process_value_get_value_from_address'].set_class('hidden')
        msg.page.elements['div_process_value_check_data_step_1'].set_class('hidden')
        msg.page.elements['div_process_value_check_data_step_2'].set_class('hidden')
        msg.page.elements['div_process_value_check_data_step_3'].set_class('hidden')
        # msg.page.elements['div_process_value_make_style'].set_class('hidden')
        # msg.page.elements['div_process_value_check_known_character'].set_class('hidden')
        # msg.page.elements['div_process_value_make_line_break'].set_class('hidden')
        # msg.page.elements['div_process_value_make_tag'].set_class('hidden')
        msg.page.elements['div_workProgress_circularProgressComment'].text = 'Progress'
 
        

    run_task(msg.page.update())

    return 0



async def reset_data(self, msg):
    # global app_excelToXml
    # app_excelToXml = AppExcelToXml.App('normal')

    comp_nm = self.name.replace('_reset','')
    print(comp_nm + '리셋 버튼 클릭')

    
    try:
        msg.page.elements['dialog_workProcess_dialog'].value = False
        msg.page.elements['circularProgress_workProgress'].indeterminate = False
        msg.page.elements['circularProgress_workProgress'].value = 0
        msg.page.elements['div_process_value_get_defined_name_list'].set_class('hidden')
        msg.page.elements['div_process_value_make_data_structure'].set_class('hidden')
        msg.page.elements['div_process_value_get_value_from_address'].set_class('hidden')
        msg.page.elements['div_process_value_check_data_step_1'].set_class('hidden')
        msg.page.elements['div_process_value_check_data_step_2'].set_class('hidden')
        msg.page.elements['div_process_value_check_data_step_3'].set_class('hidden')
        # msg.page.elements['div_process_value_make_style'].set_class('hidden')
        # msg.page.elements['div_process_value_check_known_character'].set_class('hidden')
        # msg.page.elements['div_process_value_make_line_break'].set_class('hidden')
        # msg.page.elements['div_process_value_make_tag'].set_class('hidden')
        msg.page.elements['div_workProgress_circularProgressComment'].text = 'Progress'
        msg.page.elements['button_getFile'+ '_' + comp_nm].classes = get_from_df(class_df, 'name', 'div_button_on', 'classes_text')
        msg.page.elements['button_Convert'].classes = get_from_df(class_df, 'name', 'div_button_off', 'classes_text')
        msg.page.elements['button_reset'+ '_' + comp_nm].classes = get_from_df(class_df, 'name', 'div_button_off', 'classes_text')
        msg.page.elements['button_getFile'+ '_' + comp_nm].disable = False
        msg.page.elements['button_Convert'].disable = True
        msg.page.elements['button_reset'+ '_' + comp_nm].disable = True
        msg.page.elements['div_getFile_fileName_value'+ '_' + comp_nm].text = '-'
        msg.page.elements['div_getFile_filePath_value'+ '_' + comp_nm].text = '-'

        run_task(msg.page.update())
        await asyncio.sleep(0)

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print('ERR', e)
        print(exc_type, fname, exc_tb.tb_lineno)

    run_task(msg.page.update())

    return 0






def get_from_df(df, column_search, value_search, column_result):
    if column_search in df.columns.tolist():
        df_temp = df[df[column_search] == value_search]
        if len(df_temp) == 1:
            if column_result in df.columns.tolist():
                return df_temp[column_result].values.tolist()[0]
            else:
                print('검색기준 column 있고 value 는 한가지이지만, 찾으려는 column 이 존재하지 않습니다.', column_search, df)
        elif len(df_temp) == 0:
            print('검색기준 column 있지만 value 값과 일치하는 row 는 존재하지 않습니다.', column_search, value_search, df)
            raise
        else:
            print('검색기준 column 있지만 value 값과 일치하는 row 가 1개 이상 입니다.', column_search, value_search, df)
            raise
    else:
        print('검색기준 column 이 존재하지 않습니다.', column_search, df)
        raise

    return 0


async def main():
    wp = QuasarPage(dark=False)
    wp.elements = {}

    div_root = Div(a=wp)
    wp.elements['div_root'] = div_root

    # 툴바

    div_toolBar = Div(classes=get_from_df(class_df, 'name', 'div_toolBar', 'classes_text'),
                      style=get_from_df(style_df, 'name', 'div_toolBar', 'style_text'),
                      a=div_root)
    div_toolBar_title = Div(classes=get_from_df(class_df, 'name', 'div_toolBar_title', 'classes_text'),
                            style=get_from_df(style_df, 'name', 'div_toolBar_title', 'style_text'),
                            a=div_toolBar,
                            text='KMPNS Mail Room')
    div_toolBar_info = Div(classes=get_from_df(class_df, 'name', 'div_toolBar_info', 'classes_text'),
                           style=get_from_df(style_df, 'name', 'div_toolBar_info', 'style_text'),
                           a=div_toolBar,
                           text='Developed by ARTS Team\nPwC Korea')

    wp.elements['div_toolBar'] = div_toolBar
    wp.elements['div_toolBar_title'] = div_toolBar_title
    wp.elements['div_toolBar_info'] = div_toolBar_info

    div_mainWindow = Div(classes=get_from_df(class_df, 'name', 'div_mainWindow', 'classes_text'),
                         style=get_from_df(style_df, 'name', 'div_mainWindow', 'style_text'),
                         a=div_root)

    # Main Window

    wp.elements['div_mainWindow'] = div_mainWindow


    # Check Employee

    div_mainButton = Div(classes=get_from_df(class_df, 'name', 'div_dsd_converter', 'classes_text'),
                            a=div_mainWindow)
    wp.elements['div_mainButton'] = div_mainButton


    div_mainButtonQ = Div(a=div_mainButton)
    # div_getFile_title = Div(classes=get_from_df(class_df, 'name', 'div_getFile_title', 'classes_text'),
    #                            a=div_getFile,
    #                            text='리스 파일 가져오기')
    


    button_Convert = QButton(size='md',
                             classes=get_from_df(class_df, 'name', 'div_button_off', 'classes_text'),
                             style=get_from_df(style_df, 'name', 'div_button_off', 'style_text'),
                             text='정산하기',
                             disable=True,
                             a=div_mainButtonQ)
    button_Convert.on('click', getFileData_Convert)
    

    wp.elements['button_Convert'] = button_Convert


    ########### 첫번째 섹션

    div_dsd_converter = Div(classes=get_from_df(class_df, 'name', 'div_dsd_converter', 'classes_text'),
                            a=div_mainWindow)
    wp.elements['div_dsd_converter'] = div_dsd_converter

    # 파일 가져오기

    div_getFile_Raw_s = Div(a=div_dsd_converter)
    
    
    card_getFile_Raw_s = QCard(classes=get_from_df(class_df, 'name', 'card_getFile', 'classes_text'),
                         a=div_getFile_Raw_s)
    cardSection_getFile_Raw_s = QCardSection(a=card_getFile_Raw_s)

    div_getFile_buttonContainer_Raw_s = Div(classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
                                      style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
                                      a=cardSection_getFile_Raw_s)
    div_getFile_buttonNaming_Raw_s = Div(text='손자 Data 가져오기',
                                   classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                   style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                   a=div_getFile_buttonContainer_Raw_s)
    button_getFile_Raw_s = QButton(size='md',
                             classes=get_from_df(class_df, 'name', 'div_button_on', 'classes_text'),
                             style=get_from_df(style_df, 'name', 'div_button_on', 'style_text'),
                             text='파일 가져오기',
                             name='Raw_s',
                             a=div_getFile_buttonContainer_Raw_s)
    button_getFile_Raw_s.on('click', load_info_data)

    button_reset_Raw_s = QButton(size='md',
                           classes=get_from_df(class_df, 'name', 'div_button_off', 'classes_text'),
                           style=get_from_df(style_df, 'name', 'div_button_off', 'style_text'),
                           text='초기화',
                           disable=True,
                           name='Raw_s_reset',
                           a=div_getFile_buttonContainer_Raw_s)
    button_reset_Raw_s.on('click', reset_data)

    wp.elements['button_reset_Raw_s'] = button_reset_Raw_s


    div_getFile_fileName_container_Raw_s = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_s)



    div_getFile_fileName_label_Raw_s = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_s,
                                     text='파일 이름')
    div_getFile_fileName_value_Raw_s = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_s,
                                     id='div_getFile_fileName_value',
                                     text='-')
    div_getFile_filePath_container_Raw_s = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_s)
    div_getFile_filePath_label_Raw_s = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_s,
                                     text='파일 경로')
    div_getFile_filePath_value_Raw_s = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_s,
                                     text='-')




    wp.elements['div_getFile_Raw_s'] = div_getFile_Raw_s
    # wp.elements['div_getFile_title'] = div_getFile_title
    wp.elements['card_getFile_Raw_s'] = card_getFile_Raw_s
    wp.elements['cardSection_getFile_Raw_s'] = cardSection_getFile_Raw_s
    wp.elements['div_getFile_buttonNaming_Raw_s'] = div_getFile_buttonNaming_Raw_s
    wp.elements['button_getFile_Raw_s'] = button_getFile_Raw_s

    wp.elements['div_getFile_fileName_container_Raw_s'] = div_getFile_fileName_container_Raw_s
    wp.elements['div_getFile_fileName_label_Raw_s'] = div_getFile_fileName_label_Raw_s
    wp.elements['div_getFile_fileName_value_Raw_s'] = div_getFile_fileName_value_Raw_s
    wp.elements['div_getFile_filePath_container_Raw_s'] = div_getFile_filePath_container_Raw_s
    wp.elements['div_getFile_filePath_label_Raw_s'] = div_getFile_filePath_label_Raw_s
    wp.elements['div_getFile_filePath_value_Raw_s'] = div_getFile_filePath_value_Raw_s
    
        
    
    
    # 두번째 Section
    #div_Raw_h = Div(classes=get_from_df(class_df, 'name', 'div_dsd_converter', 'classes_text'),
    #                        a=div_mainWindow)
    #wp.elements['div_Raw_h'] = div_Raw_h

    # 파일 가져오기

    div_getFile_Raw_h = Div(a=div_dsd_converter)
    
    
    card_getFile_Raw_h = QCard(classes=get_from_df(class_df, 'name', 'card_getFile', 'classes_text'),
                         a=div_getFile_Raw_h)
    cardSection_getFile_Raw_h = QCardSection(a=card_getFile_Raw_h)

    div_getFile_buttonContainer_Raw_h = Div(classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
                                      style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
                                      a=cardSection_getFile_Raw_h)
    div_getFile_buttonNaming_Raw_h = Div(text='24시화물 Data 가져오기',
                                   classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                   style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                   a=div_getFile_buttonContainer_Raw_h)
    button_getFile_Raw_h = QButton(size='md',
                             classes=get_from_df(class_df, 'name', 'div_button_on', 'classes_text'),
                             style=get_from_df(style_df, 'name', 'div_button_on', 'style_text'),
                             text='파일 가져오기',
                             name='Raw_h',
                             a=div_getFile_buttonContainer_Raw_h)
    button_getFile_Raw_h.on('click', load_info_data)

    button_reset_Raw_h = QButton(size='md',
                           classes=get_from_df(class_df, 'name', 'div_button_off', 'classes_text'),
                           style=get_from_df(style_df, 'name', 'div_button_off', 'style_text'),
                           text='초기화',
                           disable=True,
                           name='Raw_h_reset',
                           a=div_getFile_buttonContainer_Raw_h)
    button_reset_Raw_h.on('click', reset_data)

    wp.elements['button_reset_Raw_h'] = button_reset_Raw_h


    div_getFile_fileName_container_Raw_h = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_h)



    div_getFile_fileName_label_Raw_h = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_h,
                                     text='파일 이름')
    div_getFile_fileName_value_Raw_h = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_h,
                                     id='div_getFile_fileName_value',
                                     text='-')
    div_getFile_filePath_container_Raw_h = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_h)
    div_getFile_filePath_label_Raw_h = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_h,
                                     text='파일 경로')
    div_getFile_filePath_value_Raw_h = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_h,
                                     text='-')




    wp.elements['div_getFile_Raw_h'] = div_getFile_Raw_h
    # wp.elements['div_getFile_title'] = div_getFile_title
    wp.elements['card_getFile_Raw_h'] = card_getFile_Raw_h
    wp.elements['cardSection_getFile_Raw_h'] = cardSection_getFile_Raw_h
    wp.elements['div_getFile_buttonNaming_Raw_h'] = div_getFile_buttonNaming_Raw_h
    wp.elements['button_getFile_Raw_h'] = button_getFile_Raw_h

    wp.elements['div_getFile_fileName_container_Raw_h'] = div_getFile_fileName_container_Raw_h
    wp.elements['div_getFile_fileName_label_Raw_h'] = div_getFile_fileName_label_Raw_h
    wp.elements['div_getFile_fileName_value_Raw_h'] = div_getFile_fileName_value_Raw_h
    wp.elements['div_getFile_filePath_container_Raw_h'] = div_getFile_filePath_container_Raw_h
    wp.elements['div_getFile_filePath_label_Raw_h'] = div_getFile_filePath_label_Raw_h
    wp.elements['div_getFile_filePath_value_Raw_h'] = div_getFile_filePath_value_Raw_h
    
        



   ############### 세번째 Section
   
    #div_Raw_t = Div(classes=get_from_df(class_df, 'name', 'div_dsd_converter', 'classes_text'),
    #                        a=div_mainWindow)
    #wp.elements['div_Raw_t'] = div_Raw_t

    # 파일 가져오기

    div_getFile_Raw_t = Div(a=div_dsd_converter)
    
    
    card_getFile_Raw_t = QCard(classes=get_from_df(class_df, 'name', 'card_getFile', 'classes_text'),
                         a=div_getFile_Raw_t)
    cardSection_getFile_Raw_t = QCardSection(a=card_getFile_Raw_t)

    div_getFile_buttonContainer_Raw_t = Div(classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
                                      style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
                                      a=cardSection_getFile_Raw_t)
    div_getFile_buttonNaming_Raw_t = Div(text='택배 Data 가져오기',
                                   classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                   style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                   a=div_getFile_buttonContainer_Raw_t)
    button_getFile_Raw_t = QButton(size='md',
                             classes=get_from_df(class_df, 'name', 'div_button_on', 'classes_text'),
                             style=get_from_df(style_df, 'name', 'div_button_on', 'style_text'),
                             text='파일 가져오기',
                             name='Raw_t',
                             a=div_getFile_buttonContainer_Raw_t)
    button_getFile_Raw_t.on('click', load_info_data)

    button_reset_Raw_t = QButton(size='md',
                           classes=get_from_df(class_df, 'name', 'div_button_off', 'classes_text'),
                           style=get_from_df(style_df, 'name', 'div_button_off', 'style_text'),
                           text='초기화',
                           disable=True,
                           name='Raw_t_reset',
                           a=div_getFile_buttonContainer_Raw_t)
    button_reset_Raw_t.on('click', reset_data)

    wp.elements['button_reset_Raw_t'] = button_reset_Raw_t


    div_getFile_fileName_container_Raw_t = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_t)



    div_getFile_fileName_label_Raw_t = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_t,
                                     text='파일 이름')
    div_getFile_fileName_value_Raw_t = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_t,
                                     id='div_getFile_fileName_value',
                                     text='-')
    div_getFile_filePath_container_Raw_t = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_t)
    div_getFile_filePath_label_Raw_t = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_t,
                                     text='파일 경로')
    div_getFile_filePath_value_Raw_t = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_t,
                                     text='-')




    wp.elements['div_getFile_Raw_t'] = div_getFile_Raw_t
    # wp.elements['div_getFile_title'] = div_getFile_title
    wp.elements['card_getFile_Raw_t'] = card_getFile_Raw_t
    wp.elements['cardSection_getFile_Raw_t'] = cardSection_getFile_Raw_t
    wp.elements['div_getFile_buttonNaming_Raw_t'] = div_getFile_buttonNaming_Raw_t
    wp.elements['button_getFile_Raw_t'] = button_getFile_Raw_t

    wp.elements['div_getFile_fileName_container_Raw_t'] = div_getFile_fileName_container_Raw_t
    wp.elements['div_getFile_fileName_label_Raw_t'] = div_getFile_fileName_label_Raw_t
    wp.elements['div_getFile_fileName_value_Raw_t'] = div_getFile_fileName_value_Raw_t
    wp.elements['div_getFile_filePath_container_Raw_t'] = div_getFile_filePath_container_Raw_t
    wp.elements['div_getFile_filePath_label_Raw_t'] = div_getFile_filePath_label_Raw_t
    wp.elements['div_getFile_filePath_value_Raw_t'] = div_getFile_filePath_value_Raw_t
    
        

   ############### 네번째 Section
   
    div_internal = Div(classes=get_from_df(class_df, 'name', 'div_dsd_converter', 'classes_text'),
                            a=div_mainWindow)
    wp.elements['div_internal'] = div_internal

    # 파일 가져오기

    div_getFile_Raw_o = Div(a=div_internal)
    
    
    card_getFile_Raw_o = QCard(classes=get_from_df(class_df, 'name', 'card_getFile', 'classes_text'),
                         a=div_getFile_Raw_o)
    cardSection_getFile_Raw_o = QCardSection(a=card_getFile_Raw_o)

    div_getFile_buttonContainer_Raw_o = Div(classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
                                      style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
                                      a=cardSection_getFile_Raw_o)
    div_getFile_buttonNaming_Raw_o = Div(text='신청내역 Data 가져오기',
                                   classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                   style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                   a=div_getFile_buttonContainer_Raw_o)
    button_getFile_Raw_o = QButton(size='md',
                             classes=get_from_df(class_df, 'name', 'div_button_on', 'classes_text'),
                             style=get_from_df(style_df, 'name', 'div_button_on', 'style_text'),
                             text='파일 가져오기',
                             name='Raw_o',
                             a=div_getFile_buttonContainer_Raw_o)
    button_getFile_Raw_o.on('click', load_info_data)

    button_reset_Raw_o = QButton(size='md',
                           classes=get_from_df(class_df, 'name', 'div_button_off', 'classes_text'),
                           style=get_from_df(style_df, 'name', 'div_button_off', 'style_text'),
                           text='초기화',
                           disable=True,
                           name='Raw_o_reset',
                           a=div_getFile_buttonContainer_Raw_o)
    button_reset_Raw_o.on('click', reset_data)

    wp.elements['button_reset_Raw_o'] = button_reset_Raw_o


    div_getFile_fileName_container_Raw_o = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_o)



    div_getFile_fileName_label_Raw_o = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_o,
                                     text='파일 이름')
    div_getFile_fileName_value_Raw_o = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_o,
                                     id='div_getFile_fileName_value',
                                     text='-')
    div_getFile_filePath_container_Raw_o = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_o)
    div_getFile_filePath_label_Raw_o = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_o,
                                     text='파일 경로')
    div_getFile_filePath_value_Raw_o = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_o,
                                     text='-')




    wp.elements['div_getFile_Raw_o'] = div_getFile_Raw_o
    # wp.elements['div_getFile_title'] = div_getFile_title
    wp.elements['card_getFile_Raw_o'] = card_getFile_Raw_o
    wp.elements['cardSection_getFile_Raw_o'] = cardSection_getFile_Raw_o
    wp.elements['div_getFile_buttonNaming_Raw_o'] = div_getFile_buttonNaming_Raw_o
    wp.elements['button_getFile_Raw_o'] = button_getFile_Raw_o

    wp.elements['div_getFile_fileName_container_Raw_o'] = div_getFile_fileName_container_Raw_o
    wp.elements['div_getFile_fileName_label_Raw_o'] = div_getFile_fileName_label_Raw_o
    wp.elements['div_getFile_fileName_value_Raw_o'] = div_getFile_fileName_value_Raw_o
    wp.elements['div_getFile_filePath_container_Raw_o'] = div_getFile_filePath_container_Raw_o
    wp.elements['div_getFile_filePath_label_Raw_o'] = div_getFile_filePath_label_Raw_o
    wp.elements['div_getFile_filePath_value_Raw_o'] = div_getFile_filePath_value_Raw_o
    
        



   ############### 다섯번째 Section
   
    #div_Raw_d = Div(classes=get_from_df(class_df, 'name', 'div_dsd_converter', 'classes_text'),
    #                        a=div_mainWindow)
    #wp.elements['div_Raw_d'] = div_Raw_d

    # 파일 가져오기

    div_getFile_Raw_d = Div(a=div_internal)
    
    
    card_getFile_Raw_d = QCard(classes=get_from_df(class_df, 'name', 'card_getFile', 'classes_text'),
                         a=div_getFile_Raw_d)
    cardSection_getFile_Raw_d = QCardSection(a=card_getFile_Raw_d)

    div_getFile_buttonContainer_Raw_d = Div(classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
                                      style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
                                      a=cardSection_getFile_Raw_d)
    div_getFile_buttonNaming_Raw_d = Div(text='딜리버리 Data 가져오기',
                                   classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                   style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                   a=div_getFile_buttonContainer_Raw_d)
    button_getFile_Raw_d = QButton(size='md',
                             classes=get_from_df(class_df, 'name', 'div_button_on', 'classes_text'),
                             style=get_from_df(style_df, 'name', 'div_button_on', 'style_text'),
                             text='파일 가져오기',
                             name='Raw_d',
                             a=div_getFile_buttonContainer_Raw_d)
    button_getFile_Raw_d.on('click', load_info_data)

    button_reset_Raw_d = QButton(size='md',
                           classes=get_from_df(class_df, 'name', 'div_button_off', 'classes_text'),
                           style=get_from_df(style_df, 'name', 'div_button_off', 'style_text'),
                           text='초기화',
                           disable=True,
                           name='Raw_d_reset',
                           a=div_getFile_buttonContainer_Raw_d)
    button_reset_Raw_d.on('click', reset_data)

    wp.elements['button_reset_Raw_d'] = button_reset_Raw_d


    div_getFile_fileName_container_Raw_d = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_d)



    div_getFile_fileName_label_Raw_d = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_d,
                                     text='파일 이름')
    div_getFile_fileName_value_Raw_d = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_fileName_container_Raw_d,
                                     id='div_getFile_fileName_value',
                                     text='-')
    div_getFile_filePath_container_Raw_d = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_Raw_d)
    div_getFile_filePath_label_Raw_d = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_d,
                                     text='파일 경로')
    div_getFile_filePath_value_Raw_d = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_filePath_container_Raw_d,
                                     text='-')




    wp.elements['div_getFile_Raw_d'] = div_getFile_Raw_d
    # wp.elements['div_getFile_title'] = div_getFile_title
    wp.elements['card_getFile_Raw_d'] = card_getFile_Raw_d
    wp.elements['cardSection_getFile_Raw_d'] = cardSection_getFile_Raw_d
    wp.elements['div_getFile_buttonNaming_Raw_d'] = div_getFile_buttonNaming_Raw_d
    wp.elements['button_getFile_Raw_d'] = button_getFile_Raw_d

    wp.elements['div_getFile_fileName_container_Raw_d'] = div_getFile_fileName_container_Raw_d
    wp.elements['div_getFile_fileName_label_Raw_d'] = div_getFile_fileName_label_Raw_d
    wp.elements['div_getFile_fileName_value_Raw_d'] = div_getFile_fileName_value_Raw_d
    wp.elements['div_getFile_filePath_container_Raw_d'] = div_getFile_filePath_container_Raw_d
    wp.elements['div_getFile_filePath_label_Raw_d'] = div_getFile_filePath_label_Raw_d
    wp.elements['div_getFile_filePath_value_Raw_d'] = div_getFile_filePath_value_Raw_d

        

    ##### 6번째 섹션
   
    div_mailTable = Div(classes=get_from_df(class_df, 'name', 'div_dsd_converter', 'classes_text'),
                            a=div_mainWindow)
    wp.elements['div_mailTable'] = div_mailTable

    # 파일 가져오기

    div_getFile_mailTable = Div(a=div_mailTable)
    
    
    card_getFile_mailTable = QCard(classes=get_from_df(class_df, 'name', 'card_getFile', 'classes_text'),
                         a=div_getFile_mailTable)
    cardSection_getFile_mailTable = QCardSection(a=card_getFile_mailTable)

    div_getFile_buttonContainer_mailTable = Div(classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
                                      style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
                                      a=cardSection_getFile_mailTable)
    div_getFile_buttonNaming_mailTable = Div(text='메일룸 Table 가져오기',
                                   classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                   style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                   a=div_getFile_buttonContainer_mailTable)
    button_getFile_mailTable = QButton(size='md',
                             classes=get_from_df(class_df, 'name', 'div_button_on', 'classes_text'),
                             style=get_from_df(style_df, 'name', 'div_button_on', 'style_text'),
                             text='파일 가져오기',
                             name='mailTable',
                             a=div_getFile_buttonContainer_mailTable)
    button_getFile_mailTable.on('click', load_info_data)

    button_reset_mailTable = QButton(size='md',
                           classes=get_from_df(class_df, 'name', 'div_button_off', 'classes_text'),
                           style=get_from_df(style_df, 'name', 'div_button_off', 'style_text'),
                           text='초기화',
                           disable=True,
                           name='mailTable_reset',
                           a=div_getFile_buttonContainer_mailTable)
    button_reset_mailTable.on('click', reset_data)

    wp.elements['button_reset_mailTable'] = button_reset_mailTable


    div_getFile_fileName_container_mailTable = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_mailTable)



    div_getFile_fileName_label_mailTable = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_fileName_container_mailTable,
                                     text='파일 이름')
    div_getFile_fileName_value_mailTable = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_fileName_container_mailTable,
                                     id='div_getFile_fileName_value',
                                     text='-')
    div_getFile_filePath_container_mailTable = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_mailTable)
    div_getFile_filePath_label_mailTable = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_filePath_container_mailTable,
                                     text='파일 경로')
    div_getFile_filePath_value_mailTable = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_filePath_container_mailTable,
                                     text='-')




    wp.elements['div_getFile_mailTable'] = div_getFile_mailTable
    # wp.elements['div_getFile_title'] = div_getFile_title
    wp.elements['card_getFile_mailTable'] = card_getFile_mailTable
    wp.elements['cardSection_getFile_mailTable'] = cardSection_getFile_mailTable
    wp.elements['div_getFile_buttonNaming_mailTable'] = div_getFile_buttonNaming_mailTable
    wp.elements['button_getFile_mailTable'] = button_getFile_mailTable

    wp.elements['div_getFile_fileName_container_mailTable'] = div_getFile_fileName_container_mailTable
    wp.elements['div_getFile_fileName_label_mailTable'] = div_getFile_fileName_label_mailTable
    wp.elements['div_getFile_fileName_value_mailTable'] = div_getFile_fileName_value_mailTable
    wp.elements['div_getFile_filePath_container_mailTable'] = div_getFile_filePath_container_mailTable
    wp.elements['div_getFile_filePath_label_mailTable'] = div_getFile_filePath_label_mailTable
    wp.elements['div_getFile_filePath_value_mailTable'] = div_getFile_filePath_value_mailTable
    
        
    print('메일룸 Table 경로를 확인합니다.')
    
    mailTablePath = la.check_mailTable_exist()
    
    if mailTablePath == "Error" :
        pass
    else:
        print('파일 존재 확인')
        print(mailTablePath)
        div_getFile_fileName_value_mailTable.text = mailTablePath.split('/')[-1]
        div_getFile_filePath_value_mailTable.text = '/'.join(mailTablePath.split('/')[:-1])
        
        try:
            button_getFile_mailTable.classes = get_from_df(class_df, 'name', 'div_button_off',
                                                                      'classes_text')
            button_getFile_mailTable.disable = True


            button_reset_mailTable.style = get_from_df(style_df, 'name', 'div_button_on',
                                                                      'style_text')
            button_reset_mailTable.classes = get_from_df(class_df, 'name', 'div_button_on',
                                                                      'classes_text')

            button_reset_mailTable.disable = False

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('ERR', e)
            print(exc_type, fname, exc_tb.tb_lineno)        



    ##### 7번째 섹션
   
    #div_templateXl = Div(classes=get_from_df(class_df, 'name', 'div_dsd_converter', 'classes_text'),
    #                        a=div_mainWindow)
    #wp.elements['div_templateXl'] = div_templateXl

    # 파일 가져오기

    div_getFile_templateXl = Div(a=div_mailTable)
    
    
    card_getFile_templateXl = QCard(classes=get_from_df(class_df, 'name', 'card_getFile', 'classes_text'),
                         a=div_getFile_templateXl)
    cardSection_getFile_templateXl = QCardSection(a=card_getFile_templateXl)

    div_getFile_buttonContainer_templateXl = Div(classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
                                      style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
                                      a=cardSection_getFile_templateXl)
    div_getFile_buttonNaming_templateXl = Div(text='Template 파일 가져오기',
                                   classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                   style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                   a=div_getFile_buttonContainer_templateXl)
    button_getFile_templateXl = QButton(size='md',
                             classes=get_from_df(class_df, 'name', 'div_button_on', 'classes_text'),
                             style=get_from_df(style_df, 'name', 'div_button_on', 'style_text'),
                             text='파일 가져오기',
                             name='templateXl',
                             a=div_getFile_buttonContainer_templateXl)
    button_getFile_templateXl.on('click', load_info_data)

    button_reset_templateXl = QButton(size='md',
                           classes=get_from_df(class_df, 'name', 'div_button_off', 'classes_text'),
                           style=get_from_df(style_df, 'name', 'div_button_off', 'style_text'),
                           text='초기화',
                           disable=True,
                           name='templateXl_reset',
                           a=div_getFile_buttonContainer_templateXl)
    button_reset_templateXl.on('click', reset_data)

    wp.elements['button_reset_templateXl'] = button_reset_templateXl


    div_getFile_fileName_container_templateXl = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_templateXl)



    div_getFile_fileName_label_templateXl = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_fileName_container_templateXl,
                                     text='파일 이름')
    div_getFile_fileName_value_templateXl = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_fileName_container_templateXl,
                                     id='div_getFile_fileName_value',
                                     text='-')
    div_getFile_filePath_container_templateXl = Div(
        classes=get_from_df(class_df, 'name', 'div_getFile_container', 'classes_text'),
        style=get_from_df(style_df, 'name', 'div_getFile_container', 'style_text'),
        a=cardSection_getFile_templateXl)
    div_getFile_filePath_label_templateXl = Div(classes=get_from_df(class_df, 'name', 'div_getFile_label', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_label', 'style_text'),
                                     a=div_getFile_filePath_container_templateXl,
                                     text='파일 경로')
    div_getFile_filePath_value_templateXl = Div(classes=get_from_df(class_df, 'name', 'div_getFile_value', 'classes_text'),
                                     style=get_from_df(style_df, 'name', 'div_getFile_value', 'style_text'),
                                     a=div_getFile_filePath_container_templateXl,
                                     text='-')




    wp.elements['div_getFile_templateXl'] = div_getFile_templateXl
    # wp.elements['div_getFile_title'] = div_getFile_title
    wp.elements['card_getFile_templateXl'] = card_getFile_templateXl
    wp.elements['cardSection_getFile_templateXl'] = cardSection_getFile_templateXl
    wp.elements['div_getFile_buttonNaming_templateXl'] = div_getFile_buttonNaming_templateXl
    wp.elements['button_getFile_templateXl'] = button_getFile_templateXl

    wp.elements['div_getFile_fileName_container_templateXl'] = div_getFile_fileName_container_templateXl
    wp.elements['div_getFile_fileName_label_templateXl'] = div_getFile_fileName_label_templateXl
    wp.elements['div_getFile_fileName_value_templateXl'] = div_getFile_fileName_value_templateXl
    wp.elements['div_getFile_filePath_container_templateXl'] = div_getFile_filePath_container_templateXl
    wp.elements['div_getFile_filePath_label_templateXl'] = div_getFile_filePath_label_templateXl
    wp.elements['div_getFile_filePath_value_templateXl'] = div_getFile_filePath_value_templateXl
    
        
    print('Template 파일 경로를 확인합니다.')
    
    templateXlPath = la.check_templateXl_exist()
    
    if templateXlPath == "Error" :
        pass
    else:
        print('파일 존재 확인')
        print(templateXlPath)
        div_getFile_fileName_value_templateXl.text = templateXlPath.split('/')[-1]
        div_getFile_filePath_value_templateXl.text = '/'.join(templateXlPath.split('/')[:-1])
        
        try:
            button_getFile_templateXl.classes = get_from_df(class_df, 'name', 'div_button_off',
                                                                      'classes_text')
            button_getFile_templateXl.disable = True


            button_reset_templateXl.style = get_from_df(style_df, 'name', 'div_button_on',
                                                                      'style_text')
            button_reset_templateXl.classes = get_from_df(class_df, 'name', 'div_button_on',
                                                                      'classes_text')

            button_reset_templateXl.disable = False

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('ERR', e)
            print(exc_type, fname, exc_tb.tb_lineno)        



    

    # 작업 현황
    dialog_workProcess_dialog = QDialog(v_model='seamless', seamless=True, position='right', a=div_dsd_converter)
    wp.elements['dialog_workProcess_dialog'] = dialog_workProcess_dialog

    # cardSection_workProcess_container1 = QCardSection(classes="no-padding items-center no-wrap bg-white", a=dialog_workProcess_dialog)
    # wp.elements['cardSection_workProcess_container1'] = cardSection_workProcess_container1
    #
    # button_workProcess_dialogClose = QButton(flat=True, round=True, icon='close', v_close_popup=True,
    #                                            a=cardSection_workProcess_container1)
    # wp.elements['button_workProcess_dialogClose'] = button_workProcess_dialogClose

    card_workProcess_container = QCard(style='min-width: 280px', a=dialog_workProcess_dialog)
    wp.elements['card_workProcess_conatiner'] = card_workProcess_container

    cardSection_workProcess_container2 = QCardSection(classes="q-pa-md items-center no-wrap bg-grey-9",
                                                      a=card_workProcess_container)
    wp.elements['cardSection_workProcess_container2'] = cardSection_workProcess_container2

    circularProgress_workProgress = QCircularProgress(value=0, size='20px', thickness='0.2', color='white',
                                                      track_color='grey-9', classes='row inline',
                                                      a=cardSection_workProcess_container2)
    wp.elements['circularProgress_workProgress'] = circularProgress_workProgress

    div_workProgress_circularProgressComment = QDiv(text='진행 중',
                                                    classes='q-ml-md row inline text-white vertical-middle',
                                                    style='font-size: 15px;', a=cardSection_workProcess_container2)
    wp.elements['div_workProgress_circularProgressComment'] = div_workProgress_circularProgressComment

    cardSection_workProcess_container3 = QCardSection(classes="items-center no-wrap bg-white",
                                                      a=card_workProcess_container)
    wp.elements['cardSection_workProcess_container3'] = cardSection_workProcess_container3

    div_workProcess_dashboard = Div(a=cardSection_workProcess_container3)
    wp.elements['div_work_process_dashboard'] = div_workProcess_dashboard

    for index, row in work_process_df.iterrows():
        process_en = row['process_name_en']
        process_ko = row['process_name_ko']

        div_process_container = Div(classes="", style='', a=div_workProcess_dashboard)

        div_process_label = Div(text=process_ko, classes="row inline vertical-middle",
                                style=get_from_df(style_df, 'name', 'div_process_label', 'style_text'),
                                a=div_process_container)

        div_process_value = QButton(round=True, color='light-green-13', size='5px',
                                    classes='q-ml-lg hidden vertical-middle', a=div_process_container)

        wp.elements[f'div_process_container_{process_en}'] = div_process_container
        wp.elements[f'div_process_label_{process_en}'] = div_process_label
        wp.elements[f'div_process_value_{process_en}'] = div_process_value

    # 작업 완료

    dialog_workDone_dialog = QDialog(v_model='alert', a=div_dsd_converter)
    wp.elements['dialog_workDone_dialog'] = dialog_workDone_dialog

    card_workDone_container = QCard(style='min-width: 280px', a=dialog_workDone_dialog)
    wp.elements['card_workDone_conatiner'] = card_workDone_container
    cardSection_workDone_container = QCardSection(
        classes="q-pa-md items-center no-wrap bg-white",
        a=card_workDone_container)
    wp.elements['cardSection_workDone_container2'] = cardSection_workDone_container

    div_workDone_text = Div(
        text='',
        classes='row inline',
        a=cardSection_workDone_container)
    wp.elements['div_workDone_text'] = div_workDone_text

    # 개발 목적 로그인 스킵
    flag_skip_login = 1
    if flag_skip_login:
        # wp.elements['div_checkEmployee'].set_class('hidden')
        wp.elements['div_dsd_converter'].remove_class('hidden')
        # wp.elements['tabs_tabs'].value = 'DSD Wizard'
        # wp.elements['tab_tabs_dsd_converter'].disable = False
        # wp.elements['tab_tabs_dsd_analyzer'].disable = False


    return wp


def run_jp(q):
    pid = os.getpid()
    q.put(pid)
    wp = justpy(main)


def run_webview():
    def on_closed():
        print('webview window closed')
        print('bye')

    window = webview.create_window(
        'KMPNS Valet',
        url=URL_jp,
        x=0,
        y=0,
        min_size=(1000, 1000)
    )

    # window.events.loaded += on_loaded
    window.events.closed += on_closed

    webview.start()




if __name__ == '__main__':
    # multiprocessing.freeze_support()
    # p1 = Process(target=manager)
    # print('start manager process')
    # p1.start()
    # p1.join()

    wp = justpy(main)