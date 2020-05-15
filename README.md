任务介绍：

    文本二分类任务。对文档进行分类，判断是否属于政治上的出访类事件。

### 准备工作

    下载requiments.txt中的第三方模块，本项目的Python版本为3.6.9。

### 数据集介绍：
    训练集：280个样本，测试集：60个样本

### 模型：

    1. ALBERT作为特征提取，模型采用最简单的神经网络模型：DNN. 直接运行model_train.py即可。
    2. ALBERT作为特征提取，采用LR，NB, SVM等机器学习模型来进行分类，直接运行ml_model_train.py即可。

### 模型效果：

1. DNN模型在训练集的acc为0.9857,在测试集上的acc为0.9500，如下图所示：

![](https://github.com/percent4/ALBERT_text_classification/blob/master/loss_acc.png)

2. 在机器学习上的效果如下：

```
Logistic Regression Model
混淆矩阵 [[33  5]
 [ 2 40]]
正确率： 0.9125
              precision    recall  f1-score   support

           0     0.9429    0.8684    0.9041        38
           1     0.8889    0.9524    0.9195        42

   micro avg     0.9125    0.9125    0.9125        80
   macro avg     0.9159    0.9104    0.9118        80
weighted avg     0.9145    0.9125    0.9122        80

Naive Bayes Model
混淆矩阵 [[37  1]
 [ 1 41]]
正确率： 0.975
              precision    recall  f1-score   support

           0     0.9737    0.9737    0.9737        38
           1     0.9762    0.9762    0.9762        42

   micro avg     0.9750    0.9750    0.9750        80
   macro avg     0.9749    0.9749    0.9749        80
weighted avg     0.9750    0.9750    0.9750        80

SVM Model
混淆矩阵 [[35  3]
 [ 1 41]]
正确率： 0.95
              precision    recall  f1-score   support

           0     0.9722    0.9211    0.9459        38
           1     0.9318    0.9762    0.9535        42

   micro avg     0.9500    0.9500    0.9500        80
   macro avg     0.9520    0.9486    0.9497        80
weighted avg     0.9510    0.9500    0.9499        80
```


2. model_predict.py中的预测语句预测全部正确。

### HTTP服务

将模型预测写成HTTP服务，用Postman测试预测时间，如下图：

![](https://github.com/percent4/ALBERT_text_classification/blob/master/predict.png)
