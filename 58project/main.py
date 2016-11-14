from multiprocessing import Pool #多进程的程序倒入
from channel_extract import chanel_list
from page_parsing import get_links_from

def get_all_links_from(channel):
    for num in range(1,101): #假设访问页面从1-100
        get_links_from(channel,num)

if __name__=='__main__':
    #多进程爬取
    pool = Pool(processes=1)  #创建进程池,所有的程序都进入进程池，然后分配给进程进行处理,pool = Pool(process=2) 可以指定进程数为2,也可以不指定
    pool.map(get_all_links_from,chanel_list.split())

#map的作用演示
# def double(x):
#     return x+2
# print(list(map (double,[1,2,3,4])))