#-*- coding: utf-8 -*-

import openpyxl as xl
import pandas as pd
import numpy as np
import os
import sys
import datetime
from dateutil.parser import parse
from openpyxl.utils.dataframe import dataframe_to_rows
#import win32com.client
#win =win32com.client.Dispatch("Excel.Application")

# CU 경로설정
if getattr(sys, 'frozen', False):
    #test.exe로 실행한 경우,test.exe를 보관한 디렉토리의 full path를 취득
    program_directory = os.path.dirname(os.path.abspath(sys.executable))
    cwd = os.path.dirname(os.path.abspath(sys.executable))
    Path_ = os.path.dirname(os.path.abspath(sys.executable))
    Save_path_app = os.path.abspath(os.path.join(Path_, os.pardir))
else:
    #python test.py로 실행한 경우,test.py를 보관한 디렉토리의 full path를 취득
    program_directory = os.path.dirname(os.path.abspath(__file__))
    cwd = os.path.dirname(os.path.abspath(__file__))
    Path_ = os.path.dirname(os.path.abspath(__file__))
    Save_path_app = os.path.dirname(os.path.abspath(__file__))


    
#CU 현재 작업 디렉토리를 변경
os.chdir(program_directory)

#현재 exe또는 py 디렉토리에 저장시키기

## CU 폴더 생성하는 함수
def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory.")



## CU 테이블 파일이 존재하는지 확인하는 함수
def check_mailTable_exist():
    path_root = program_directory
    print('프로그램실행경로 : ' + path_root)
    valetTablePath = path_root+"/"+'KMPNS_메일룸_Table.xlsx'
    parentPath = os.path.join(path_root, os.pardir)
    valetTableParent = os.path.abspath(parentPath+"/"+'KMPNS_메일룸_Table.xlsx')
    
    if os.path.isfile(valetTablePath) :
        print('테이블 존재를 확인하였습니다.')
        valetTableXl = valetTablePath
        return valetTableXl.replace('\\','/')
    elif os.path.isfile(valetTableParent) :
        print('테이블 존재를 확인하였습니다.')
        valetTableXl = valetTableParent.replace('\\','/')
        return valetTableXl            
    else :
        print('메일룸 테이블이 경로에 없습니다.')
        return "Error"



def check_templateXl_exist():
    path_root = program_directory
    print('프로그램실행경로 : ' + path_root)
    ValettemplPath = path_root+"/"+'KMPNS_메일룸_Template.xlsx'
    parentPath2 = os.path.join(path_root, os.pardir)
    ValettemplParent = os.path.abspath(parentPath2+"/"+'KMPNS_메일룸_Template.xlsx')
        
    if os.path.isfile(ValettemplPath) :
        print('템플릿 존재를 확인하였습니다.')
        ValettemplPath = ValettemplPath.replace('\\','/')
        return ValettemplPath
    elif os.path.isfile(ValettemplParent) :
        print('테이블 존재를 확인하였습니다.')
        ValettemplParent = ValettemplParent.replace('\\','/')
        return ValettemplParent             
    else :
        print('템플릿이 경로에 없습니다.')
        return "Error"
        


# CU Range로 파일 가져오기
class getRngTable(object):

    def __init__(self, file_full_path, rngName):

        # file_full_path 속성 정의 -> 파일 경로를 속성으로 정의
        self.file_full_path = file_full_path
        
        # rngName 속성 정의 -> 이름정의를 속성으로 정의
        self.rngName = rngName
        
        # xls 속성 정의 -> 실제로 엑셀 파일을 불러와서 속성으로 정의함
        self.xls = xl.load_workbook(self.file_full_path,read_only=False, keep_vba=True,data_only=True)
        
        # rngName으로 받은 table 정보 가져오기
        address = list(self.xls.defined_names[rngName].destinations)

        # rngName의 sheet name 가져오기
        self.input_sh_nm = address[0][0]

        # rngName의 table 위치 가져오기
        self.cellAddress = address[0][1]


