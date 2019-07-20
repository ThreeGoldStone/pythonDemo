import random
import pickle
import datetime


class SortCounter:
    def __init__(self):
        self.swap_count = 0
        self.times_count = 0
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def end(self):
        self.end_time = datetime.datetime.now()

    def times(self):
        self.times_count += 1

    def swap(self, lst, i, j):
        lst[i], lst[j] = lst[j], lst[i]
        self.swap_count += 1

    def __str__(self):
        return '''
        times_count = %i
        swap_count  = %i
        time        = %s
        ''' % (self.times_count, self.swap_count, str(self.end_time - self.start_time))


def get_random_list(lenth=10):
    lst = []
    for i in range(lenth):
        lst.append(random.randint(0, 100000))
    return lst


file_name = 'random_list_data.dump'


def save_random_list(lenth=10):
    random_list = get_random_list(lenth)
    file = open(file_name, 'wb')
    pickle.dump(random_list, file)
    file.flush()
    file.close()
    print(random_list)


def load_dumped_list():
    file = open(file_name, 'rb')
    loaded_list = pickle.load(file)
    return loaded_list


counter = SortCounter()


# times_count = 49993775
# swap_count  = 25278409
# time        = 0:00:33.752963

# times_count = 4999919619
# swap_count  = 2494783389
# time        = 0:56:08.670276
def bubble_sorting(lst):
    lenth = len(lst)
    for i in range(lenth):
        flag = False
        for j in range(lenth - i - 1):
            counter.times()
            if lst[j] > lst[j + 1]:
                flag = True
                # lst[j], lst[j + 1] = j_value, i_value
                counter.swap(lst, j, j + 1)
        if not flag:
            break


# times_count = 50005000
# swap_count  = 23896792
# time        = 0:00:29.178341

# times_count = 5000050000
# swap_count  = 1839901937
# time        = 0:44:36.250414
def select_sorting(lst):
    lenth = len(lst)
    for i in range(lenth):
        for j in range(i, lenth):
            counter.times()
            if lst[i] < lst[j]:
                counter.swap(lst, i, j)


# times_count = 2494883376
# swap_count  = 2494783389
# time        = 0:39:21.904388
def insertion(lst):
    '''
    插入排序法
    :param lst:
    :return:
    '''
    lenth = len(lst)
    for i in range(lenth):
        for j in range(i, 0, -1):
            counter.times()
            if lst[j] < lst[j - 1]:
                counter.swap(lst, j, j - 1)
            else:
                break


# randint = random.randint(0, 100000)
# print(randint)
# 保存数组
# save_random_list(100000)
# 加载数组
loaded_list = load_dumped_list()
compare_count = 0
counter.start()

# bubble_sorting(loaded_list)
# select_sorting(loaded_list)
insertion(loaded_list)
counter.end()
print(loaded_list)
print(counter)
