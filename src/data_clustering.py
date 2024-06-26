import pandas as pd
import numpy as np
from tslearn.clustering import TimeSeriesKMeans, KernelKMeans, KShape
from tslearn.preprocessing import TimeSeriesScalerMeanVariance

def KMeansClustering(data, n_clusters):
    # DataFrame에서 NumPy 배열로 변환
    data_np = data.values

    # 데이터 스케일링
    scaler = TimeSeriesScalerMeanVariance(mu=0., std=1.) # 평균 0, 표준편차 1로 정규화
    data_scaled = scaler.fit_transform(data_np)

    # 클러스터링 모델 생성 및 학습
    model = TimeSeriesKMeans(n_clusters=n_clusters, metric="euclidean", max_iter=50, n_init=5, random_state=0)
    labels = model.fit_predict(data_scaled)

    data['clusters'] = labels

    return data

def KernelKMeansClustering(data, kernel, n_clusters):
    # DataFrame에서 NumPy 배열로 변환
    data_np = data.values

    # 데이터 스케일링
    scaler = TimeSeriesScalerMeanVariance(mu=0., std=1.) # 평균 0, 표준편차 1로 정규화
    data_scaled = scaler.fit_transform(data_np)

    # 클러스터링 모델 생성 및 학습
    model = KernelKMeans(n_clusters=n_clusters, kernel=kernel, max_iter=50, n_init=5, verbose=True, random_state=0)
    labels = model.fit_predict(data_scaled)

    data['clusters'] = labels

    return data

def KShapeClustering(data, n_clusters):
    # DataFrame에서 NumPy 배열로 변환
    data_np = data.values

    # 데이터 스케일링
    scaler = TimeSeriesScalerMeanVariance(mu=0., std=1.) # 평균 0, 표준편차 1로 정규화
    data_scaled = scaler.fit_transform(data_np)

    # 클러스터링 모델 생성 및 학습
    model = KShape(n_clusters=n_clusters, max_iter=50, n_init=5, verbose=True, random_state=0)
    labels = model.fit_predict(data_scaled)

    data['clusters'] = labels

    return data