#### import된 input_data를 df으로 변환 ####
    def input_to_df(self):                                                                        

        # wb에 input 한 파일 지정
        wb = self.xls
        rngName = self.rngName
        
        # input_sh_nm / cellAddress 변수에 값 지정 및 $ 문자를 address 변수에서 제거
        input_sh_nm = self.input_sh_nm
        cellAddress = self.cellAddress.replace('$','')

        # 엑셀 상 input_data를 list에 추가하기     
        worksheet = wb[input_sh_nm]
        data_rows = []

        for i in range(0,len(worksheet[cellAddress])):
            data_cols = []

            for item in worksheet[cellAddress][i]:
                data_cols.append(item.value)

            # 첫행이 입력된 행까지만 list에 추가
            if data_cols[1] is not None :
                data_rows.append(data_cols)

        # pandas dataframe에 넣어주기
        df = pd.DataFrame(data_rows)

        # Pandas column 설정
        df = df.rename(columns=df.iloc[0]) 
        
        # 첫번째 행 지우기
        df = df.drop(df.index[0]) 

        print(f'{rngName}이 Input되었습니다.')

        return df







# 기본 설정
def Get_Setting_Data(Table_set):
        DateTable = Table_set[Table_set['구분']=='기간']
        ReportTable = Table_set[Table_set['구분']=='보고일자']
        Fix_Table = Table_set[Table_set['구분']=='기본요금']
        Ex_Table = Table_set[Table_set['구분']=='추가요금']
        Ex_count_Table = Table_set[Table_set['구분']=='추가요금 기준건수']
        Fee_Table = Table_set[Table_set['구분']=='요금']
        Date_ = DateTable['값'].iloc[0]
        Report_Date = ReportTable['값'].iloc[0]
        Flat_Rate = Fix_Table['값'].iloc[0]
        Ex_Rate = Ex_Table['값'].iloc[0]
        Ex_Count = Ex_count_Table['값'].iloc[0]
        Fee = Fee_Table['값'].iloc[0]
        
        
        return Date_, Report_Date, Flat_Rate, Ex_Rate, Ex_Count, Fee


