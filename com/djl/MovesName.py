import xlrd
import xlwt
import os
import time
from com.djl.FileCheck import FileCheck


# dir = 'C:\cmder'
# files = os.listdir(dir)
# for f in files:
#     print(os.path.isdir(dir + '/' + f))
#     print(f)


def file_deep(path, func):
    '''
    :param path: 父文件夹路径
    :param func: 回掉函数
    :return:
    '''
    files = os.listdir(path)
    for f in files:
        newPath = path + '/' + f
        if os.path.isdir(newPath):
            file_deep(newPath, func)
        else:
            func(newPath)


move_infos = []

check = FileCheck()

useLessNamePart = ['[阳光电影www.ygdy8.com].', '[阳光电影www.ygdy8.net].', '【6v电影www.dy131.com】.', '【6v电影www.dy131.com】.',
                   '阳光电影www.ygdy8.com.', '[最新电影www.6vhao.tv]', '飘花电影piaohua.com', '[最新电影www.66ys.tv]',
                   '[电影天堂www.dy2018.com]', '[66影视www.66ys.tv]', '【6v电影www.dy131.com】', '【更多电影请去www.66ys.org】',
                   '【6v电影www.dy131.com】', '【6v电影www.dy131.com】', '【最新电影www.66e.cc】', '【最新电影www.66e.cc】',
                   '【更多电影请去www.6vdy.net】', '[www.dy131.com转载]', '[6v电影www.dy131.com]', '[电影天堂www.dy2018.net].']


def file_call_back(path):
    if path and len(path) > 0:
        split = path.split('/')
        name = split[-1]
        for n in useLessNamePart:
            name = name.replace(n, '')
        file_byte = os.path.getsize(path)
        size = check.get_filesize(path)
        fileEnd = name.split('.')[-1]
        if file_byte > 500 * 1024 ** 2 and (fileEnd in ('rmvb', 'mkv', 'mp4', 'flv', 'rmvb')):
            timeL = check.get_file_times(path)
            move_info = [name, timeL, size, file_byte, path]
            move_infos.append(move_info)


def write(moves):
    moves.insert(0, ['名字', '时长', '文件大小', 'size', '文件路径'])
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('所有电影')
    for i, move in enumerate(moves):
        print(move)
        for j, info in enumerate(move):
            worksheet.write(i, j, label=info)
    workbook.save('test6.xls')


paths = ['G:\m2\Video\Move', 'Z:\电影\@电影@']
for p in paths:
    file_deep(p, file_call_back)

write(move_infos)
