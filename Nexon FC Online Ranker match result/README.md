# FC Online 랭커 유저 경기 결과 예측 모델
## 유저 경기 기록을 입력하면 경기 결과를 예상해서 알려주는 웹
### FC Online API를 사용해 랭커 총 19명 경기 데이터 수집

### Process
#### 데이터 수집
- NEXON API 센터에서 FC Online 사용자 매치정보를 통해 상위랭커 10명, 하위 랭커 9명 데이터 수집

#### 데이터 전처리 및 분석
- 결측치 제거 후, 각 유저 그룹별 경기 결과 비율 시각화
- 경기 결과와 모든 변수 간 상관분석 진행
- 두 유저 그룹에 대한 상관분석에서 조건 충족하는 변수(p-value 0.05미만 + 상관계수 0.1 이상)
- 가설 : 해당 조건 충족하는 변수들이 그룹 간 차이가 있을까?
- 두 집단 A/B 테스트 시각화
- Mann-Whitney U 검정 진행 : Shapiro-Wilk 정규성 검정 결과, 모든 변수가 정규성 만족하지 않음
- A/B 테스트 검정 결과 유의한 변수 : 점유율, 헤딩 슛 수, 패널티 박스 골수, 헤딩 골 수, 총 골수, 바운싱 롭 패스 성공 수, 게임 종료 후 골수, 바운싱 롭 패스 시도 수

#### 모델링
- 앞서 분석에서 살아남은 변수로 승부 예측 모델 구현
- 상위 랭커 : Random Forest Classifier 선정(Random forest, XGBoost, LightGBM 중) : 이유 - 전반적인 안정적인 Accuarcy
- 하위 랭커 : LightGBM Classifier 선정(Random forest, XGBoost, LightGBM 중) : 이유 - 준수한 Accuarcy, 각 클래스 공정한 평가 가능한 macro avg 준수, 무승부 클래스 예측 가능
- Joblib 통한 data, model, 라벨 인코더 저장

#### main.py
- FastAPI로 FC 온라인 게임 승부 예측 API 구현
- 사용자가 경기 데이터를 POST 요청으로 전송
- 상위/하위 랭커 모델을 통해 승, 무, 패 예측
- 예측 결과를 라벨 인코더로 디코딩하여 반환
- CORS 설정으로 다양한 출처의 요청 허용, Uvicorn 서버로 실행

#### WEB 배포 - test.html
- 사용자가 FC 온라인 승부 예측 위한 데이터를 입력할 수 있는 웹 폼 제공
- 사용자 인터페이스 제공
- FastAPI 서버와 상호작용

#### API 요청 - api_request.py
- 서버와의 API 요청 처리

### 상위 랭커 경기 결과 시각화
![상위 랭커 경기 결과 비율](https://github.com/user-attachments/assets/078fde20-93ef-4f96-a9ad-957c2683b95b)

### 하위 랭커 경기 결과 시각화
![하위 랭커 경기 결과 비율](https://github.com/user-attachments/assets/6c355b42-e85c-4bad-8026-c1799a642485)

### 가상환경 실행
![가상환경 실행](https://github.com/user-attachments/assets/7561e7ee-bacc-46c8-9ecc-80708ae979f2)

### FC온라인 승부 예측 웹 실행 (승리)
https://github.com/user-attachments/assets/360948ae-93c3-4896-a41d-a5655e10025f

### FC온라인 승부 예측 웹 실행 (패배)
https://github.com/user-attachments/assets/10aa4302-005e-4e27-838e-b709a2756d33

### 버전
1. `fastapi version: 0.115.3`
2. `Python version: 3.12.4`
3. `pandas version: 2.2.3`
4. `numpy version: 2.1.2`
5. `joblib version: 1.4.2`
6. `requests version: 2.32.3`
7. `starlette version: 0.41.0`
8. `uvicorn version: 0.32.0`