def Get_Table_Mailroom(Raw_h,Raw_d,Raw_s,Raw_o,Raw_t,Table_premium,Table_name,Table_account, Table_price, Table_Formula):
        # 헤더 가공
        header_h = Raw_h.iloc[0]
        Raw_h = Raw_h[1:]
        Raw_h.columns = header_h

        Raw_d_rev = Raw_d # 딜리버리 매출 계산용
        
        header_d = Raw_d.iloc[2]
        Raw_d = Raw_d[3:]
        Raw_d.columns = header_d

        # 필요없는 열 제거
        # 필요한 열을 선택하여 새로운 DataFrame 생성
        Raw_o = Raw_o[
        [
                '운송장번호', '생성일시', '주문상태', '착불여부', '편도/왕복', '배송수단', '그룹명',
                '이용사유', '주문자 이름', '출발지 주소', '도착지 주소', '상품', '물품정보(유의사항)',
                '결제금액', '결제타입'
        ]
        ]


                
        # 20240716 주문데이터 에서 특정 키워드 제외
        Raw_o = Raw_o[Raw_o['그룹명']!='.']
        Raw_o = Raw_o[Raw_o['착불여부']!='착불']
        Raw_o = Raw_o[Raw_o['주문상태']!='취소']
        Raw_o = Raw_o[~Raw_o['결제타입'].isin(['카드 등록 결제', '현장결제'])]

        # 20240716 주문데이터 전처리
        Raw_o['그룹명'] = Raw_o['그룹명'].str.strip()
        Raw_o.fillna(0,inplace=True)
        
        #20240716 회사명 테이블 정리
        Table_name.columns = ['그룹명', '회사명']
        Error_Table_name = Table_name[Table_name.duplicated(subset = '그룹명')]
        if Error_Table_name['그룹명'].count() != 0:
                with pd.ExcelWriter(Save_path_ + r'/회사명 중복 확인.xlsx') as writer:
                        Error_Table_name.to_excel(writer, sheet_name='회사명중복')
                raise Exception('중복 입력된 회사명 히스토리(고객사 입력 회사명)가 있습니다. 회사명 테이블을 확인하시어 중복값을 제거해주세요.')
        else:
                pass
        
        #20240716 프리미엄 테이블 정리
        Table_premium = Table_premium[['빌딩명', '이름', '프리미엄 상태', '요금 타입']]
        Table_premium = Table_premium.fillna('')
        Table_premium_on = Table_premium[Table_premium['프리미엄 상태']=='서비스 중']
        
        #완전성 확인
        Raw_o = pd.merge(Raw_o,Table_name, on='그룹명', how='left')
        Raw_o['그룹명'].fillna('Error', inplace=True)
        Error_Table = Raw_o[Raw_o['그룹명']=='Error']
        if Error_Table['그룹명'].count() != 0:
                with pd.ExcelWriter(Save_path_ + r'/예외사항_회사명 테이블에 없는 그룹명.xlsx') as writer:
                        Error_Table.to_excel(writer, sheet_name='회사명 테이블 업데이트')
                raise Exception('확인되지 않은 고객명이 식별되었습니다. 회사명 테이블을 확인해주세요.')
        else:
                pass
        
        Table_premium.columns = ['빌딩명', '회사명', '프리미엄 상태', '요금 타입']
        Error_Compnm = pd.merge(Raw_o,Table_premium, on='회사명', how='left')
        Error_Compnm['빌딩명'].fillna('Error',inplace=True)
        Error_Compnm = Error_Compnm[Error_Compnm['빌딩명']=='Error']
        if Error_Compnm['빌딩명'].count() != 0:
                with pd.ExcelWriter(Save_path_ + r'/예외사항_입주사 테이블에 없는 그룹명.xlsx') as writer:
                        Error_Compnm.to_excel(writer, sheet_name='입주사 테이블 업데이트')
                raise Exception('입주사 테이블에 누락된 고객명이 식별되었습니다. 입주사 테이블을 확인해주세요.')
        else:
                pass

        Error_account=pd.merge(Table_premium, Table_account, on='빌딩명', how='left')
        Error_account['소재지'].fillna('Error',inplace=True)
        Error_account = Error_account[Error_account['소재지']=='Error']
        if Error_account['소재지'].count() != 0:
                with pd.ExcelWriter(Save_path_ + r'/예외사항_소재지 테이블에 없는 빌딩명.xlsx') as writer:
                        Error_Compnm.to_excel(writer, sheet_name='소재지 테이블 업데이트')
                raise Exception('소재지 테이블에 누락된 빌딩명이 식별되었습니다. 소재지 테이블을 확인해주세요.')
        else:
                pass

        # 날짜 데이터 입력
        #Raw_o['생성일시'] = Raw_o['생성일시'].str.replace('오전','AM')
        #Raw_o['생성일시'] = Raw_o['생성일시'].str.replace('오후','PM')
        #Raw_o['생성일시'] = Raw_o['생성일시'].str.replace('\. ','-', regex=True)
        #Raw_o['생성일시'] = pd.to_datetime(Raw_o['생성일시'] , format='%Y-%m-%d %p %I:%M:%S')
        #Raw_o['생성일시'] = pd.to_datetime(Raw_o['생성일시'].replace('\..*','',regex=True) , format='%Y-%m-%d %I:%M:%S %p')
        Raw_o['생성일시'] = pd.to_datetime(Raw_o['생성일시'] , format='%Y-%m-%d %H:%M:%S')
        Raw_o['신청날짜'] = pd.to_datetime(Raw_o['생성일시']).dt.date
        Raw_o['신청시간'] = pd.to_datetime(Raw_o['생성일시']).dt.time

        # 추가필요 열 가공 20240716 필요없어보이지만 남겨둠
        Raw_o['결제완료여부'] = 0
        Raw_o['카드, 착불'] = np.where(Raw_o['결제타입'].str.contains('카드'), 'O', 'X')

                
        # 운송사 데이터 입력
        Raw_o['운송사'] = np.where(
                                Raw_o['운송장번호'].str.startswith('3-', na=False), #20240716 2-에서 3-으로 수정
                                '24시화물',
                                np.where(
                                        '택배' == Raw_o['배송수단'],
                                        '택배', 
                                        # np.where('오토바이 급송' == Raw_o['배송수단'], # 확인필요. 정산서에 안쓰는 부분
                                                #np.where(
                                                 #       '24시화물' != Raw_o['물품정보(유의사항)'], # 확인필요. 정산서에 안쓰는 부분인듯
                                                        '손자KMC')
                                                  #      'Error'),
                                                #'Error')
                                        #)
                                )
        Raw_o['마진율'] = np.where(
                                Raw_o['운송사']=='택배',
                                0.09,
                                np.where(
                                        Raw_o['운송사']=='손자KMC',
                                        0.23,
                                        np.where(
                                                Raw_o['운송사']=='24시화물',
                                                0.15,
                                                'Error'
                                                )
                                        )
                                )


        # join 전 가공
        ##택배 Raw 데이터 가공
        # price_dict = {'극소': 4500, '소': 4500, '중': 6000, '대': 9000, '대1': 9000}
        price_dict = Table_price.set_index('구분')['금액'].to_dict() # 테이블에서 읽어오도록 함
        Raw_t.rename(columns={'운송장번호':'운송장번호'},inplace=True)
        Raw_t.rename(columns={'박스타입':'운임타입'},inplace=True)
        Raw_t = Raw_t[['운송장번호','운임타입']]
        Raw_t['청구가(부가세제외)_t'] = Raw_t['운임타입'].map(price_dict)


        ## 손자 Raw 데이터 가공
        Raw_s.rename(columns={'오더번호':'운송장번호'}, inplace=True)
        Raw_s['청구가(부가세제외)_s'] = Raw_s['고객적용요금']*(1-Raw_s['할인율']/100)
        Raw_s['원가(부가세제외)_s'] = Raw_s['고객적용요금']*(1-Raw_s['수수료율']/100)
        Raw_s = Raw_s[['운송장번호','청구가(부가세제외)_s','원가(부가세제외)_s','거리-km']]

        ## 화물 Raw 데이터 가공
        Raw_h.rename(columns={'화물번호':'운송장번호', '운송료':'원가(부가세제외)_h'}, inplace=True)
        Raw_h['청구가(부가세제외)_h'] = np.floor(Raw_h['원가(부가세제외)_h'] / 0.85 / 100) * 100     
        Raw_h = Raw_h[['운송장번호','원가(부가세제외)_h','차량종류','청구가(부가세제외)_h']]

        # JOIN

        Raw_o['운송장번호'] = Raw_o['운송장번호'].astype(str)
        Raw_s['운송장번호'] = Raw_s['운송장번호'].astype(str)
        Raw_t['운송장번호'] = Raw_t['운송장번호'].astype(str)

        Raw_o = pd.merge(Raw_o,Raw_t, on='운송장번호', how='left')
        Raw_o = pd.merge(Raw_o,Raw_s, on='운송장번호', how='left')
        Raw_o = pd.merge(Raw_o,Raw_h, on='운송장번호', how='left')
        Raw_o.fillna(0,inplace=True)
        
        
        # condition = (Raw_o['배송수단'] != '택배') & (Raw_o['운송사'] == '손자KMC') & (Raw_o['청구가(부가세제외)_s'] < 6364) # 6364원 미만 손자퀵 6363.636364 << 20240730 로직삭제
        # Raw_o.loc[condition, '청구가(부가세제외)_s'] = 6363.636364

                
        # JOIN 후 가공

        Raw_o['운임타입'] = np.where(Raw_o['배송수단']=='택배',
                                Raw_o['운임타입'],
                                np.where(                               
                                        Raw_o['배송수단']=='오토바이 급송',
                                        '급송',
                                        '일반'
                                        )
                                )
        Raw_o['청구가(부가세제외)'] = np.where(Raw_o['운송사']=='24시화물', Raw_o['결제금액']/1.1, # np.where(Raw_o['운송사']=='24시화물', Raw_o['청구가(부가세제외)_h'],
                                
                                np.where(Raw_o['운송사']=='손자KMC', Raw_o['결제금액']/1.1, #  np.where(Raw_o['운송사']=='손자KMC', Raw_o['청구가(부가세제외)_s']
                                np.where(Raw_o['운송사']=='택배', Raw_o['청구가(부가세제외)_t'], 'Error')))

        Raw_o['청구가(부가세제외)'] =Raw_o['청구가(부가세제외)'].astype(float)

        Raw_o['원가(부가세제외)'] = np.where(Raw_o['운송사']=='24시화물', Raw_o['원가(부가세제외)_h'],
                                np.where(Raw_o['운송사']=='손자KMC', Raw_o['원가(부가세제외)_s'],
                                np.where(Raw_o['운송사']=='택배', Raw_o['청구가(부가세제외)_t']/1.1, 'Error')))

        Raw_o['원가(부가세제외)']=Raw_o['원가(부가세제외)'].astype(float)

        Raw_o['원가(부가세)'] = np.where(Raw_o['운송사']=='손자KMC', 0,
                                        Raw_o['원가(부가세제외)']/10)

        Raw_o['원가(부가세)'] = Raw_o['원가(부가세)'].astype(float)

        Raw_o['원가(합계)'] = Raw_o['원가(부가세제외)'].astype(float) + Raw_o['원가(부가세)'].astype(float)
        Raw_o['마진'] = Raw_o['청구가(부가세제외)'].astype(float) - Raw_o['원가(부가세)'].astype(float)

        Raw_o.drop(
                ['청구가(부가세제외)_t',
                '청구가(부가세제외)_s',
                '청구가(부가세제외)_h',
                '원가(부가세제외)_s',
                '원가(부가세제외)_h'],  
                axis=1, inplace=True)

        Raw_o['차량정보'] = np.where(Raw_o['운송사']=='택배','택배',
                        np.where(Raw_o['운송사']=='손자KMC',
                                        np.where(Raw_o['배송수단'].str.contains('다마스'),'다마스','일반'), #배송수단으로
                        np.where(Raw_o['운송사']=='24시화물',Raw_o['차량종류'],'Error')))
        
        Year_ = pd.to_datetime(Raw_o['신청날짜']).dt.year
        Weak_ = pd.to_datetime(Raw_o['신청날짜']).dt.strftime('%U')

        Raw_o['주차'] = Year_.astype(str) + '-W' + Weak_.astype(str)
        Raw_o['날짜'] = pd.to_datetime(Raw_o['신청날짜']).dt.day
        Raw_o_nodata = Raw_o[Raw_o['청구가(부가세제외)']==0]
        Raw_o = Raw_o[Raw_o['청구가(부가세제외)']!=0]
        Raw_o.to_excel(Save_path_+'\\' + 'RPA_Results.xlsx')  #저장경로
        Raw_o_nodata.to_excel(Save_path_+'\\' + 'RPA_Results_NoTransitData.xlsx') #저장경로
        
        
        Raw_d_Report = Raw_d[['년월','년월일','건별','월정액','무료','주차']]
        Raw_d_Report.fillna(0,inplace=True)
        Raw_d_Report = Raw_d_Report[Raw_d_Report['년월']!=0]
        
        # 월정액 매출 계산
        
        header_dm = Raw_d_rev.iloc[1]
        Raw_dm = Raw_d_rev[2:]
        Raw_dm.columns = header_dm
        
        header_d2 = Raw_d_rev.iloc[2]
        Raw_d_rev = Raw_d_rev[3:]
        Raw_d_rev.columns = header_d2

        Raw_d_M=Raw_dm[['월정액']]
        Raw_d_M.fillna(0,inplace=True)
        
        ## 헤더 추출
        Raw_d_M = Raw_d_M.iloc[0]
        list_d = Raw_d_M.to_list()
        list_d.append('년월')
        
        ## 정액제 계산 대상 회사 추출
        Raw_d_fee=Raw_d_rev[list_d]
        Raw_d_fee.fillna(0,inplace=True)
        pivot_d = Raw_d_fee.pivot_table(
                                        values=list_d
                                          ,index='년월'
                                          ,aggfunc='sum')
        for M_compn in list_d:
                if M_compn == '년월':
                        pass
                else:
                        pivot_d.loc[pivot_d[M_compn] < Ex_Count, 'R_' + M_compn] = Flat_Rate
                        pivot_d.loc[pivot_d[M_compn] >= Ex_Count, 'R_' + M_compn] = Flat_Rate + (pivot_d[M_compn]-Ex_Count)*Ex_Rate

        ## 합산
        R_list_d = []
        for old_column in list_d:
                if old_column == '년월':
                        pass
                else:
                        R_list_d.append('R_'+old_column)
        pivot_d['월정액_Sum'] = 0
        
        for each_compn in R_list_d:
                pivot_d['월정액_Sum'] =pivot_d['월정액_Sum'] + pivot_d[each_compn]
        
        
        pivot_d.reset_index(inplace=True)

        pivot_d = pivot_d[['년월','월정액_Sum']]
        Raw_d_merged = pd.merge(Raw_d_Report,pivot_d,on='년월',how='left')
        Raw_d_merged.to_excel(Save_path_+ '\\' + 'RPA_Results_Delivery.xlsx')
        
        return Raw_o, Raw_d, Table_premium, Table_premium_on

