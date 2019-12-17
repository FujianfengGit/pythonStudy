#python的一些基础预发


#变量
total = 20
num = 4
print(total/num)
print(20/4)


#序列
shenxiao ='鼠牛虎兔龙蛇马羊猴鸡狗猪'
print(shenxiao[0:3])
print(shenxiao[-1])


#计算星座
zodiac_name = ['摩羯座','水瓶座','双鱼座','白羊座','金牛座','双子座',
'巨蟹座','狮子座','处女座','天秤座','天蝎座','射手座']
zodiac_date = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),
  (7,23),(8,23),(9,23),(10,23),(11,23),(12,23))


year,month,day = eval(input("请输入出生年月日，用逗号分隔："))
#(month,day) = (9,23)
pos = len(list(filter(lambda x:x<(month,day),zodiac_date)))%12
print(zodiac_name[pos])