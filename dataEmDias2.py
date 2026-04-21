from datetime import datetime

data1 = input("insira a primeira data (dd/mm/aaaa): ")
data2 = input("insita a segunda data (dd/mm/aaaa): ")
formato = "%d/%m/%Y"
data1 = datetime.strptime(data1, formato)
data2 = datetime.strptime(data2, formato)
data3 = (data2 - data1)
print(f"A diferença das datas: ", data3.days, "dias")
