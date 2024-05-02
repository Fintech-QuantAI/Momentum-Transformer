# Momentum-Transformer
Finance Momentum_Transformer project/

│

├── data/                        # 데이터 관련 파일

│   ├── raw/                     # 원본 데이터

│   └── processed/               # 전처리 및 클러스터링 처리된 데이터

│

├── models/                      # 모델 파일 및 학습된 모델

│   ├── transformer_encoder.py      # 트랜스포머 인코더 모델 정의

│   └── trained/                 # 학습된 모델 파일

│

├── notebooks/                   # Jupyter 노트북 파일

│   ├── data_preprocessing.ipynb      # 데이터 전처리 노트북

│   ├── data_clustering.ipynb         # 데이터 클러스터링 노트북

│   ├── model_training.ipynb          # 모델 학습 노트북

│   └── evaluation_and_plots.ipynb    # 평가 및 결과 시각화 노트북

│

├── src/                         # 소스 코드

│   ├── __init__.py

│   ├── data_loader.py           # 데이터 로딩 및 전처리 스크립트

│   ├── data_clustering.py       # 데이터 클러스터링 스크립트

│   ├── model.py                 # 모델 아키텍처 스크립트

│   ├── train.py                 # 모델 학습 스크립트

│   └── evaluate.py              # 모델 평가 및 테스트 스크립트

│

├── results/                     # 결과 및 로그 파일

│   ├── metrics.log              # 평가 지표 로그 파일

│   └── plots/                   # 결과 시각화 이미지

│

├── requirements.txt             # 프로젝트 의존성 목록

└── README.md                    # 프로젝트 설명 및 사용법
