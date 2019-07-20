import xlrd
import xlwt
import os
import time
from moviepy.editor import VideoFileClip

# def format_byte(number):
#     '''
#     :param number:
#     :return:
#     '''
#     for (scale, label) in [(1024 ** 3, 'GB'), (1024 ** 2, 'MB'), (1024 ** 3, 'KB')]:
#         if number > scale:
#             return '%.2f%s' % (number / scale, label)
#         elif number == 1:
#             return '1字节'
#         else:


class MovesInfo(object):
    def __init__(self, path):
        if path and len(path) > 0:
            self.path = path
            split = path.split('/')
            self.name = split[-1]
            file_info = os.stat(path)
            self.size = file_info.st_size
            self.changeTime = file_info.st_ctime


def read():
    data = xlrd.open_workbook('电影整理.xlsx')
    table = data.get_sheet(0)


def write(moves=[MovesInfo('')]):
    for move in moves:
        print(move)
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('所有电影')
    worksheet.write(0, 0, label='Row 0, Column 0 Value')
    workbook.save('test.xls')


write()
