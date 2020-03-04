# -*- coding: utf-8 -*-
# author: Jclian91
# place: Pudong Shanghai
# time: 2020-03-04 20:13

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import json
import numpy as np
from albert_zh.extract_feature import BertVector
from keras.models import load_model


# 定义端口为10008
define("port", default=10008, help="run on the given port", type=int)

# 加载ALBERT
bert_model = BertVector(pooling_strategy="REDUCE_MEAN", max_seq_len=100)
# 加载已经训练好的模型
load_model = load_model("visit_classify.h5")


# 对句子进行预测
class PredictHandler(tornado.web.RequestHandler):

    def post(self):

        text = self.get_argument("text")

        # 将句子转换成向量
        vec = bert_model.encode([text])["encodes"][0]
        x_train = np.array([vec])

        # 模型预测
        predicted = load_model.predict(x_train)
        y = np.argmax(predicted[0])
        label = '是' if y else "否"

        # 返回结果
        result = {"原文": text, "是否属于出访类事件？": label}

        self.write(json.dumps(result, ensure_ascii=False, indent=2))


# 主函数
def main():

    # 开启tornado服务
    tornado.options.parse_command_line()
    # 定义app
    app = tornado.web.Application(
            handlers=[(r'/predict', PredictHandler)] #网页路径控制
           )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


main()