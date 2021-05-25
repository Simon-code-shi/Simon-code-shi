import os
import collections


def getAllDirQU(path):
    queue = collections.deque()
    # 进队
    queue.append(path)

    while len(queue) != 0:
        # 出队
        dirPath = queue.popleft()
        # 找出所有的文件
        filesList = os.listdir(dirPath)
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            if os.path.isdir(fileAbsPath):
                print("目录：" + fileName)
                queue.append(fileAbsPath)
            else:
                print("文件：" + fileName)


path = r'C:\Users\Fly\Desktop\dir'

getAllDirQU(path)
