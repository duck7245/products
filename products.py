products = []
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
# print(products[0][0], products[0][1])

# for product in products:
# 	print(product)
# 	for p in product:
# 		print(p)

for p in products:
	print(p[0], '的價格是', p[1])

# 'abc' + '123' = 'abc123' # 字串有加乘 沒有減除 
# 'abc' * 3 = 'abcabcabc'

# with open('products.csv', 'w') as f: 
with open('products.csv', 'w', encoding='utf-8') as f:
								 # 設定通用編碼解決亂碼問題	
	# f.write('商品' + ',' + '價格' + '\n')
	f.write('商品, 價格, \n') # f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
		# f.write(p[0], str(p[1]), '\n') # 寫入時字串之間需要用+來串聯
print(p[0], str(p[1]), '\n') #印出時不需用+串聯

# with open('products.csv', 'w') as f:
# 	for p in products:
# 		f.write(p[0] + '\n'+ p[1] + '\n')

# with open('products.csv', 'w') as f:
# 	for product in products:
# 		for p in product:
# 			f.write(p + '\n')

# with open('products.txt', 'w') as f:
# 	for p in products:
# 		f.write(p[0] + ',' + p[1] + '\n')

# # with open('products.docx', 'w') as f:
# 	for p in products:
# 		f.write(p[0] + ',' + p[1] + '\n')

# with open('products.xlsx', 'w') as f:
# 	for p in products:
# 		f.write(p[0] + ',' + p[1] + '\n')
