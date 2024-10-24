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
- A/B 테스트로 Welch's test 사용 : 이유 - 두 그룹의 크기가 다름
- A/B 테스트 결과 유의한 변수 : 점유율, 헤딩 슛 수, 패널티 박스 골수, 헤딩 골 수, 총 골수, 바운싱 롭 패스 성공 수, 게임 종료 후 골수, 바운싱 롭 패스 시도 수

#### 모델링
- 앞서 분석에서 살아남은 변수로 승부 예측 모델 구현
- 상위 랭커 : Random Forest Classifier 선정(Random forest, XGBoost, LightGBM 중) : 이유 - 전반적인 안정적인 Accuarcy
- 하위 랭커 : LightGBM Classifier 선정(Random forest, XGBoost, LightGBM 중) : 이유 - 준수한 Accuarcy, 각 클래스 공정한 평가 가능한 macro avg 준수, 무승부 클래스 예측 가능
- Joblib 통한 data, model, 라벨 인코더 저장

#### main.py
- FastAPI를 사용하여 FC 온라인 게임 승부 예측 API 구현
- 사용자가 경기 데이터를 POST 요청으로 전송
- 상위 또는 하위 랭커 모델을 통해 승, 무, 패 예측
- 예측 결과를 라벨 인코더로 디코딩하여 반환
- CORS 설정으로 다양한 출처의 요청 허용하고, Uvicorn 서버로 실행

#### WEB 배포
##### test.html
- 사용자가 FC 온라인 승부 예측 위한 데이터를 입력할 수 있는 웹 폼 제공
- FastAPI를 활용해 입력된 데이터를 서버로 전송하고, 서버로부터 예측 결과를 받아 화면에 표시
- HTML, CSS, JavaScript로 구성된 인터페이스

#### API 요청
##### api_request.py
- 사용자로부터 FC 온라인 경기 데이터를 입력받아 FastAPI 서버에 POST 요청을 전송
- 서버의 응답을 받아 예측 결과 출력
- 잘못된 입력이나 요청 실패 시 오류 메시지 출력

#### 외부 앱 배포
- Ngrok를 활용해 배포

### Ollama 모델 등록
![ollama 모델 등록](https://github.com/user-attachments/assets/9a36450e-05e9-4243-8527-5efbdfc298eb)

### 서버 실행 코드
![서버 코드](https://github.com/user-attachments/assets/72d77932-712b-4b11-8ce9-e6b7d1fc33fa)


### RAG 기반 반려동물 챗봇 구현
![챗 체인](https://github.com/user-attachments/assets/17d52ef1-d9c1-4726-89df-e6c574def4a1)

### 모델 선정
- 모델 크기와 사용자 Local 환경 고려해 llama3-ko와 EEVE 모델 중 한국어 답변 우수했던 야놀자 EEVE LLM 모델 선정
- 한국어 임베딩 모델 성능 테스트 자료 참고해 BGE-M3 임베딩 모델 선정

### 챗봇 URL(채팅챗)
[**펫 케어 봇**](https://brave-martin-endlessly.ngrok-free.app/chat/playground/)

# 참고 자료
1. [**EEVE LLM 논문 리뷰**](https://fornewchallenge.tistory.com/entry/AI-%EB%85%BC%EB%AC%B8-%EC%98%AC%ED%95%B4%EC%9D%98-%ED%95%9C%EA%B5%AD%EC%96%B4-LLM%EC%97%90-%EC%84%A0%EC%A0%95%EB%90%9C-%EC%95%BC%EB%86%80%EC%9E%90-%EC%96%B8%EC%96%B4-%EB%AA%A8%EB%8D%B8-EEVE)
2. [**BGE-M3 임베딩 모델 논문 리뷰**](https://introduce-ai.tistory.com/entry/%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-BGE-M3-Embedding-Multi-Lingual-Multi-Functionality-Multi-Granularity-Text-Embeddings-Through-Self-Knowledge-Distillation)
2. [**한국어 임베딩 모델 성능 비교 테스트 결과**](https://steemit.com/kr-dev/@anpigon/20240604t162445271z)


### 사용 모델
> 1. [**야놀자 EEVE모델**](https://huggingface.co/heegyu/EEVE-Korean-Instruct-10.8B-v1.0-GGUF)
> 2. [**BAAI/bge-m3 임베딩 모델**](https://huggingface.co/BAAI/bge-m3)

### 버전
1. `LangChain version: 0.2.12`
2. `Python version: 3.12.4`
3. `LangServe version: 0.2.2`