def Mail_Room_def(Date_, Report_Date, Flat_Rate, Ex_Rate, Ex_Count, Fee, Raw_o, Raw_d, Table_premium, Table_premium_on, Table_Formula):    


        #프리미엄 딜리버리 가공
        Raw_d = Raw_d[Raw_d['년월']==Date_]
        Company_name = Raw_o['회사명'].unique().tolist()
        Company_name_2 = pd.DataFrame(Raw_o['회사명'].unique(), columns = ['이름'])
        Company_name_2['포함'] = 'O'
        Premium_only = pd.merge(Table_premium_on, Company_name_2, on='이름', how='left')
        Premium_only['포함'].fillna('X',inplace=True)
        Premium_only = Premium_only[Premium_only['포함']=='X']

        # openpyxl

        for CompNm in Company_name:
                
                

                wb_mailroom = xl.load_workbook(dir_temp)
                #ws_o = wb_mailroom['RAW']
                ws_p = wb_mailroom['운영보고서']
                ws_p['C4'] = Report_Date
                # RAW 데이터 붙여넣기                
                Filtered_Raw_o = Raw_o[Raw_o['회사명']==CompNm]
                Filtered_Raw_o = Filtered_Raw_o[['신청날짜','주문자 이름','이용사유','출발지 주소','도착지 주소','배송수단','편도/왕복','청구가(부가세제외)']]
                #for r_idx, row in enumerate(dataframe_to_rows(Filtered_Raw_o,in도착지, 1):
                #        for c_idx, value in enumerate(row, 1):
                #                ws_o.cell(row=r_idx, column=c_idx, value=value)
                
                                
                ws_q = wb_mailroom['퀵발송']
                Quick_Raw_o = Filtered_Raw_o[Filtered_Raw_o['배송수단']!='택배'] # 20240716 해당없음(택배) > 택배
                Row_count_q = Quick_Raw_o['배송수단'].count()
                if Row_count_q != 0:
                        header_q = Quick_Raw_o.iloc[0]
                        Quick_Raw_o = Quick_Raw_o[1:]
                        Quick_Raw_o.columns = header_q
                        
                        for r_idx, row in enumerate(dataframe_to_rows(Quick_Raw_o,index=False,header=True), 1):
                                for c_idx, value in enumerate(row, 1):
                                        ws_q.cell(row=r_idx+3, column=c_idx+1, value=value)
                
                Target_row = 4
                End_Row_q = Row_count_q + Target_row
                ws_q.delete_rows(End_Row_q, 197-Row_count_q - 1)        
                ws_q['I'+str(Row_count_q+7-1)] = '=SUM(I4:I' + str(Row_count_q+6-2) +')'
                ws_q['I'+str(Row_count_q+7)] = '=' + 'I' + str(Row_count_q+7+1-2) + '*10%'
                ws_q['I'+str(Row_count_q+7-2)] = '=SUM(' + 'I'+str(Row_count_q+7+1-2) + ':' + 'I'+str(Row_count_q+7+2-2) + ')'
                                
                ws_t = wb_mailroom['택배발송']
                TB_Raw_o = Filtered_Raw_o[Filtered_Raw_o['배송수단']=='택배'] #20240716 해당없음(택배) > 택배
                Row_count_T = TB_Raw_o['배송수단'].count()
                if Row_count_T != 0:
                        header_TB = TB_Raw_o.iloc[0]
                        TB_Raw_o = TB_Raw_o[1:]
                        TB_Raw_o.columns = header_TB
                
                        for r_idx, row in enumerate(dataframe_to_rows(TB_Raw_o,index=False,header=True), 1):
                                for c_idx, value in enumerate(row, 1):
                                        ws_t.cell(row=r_idx+3, column=c_idx+1, value=value)                   
                
                Target_row = 4
                End_Row_t = Row_count_T + Target_row
                ws_t.delete_rows(End_Row_t, 97-Row_count_T - 1)  
                ws_t['I'+str(Row_count_T+7+1-2)] = '=SUM(I4:I' + str(Row_count_T+6-2) +')'
                ws_t['I'+str(Row_count_T+7+2-2)] = '=' + 'I' + str(Row_count_T+7+1-2) + '*10%'
                ws_t['I'+str(Row_count_T+7-2)] = '=SUM(' + 'I'+str(Row_count_T+7+1-2) + ':' + 'I'+str(Row_count_T+7+2-2) + ')'
                
                ws_p['F12'] = '=퀵발송!I' + str(Row_count_q+7-1)
                ws_p['F13'] = '=택배발송!I' + str(Row_count_T+7-1)
                Table_premium_tower = Table_premium[Table_premium['회사명']==CompNm]
                Tower = Table_premium_tower['빌딩명'].iloc[0]
                
                ws_p['B2']= Tower +' 얼른 딜리버리 사용 내역서'
                ws_p['C5']= Table_account[Table_account['빌딩명']==Tower]['소재지'].iloc[0]
                
                ws_d = wb_mailroom['일자별배송건수']
                ws_d['C3']=CompNm
                
                Filtered_Table_p = Table_premium_on[Table_premium_on['이름']==CompNm]
                if Filtered_Table_p['이름'].count() != 0:

                        formula_dict = Table_Formula.set_index('구분')['수식'].to_dict()
                        Filtered_Table_p['수식'] = Filtered_Table_p['빌딩명'].map(formula_dict)
                        Filtered_Table_p['수식'].fillna(0,inplace=True)
                        ws_p['E17'] = Filtered_Table_p['수식'].iloc[0]
                        
                        if Filtered_Table_p['요금 타입'].iloc[0] == '건별(500)':
                                ws_p['D17'] = '건별 요금제'
                        #        ws_p['E17'] = '=' + str(Fee) + '*C17'
                        elif Filtered_Table_p['요금 타입'].iloc[0] == '월이용료':
                                ws_p['D17'] = '정액제'

                        elif Filtered_Table_p['요금 타입'].iloc[0] == '무료':
                                ws_p['D17'] = '무료'
                        #        ws_p['E17'] = 0
                        else:
                                pass
                        
                        # 프리미엄 배송데이터
                        Filtered_Raw_d = Raw_d[['년월일', CompNm]]
                        
                        for r_idx, row in enumerate(dataframe_to_rows(Filtered_Raw_d,index=False,header=True), 1):
                                for c_idx, value in enumerate(row, 1):
                                        ws_d.cell(row=r_idx+2, column=c_idx+1, value=value)
                                        


                        ws_p['B17'] = '프리미엄 서비스'
                        
                
                filename = '\\' + CompNm+ ')'+ Tower + ' 얼른 딜리버리_' + Date_[-2:] + '월 이용내역_KMPNS.xlsx'

                
                

                wb_mailroom.save(Save_path_+filename)
                print(filename + ' 생성 완료')
                

        for CompNm_p in Premium_only['이름'].unique().tolist():
                #20230204수정: 프리미엄 배송 건만 있는 거래처도 생성
        
                wb_mailroom = xl.load_workbook(dir_temp)
                #ws_o = wb_mailroom['RAW']
                ws_p = wb_mailroom['운영보고서']
                ws_p['C4'] = Report_Date
                # RAW 데이터 붙여넣기                
                        
                ws_q = wb_mailroom['퀵발송']
                Row_count_q = 0
                Target_row = 4
                End_Row_q = Row_count_q + Target_row
                ws_q.delete_rows(End_Row_q, 197-Row_count_q - 1)        
                ws_q['I'+str(Row_count_q+7-1)] = '=SUM(I4:I' + str(Row_count_q+6-2) +')'
                ws_q['I'+str(Row_count_q+7)] = '=' + 'I' + str(Row_count_q+7+1-2) + '*10%'
                ws_q['I'+str(Row_count_q+7-2)] = '=SUM(' + 'I'+str(Row_count_q+7+1-2) + ':' + 'I'+str(Row_count_q+7+2-2) + ')'
                                
                ws_t = wb_mailroom['택배발송']  
                       
                Row_count_T = 0
                Target_row = 4
                End_Row_t = Row_count_T + Target_row
                ws_t.delete_rows(End_Row_t, 97-Row_count_T - 1)  
                ws_t['I'+str(Row_count_T+7+1-2)] = '=SUM(I4:I' + str(Row_count_T+6-2) +')'
                ws_t['I'+str(Row_count_T+7+2-2)] = '=' + 'I' + str(Row_count_T+7+1-2) + '*10%'
                ws_t['I'+str(Row_count_T+7-2)] = '=SUM(' + 'I'+str(Row_count_T+7+1-2) + ':' + 'I'+str(Row_count_T+7+2-2) + ')'
                
                ws_p['F12'] = '=퀵발송!I' + str(Row_count_q+7-1)
                ws_p['F13'] = '=택배발송!I' + str(Row_count_T+7-1)
                Table_premium_tower = Table_premium[Table_premium['회사명']==CompNm_p]
                Tower = Table_premium_tower['빌딩명'].iloc[0]
                
                ws_p['B2']= Tower +' 얼른 딜리버리 사용 내역서'
                ws_p['C5']= Table_account[Table_account['빌딩명']==Tower]['소재지'].iloc[0]
                
                ws_d = wb_mailroom['일자별배송건수']
                ws_d['C3']=CompNm_p
                
                Filtered_Table_p = Table_premium_on[Table_premium_on['이름']==CompNm_p]
                if Filtered_Table_p['이름'].count() != 0:
                        if Filtered_Table_p['요금 타입'].iloc[0] == '건별(500)':
                                ws_p['D17'] = '건별 요금제'
                        #         ws_p['E17'] = '=' + str(Fee) + '*C17'
                        elif Filtered_Table_p['요금 타입'].iloc[0] == '월이용료':
                                ws_p['D17'] = '정액제'
                        #         ws_p['E17'] = '=' + str(Flat_Rate)+'+IF(C17>' + str(Ex_Count) + ',(C17-' + str(Ex_Count) + ')*' + str(Ex_Rate) +',0)'
                        elif Filtered_Table_p['요금 타입'].iloc[0] == '무료':
                                ws_p['D17'] = '무료'
                        #         ws_p['E17'] = 0
                        else:
                                pass

                        formula_dict = Table_Formula.set_index('구분')['수식'].to_dict()
                        Filtered_Table_p['수식'] = Filtered_Table_p['빌딩명'].map(formula_dict)
                        Filtered_Table_p['수식'].fillna(0,inplace=True)
                        ws_p['E17'] = Filtered_Table_p['수식'].iloc[0]
                        
                        # 프리미엄 배송데이터
                        if CompNm_p in Raw_d.columns.tolist():
                                Filtered_Raw_d = Raw_d[['년월일', CompNm_p]]
                                
                                for r_idx, row in enumerate(dataframe_to_rows(Filtered_Raw_d,index=False,header=True), 1):
                                        for c_idx, value in enumerate(row, 1):
                                                ws_d.cell(row=r_idx+2, column=c_idx+1, value=value)
                                        


                        ws_p['B17'] = '프리미엄 서비스'
                        
                
                filename = '\\' + CompNm_p+ ')'+ Tower + ' 얼른 딜리버리_' + Date_[-2:] + '월 이용내역_KMPNS.xlsx'

                
                

                wb_mailroom.save(Save_path_+filename)
                print(filename + ' 생성 완료')
                


