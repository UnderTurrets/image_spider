# def percentage(a,b,c):
#     '''''
#     a:已经下载的数据块
#     b:数据块的大小
#     c:远程文件的大小
#    '''
#     per = 100.0 * a * b / c
#     if per > 100 :
#         per = 100
#     return
def percentage(a, b, c):
    if c > 0:
        per = 100.0 * a * b / c
        if per > 100:
            per = 100
        return per
    else:
        return 0
