import os
import time
from win32com import client as wc

#path1 = r'C:\Users\51653\Desktop\all\北京\word'  # 需要修改的文件的路径
#path2 = r'C:\Users\51653\Desktop\doc2docx\北京'  # 存储的路径
def doc2docx(path1, path2):
    for file in os.listdir(path1):

        if file.endswith('.doc'):
            word = wc.Dispatch("Word.Application")
            out_name = file.replace("doc", r'docx')  # doc文件修改后缀名
            in_file = os.path.abspath(path1 + "\\" + file)
            out_file = os.path.abspath(path2 + "\\" + out_name)
            print(in_file)
            print(out_file)

            doc = word.Documents.Open(in_file)
            doc.SaveAs(out_file, 12, False, "", True, "", False, False, False, False)
            doc.Close()

            print('转换成功')
            word.Quit()
            time.sleep(3)  # 避免文件未关闭就打开下一个文件

        else:
            word = wc.Dispatch("Word.Application")
            out_name = file  # 不是doc文件则不修改后缀名
            in_file = os.path.abspath(path1 + "\\" + file)
            out_file = os.path.abspath(path2 + "\\" + out_name)
            doc = word.Documents.Open(in_file)
            print(in_file)
            print(out_file)

            doc.SaveAs(out_file, 12, False, "", True, "", False, False, False, False)
            doc.Close()

            print('复制成功')
            word.Quit
            time.sleep(3)

if __name__ == "__main__":

    path = r'C:\Users\51653\Desktop\all'
    for file_name in os.listdir(path):
        print(file_name)

        path_from = r'C:\Users\51653\Desktop\all\{}\word'.format(file_name)
        print(path_from)
        path_to = r'C:\Users\51653\Desktop\doc2docx\{}'.format(file_name)
        print(path_to)
        doc2docx(path_from, path_to)