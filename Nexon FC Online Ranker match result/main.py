import joblib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

import warnings
warnings.filterwarnings("ignore")

app = FastAPI()
# data set 불러오기
top_ranker = joblib.load('C:/Users/user/Desktop/데이터분석 직무 공부/넥슨 데이터 분석 공부/Nexon FC Online Ranker match result/FC_Online_save/top_ranker_data.pkl')
low_ranker = joblib.load('C:/Users/user/Desktop/데이터분석 직무 공부/넥슨 데이터 분석 공부/Nexon FC Online Ranker match result/FC_Online_save/low_ranker_data.pkl')
# model 불러오기
top_ranker_model = joblib.load('C:/Users/user/Desktop/데이터분석 직무 공부/넥슨 데이터 분석 공부/Nexon FC Online Ranker match result/FC_Online_save/top_ranker_model.pkl')
low_ranker_model = joblib.load('C:/Users/user/Desktop/데이터분석 직무 공부/넥슨 데이터 분석 공부/Nexon FC Online Ranker match result/FC_Online_save/low_ranker_model.pkl')
# 라벨 인코더 불러오기
label_encoder_top_ranker = joblib.load('C:/Users/user/Desktop/데이터분석 직무 공부/넥슨 데이터 분석 공부/Nexon FC Online Ranker match result/FC_Online_save/top_ranker_label_encoder.pkl')
label_encoder_low_ranker = joblib.load('C:/Users/user/Desktop/데이터분석 직무 공부/넥슨 데이터 분석 공부/Nexon FC Online Ranker match result/FC_Online_save/low_ranker_label_encoder.pkl')

# CORS 설정
origins = ["*"]  # 허용할 URL 주소
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {
        'message' : 'FC 온라인 승부 예측'
    }
    
@app.post('/predict')
async def predict(data: Request):
    data = await data.json()
    # data 추출
    bouncingLobPassTry = data['bouncingLobPassTry']
    shootHeading = data['shootHeading']
    bouncingLobPassSuccess = data['bouncingLobPassSuccess']
    goalTotal = data['goalTotal']
    goalHeading = data['goalHeading']
    possession = data['possession']
    goalTotalDisplay = data['goalTotalDisplay']
    goalInPenalty = data['goalInPenalty']
    current_rank = data['current_rank']  # 현재 랭커 순위 추가

    
    df = pd.DataFrame({
        'bouncingLobPassTry': [bouncingLobPassTry],
        'shootHeading': [shootHeading],
        'bouncingLobPassSuccess': [bouncingLobPassSuccess],
        'goalTotal': [goalTotal],
        'goalHeading': [goalHeading],
        'possession': [possession],
        'goalTotalDisplay': [goalTotalDisplay],
        'goalInPenalty': [goalInPenalty]
    })
    
    # 랭커 등급에 따른 모델 구분
    result = predict_match_result(current_rank, df)
    return result


# 랭커 등급에 따른 모델 구분
def predict_match_result(current_rank, df):
    # 현재 랭커 순위를 입력받고, 1~10 범위인지 확인
    if 1 <= current_rank <= 10:
        result = top_ranker_model.predict(df)
        label_encoder = label_encoder_top_ranker
    else:
        result = low_ranker_model.predict(df)
        label_encoder = label_encoder_low_ranker

    # 예측 결과 디코딩
    decoded_result = label_encoder.inverse_transform(result)

    if decoded_result[0] == '승':
        return {'message': '해당 경기는 승리할 것으로 판단됩니다.'}
    elif decoded_result[0] == '무':
        return {'message': '해당 경기는 무승부로 끝날 것으로 판단됩니다.'}
    else:
        return {'message': '해당 경기는 패배할 것으로 판단됩니다.'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)