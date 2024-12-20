# FC Online 유저 게임 매칭 데이터 분석

## 게임 유저에 대한 데이터 분석
#### 넥슨 게임 중 FC Online 게임 유저 데이터를 사용한 데이터 분석 및 시각화

1) NEXON Open API에서 'FC Online'의 유저ID에 대한 공식경기 게임 매칭 정보 수집
2) 게임 로그 데이터 전처리 후, 분석 및 EDA를 통해 유저 게임 플레이 성향 파악
- 골 성공률 : 패널티 킥 > 박스 안 > 프리킥 > 박스 밖 > 헤딩
3) 분산 분석을 위한 정규성 및 등분산 검정 진행
- 정규성 / 등분산성 모두 만족 : Anova
- 정규성 만족 / 등분산성 만족 X : Welch's Anova
- 정규성 만족 X : Kruskal-Wallis 비모수 검정
4) 분산 분석 결과에 대한 사후 검정 진행
- Turkey's hsd / Post-hoc 기법으로 사후 검정
5) 데이터 분석 과정에서 얻은 인사이트로 게임 내 기능 기획
