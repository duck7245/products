import os


# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r') as f: 
        for line in f:
            # s = line.strip().split(',')
            #          # 刪除\n  以,做切割
            # print(s)
            # name = s[0]
            # price = s[1]
            if '商品, 價格' in line:
                continue # 繼續 跳到下一迴 / break 跳出迴圈 (continue, break 都只能寫在迴圈裡)
            name, price = line.strip().split(',')
            # print(name, price)
            products.append([name,price])
    print(products)
    return products


# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        # p = []
        # p.append(name)
        # p.append(price)
        # products.append(p) # 二維清單
        # p = [name, price]   # products = [p] 這種寫法只會裝最後一個進去,不會累計裝入
        products.append([name, price])
    print(products)
    return products
    # print(products[0][0], products[0][1])
    # for product in products:
    #     print(product)
    #     for p in product:
    #         print(p)


# 印出所有商品購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])
    # 'abc' + '123' = 'abc123' # 字串有加乘 沒有減除 
    # 'abc' * 3 = 'abcabcabc'
    # 沒有對product 增減內容, 所以略過return


# 寫入檔案
def write_file(filename, products):
    with open(filename, 'w') as f: 
    # with open('products.csv', 'w', encoding='utf-8') as f:
                                     # 設定通用編碼解決亂碼問題    
        # f.write('商品' + ',' + '價格' + '\n')
        f.write('商品, 價格\n') # f.write('商品, 價格, \n') 這種寫法之後讀取csv時會多出一格空白字串''
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')
            # f.write(p[0], str(p[1]), '\n') # 寫入時字串之間需要用+來串聯
            # print(p[0], str(p[1]), '\n') #印出時不需用+串聯
        # 只是寫入檔案, 不用return

    # with open('products.csv', 'w') as f:
    #     for p in products:
    #         f.write(p[0] + '\n'+ p[1] + '\n')

    # with open('products.csv', 'w') as f:
    #     for product in products:
    #         for p in product:
    #             f.write(p + '\n')

    # with open('products.txt', 'w') as f:
    #     for p in products:
    #         f.write(p[0] + ',' + p[1] + '\n')

    # # with open('products.docx', 'w') as f:
    #     for p in products:
    #         f.write(p[0] + ',' + p[1] + '\n')

    # with open('products.xlsx', 'w') as f:
    #     for p in products:
    #         f.write(p[0] + ',' + p[1] + '\n')


def main(filename):
    if os.path.isfile(filename): # 檢查檔案在不在
        print('yeah!')
        products = read_file(filename)
        products = user_input(products)
        print_products(products)
        write_file(filename, products)
    else:
        print('file cannot find')


main('products.csv')
# main('products1.csv')
# main('products2.csv')


# refactor 重構