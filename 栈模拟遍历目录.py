import os


def getAllDirRE(path):
    stack = []
    stack.append(path)

    # 处理栈，当栈为空的时候结束循环
    while len(stack) != 0:
        # 重栈里取出数据
        dirPath = stack.pop()
        # 目录下所有问题件
        fileList = os.listdir(dirPath)

        # 处理每一个文件
        for fileName in fileList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                # 如果是目录就压栈
                print("目录：" + fileName)
                stack.append(fileAbsPath)
            else:
                # 打印普通文件
                print("文件：" + fileName)


path = r'C:\Users\Fly\Desktop\dir'

getAllDirRE(path)
