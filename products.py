products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	# p = []
	# p.append(name)
	# p.append(price)
	# p = [name, price]
	# products.append(p) # 二維清單
	# products = [p] 這種寫法只會裝最後一個進去,不會累計裝入
	products.append([name, price])
print(products)
# print(products[0][0], products[0][1])

# for product in products:
# 	print(product)
# 	for p in product:
# 		print(p)

for p in products:
	print(p[0], '的價格是', p[1])

