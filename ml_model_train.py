# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020/5/15 3:44 下午

import numpy as np
from sklearn.linear_model import LogisticRegression as LR
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.externals import joblib
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB

from load_data import train_df, test_df
from albert_zh.extract_feature import BertVector

# 读取文件并进行转换
bert_model = BertVector(pooling_strategy="REDUCE_MEAN", max_seq_len=200)
print('begin encoding')
f = lambda text: bert_model.encode([text])["encodes"][0]
train_df['x'] = train_df['text'].apply(f)
test_df['x'] = test_df['text'].apply(f)
print('end encoding')

x_train = np.array([vec for vec in train_df['x']])
x_test = np.array([vec for vec in test_df['x']])
y_train = np.array([vec for vec in train_df['label']])
y_test = np.array([vec for vec in test_df['label']])
print('x_train: ', x_train.shape)

# Logistic Regression
lr = LR(random_state=123)
lr.fit(x_train, y_train)

y_pred = lr.predict(x_test)
print("Logistic Regression Model")
print("混淆矩阵", confusion_matrix(y_true=y_test, y_pred=y_pred))
print("正确率：", accuracy_score(y_test, y_pred))
print(classification_report(y_true=y_test, y_pred=y_pred, digits=4))

# 保存模型
joblib.dump(lr, "lr.model")

# Naive Bayes Model
gnb = GaussianNB()
gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)
print("\nNaive Bayes Model")
print("混淆矩阵", confusion_matrix(y_true=y_test, y_pred=y_pred))
print("正确率：", accuracy_score(y_test, y_pred))
print(classification_report(y_true=y_test, y_pred=y_pred, digits=4))

# SVM model
svc = SVC(kernel="rbf")
svc.fit(x_train, y_train)
y_pred = svc.predict(x_test)
print("\nSVM Model")
print("混淆矩阵", confusion_matrix(y_true=y_test, y_pred=y_pred))
print("正确率：", accuracy_score(y_test, y_pred))
print(classification_report(y_true=y_test, y_pred=y_pred, digits=4))

joblib.dump(svc, "svc.model")