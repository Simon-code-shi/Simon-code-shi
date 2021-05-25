import os


def getAllDir(path, sp=""):

    # 列出当前目录下所有文件
    fileList = os.listdir(path)

    # 处理每一个文件
    sp += "   "
    for fileName in fileList:
        # 使用绝对路径
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            print(sp + "目录：" + fileName)
            getAllDir(fileAbsPath, sp)
        else:
            print(sp + "文件：" + fileName)


path = r'C:\Users\Fly\Desktop\dir'

getAllDir(path)