if __name__ == '__main__':
        
        #Input파일
        Dir_Raw_h = r'\input\Data_24시화물.xlsx'
        Dir_Raw_d = r'\input\Data_딜리버리.xlsx'
        Dir_Raw_s = r'\input\Data_손자.csv'
        Dir_Raw_o = r'\input\Data_신청내역.xlsx'
        Dir_Raw_t = r'\input\Data_택배2.xlsx'
        
        #기본파일
        mailTableXl = 'KMPNS_메일룸_Table.xlsx'
        dir_temp = 'KMPNS_메일룸_Template.xlsx'
        
        Dir_Table_premium = getRngTable(mailTableXl, 'Company')    #'\Table_입주사.xlsx'
        Dir_Table_name = getRngTable(mailTableXl, 'GoogleName')    #'\Table_회사명.xlsx'
        Dir_Table_account = getRngTable(mailTableXl, 'Location')   #'\Table_소재지.csv'
        Dir_Table_setting = getRngTable(mailTableXl, 'Setting')    #'\Table_설정.xlsx'
        Dir_Table_Price = getRngTable(mailTableXl, 'Price')    #20240716 규격별 택배비 테이블
        Dir_Table_Formula = getRngTable(mailTableXl, 'Formula')

        Raw_h = pd.read_excel(Path_+Dir_Raw_h)
        Raw_d = pd.read_excel(Path_+Dir_Raw_d)
        Raw_s = pd.read_csv(Path_+Dir_Raw_s, encoding='CP949')
        Raw_o = pd.read_excel(Path_+Dir_Raw_o)  
        Raw_t = pd.read_excel(Path_+Dir_Raw_t)
        Table_premium = Dir_Table_premium.input_to_df()    #pd.read_excel(Path_+Dir_Table_premium)
        Table_name = Dir_Table_name.input_to_df()          #pd.read_excel(Path_+Dir_Table_name)
        Table_account = Dir_Table_account.input_to_df()    #pd.read_csv(Path_+Dir_Table_account)
        Table_set = Dir_Table_setting.input_to_df()        #pd.read_excel(Path_+Dir_Table_setting)
        Table_price = Dir_Table_Price.input_to_df()
        Table_Formula = Dir_Table_Formula.input_to_df()

        createDirectory(Path_+'\\'+datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
                
        Save_path_ = Path_+'\\'+datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        Date_, Report_Date, Flat_Rate, Ex_Rate, Ex_Count, Fee = Get_Setting_Data(Table_set)
        Raw_o, Raw_d, Table_premium, Table_premium_on = Get_Table_Mailroom(Raw_h,Raw_d,Raw_s,Raw_o,Raw_t,Table_premium,Table_name,Table_account, Table_price, Table_Formula)
        Mail_Room_def(Date_, Report_Date, Flat_Rate, Ex_Rate, Ex_Count, Fee, Raw_o, Raw_d, Table_premium, Table_premium_on, Table_Formula)
        
        
        