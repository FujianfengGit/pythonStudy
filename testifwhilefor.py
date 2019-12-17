shenxiao ='猴鸡狗猪鼠牛虎兔龙蛇马羊'
# year=int(input("请用户输入年份:"))

#if和else语句
# if  (shenxiao[year%12])=='猴':
#     print("猴年行大运")
# else:
#     print(shenxiao[year%12]+"年好")


#for语句
for cz in shenxiao:
    print(cz)

for i in range(1,8):
    print(i)

for year in range(2006,2019):
    print("%s 年的生肖是 %s"%(year,shenxiao[year%12]))