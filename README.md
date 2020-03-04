任务介绍：

    文本二分类任务。对文档进行分类，判断是否属于政治上的出访类事件。

### 准备工作

    下载requiments.txt中的第三方模块，本项目的Python版本为3.6.9。

### 数据集介绍：
    训练集：280个样本，测试集：60个样本

### 模型：

    ALBERT作为特征提取，模型采用最简单的神经网络模型：DNN. 直接运行model_train.py即可。

### 模型效果：

1. 在训练集的acc为0.9857,在测试集上的acc为0.9500，如下图所示：

![](https://github.com/percent4/ALBERT_text_classification/blob/master/loss_acc.png)


2. model_predict.py中的预测语句预测全部正确。

### HTTP服务

将模型预测写成HTTP服务，用Postman测试预测时间，如下图：

![](https://github.com/percent4/ALBERT_text_classification/blob/master/predict.png)
