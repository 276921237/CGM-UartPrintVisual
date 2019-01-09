# 代码功能：
# 1.以分号为间隔，按列读取文本文件
# 2.将读取到的数据转换成int类型数据
# 3.将int类型数据以折线图形式展示出来 
# 4.由于原始数据可能有大的突变不方便图形暂时，在代码中可以限制最大值，可修改 max_pdd 变量来控制最大值，
# 5.也可以设定 max_visual_value_plus , max_visual_value_minus 来控制Y轴的最大正，负显示值
# 6.数据格式如下，如果python运行报错，请检查数据格式，特别是在中途是否有打印输入：
# [12-13 16:22:07]3d87:pdd:0004,000a,0004,8006;pll:6;da:7df3
# [12-13 16:22:08]3d88:pdd:0004,000b,0004,8007;pll:6;da:7df3
# [12-13 16:22:09]3d89:pdd:0003,000a,0003,8007;pll:6;da:7df3
# [12-13 16:22:10]3d8a:pdd:0005,000b,0005,8006;pll:6;da:7df3
# [12-13 16:22:11]3d8b:pdd:0004,000b,0004,8007;pll:6;da:7df3
# [12-13 16:22:12]3d8c:pdd:0003,000b,0003,8008;pll:6;da:7df3
# [12-13 16:22:13]3d8d:pdd:0005,000b,0005,8006;pll:6;da:7df3
# [12-13 16:22:14]3d8e:pdd:0004,000b,0004,8007;pll:6;da:7df3
# [12-13 16:22:15]3d8f:pdd:0003,000b,0003,8008;pll:6;da:7df3
# [12-13 16:22:16]3d90:pdd:0005,000b,0005,8006;pll:6;da:7df3
# [12-13 16:22:17]3d91:pdd:0004,000b,0004,8007;pll:6;da:7df3
# [12-13 16:22:18]3d92:pdd:0003,000b,0003,8008;pll:6;da:7df3
# [12-13 16:22:19]3d93:pdd:0005,000b,0005,8006;pll:6;da:7df3
# [12-13 16:22:20]3d94:pdd:0004,000b,0004,8007;pll:6;da:7df3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

import tkinter as tk
from tkinter import filedialog

# 设定最大PDD值，在取数据时如果某个值大于 max_pdd 则修改该值为 max_pdd
max_pdd = 10000
# 设定 max_visual_value_plus 来控制Y轴的最大显示值
max_visual_value_plus = 200
# 设定 max_visual_value_minus 来控制Y轴的最小显示值
max_visual_value_minus = -200
# 获取文件 
root = tk.Tk()
root.withdraw()
 
origin_data_file = filedialog.askopenfilename()


# 指定文件名
# file_path = 'CGM1216_2145 4B0.log'
file_path = origin_data_file
# 指定数据列名称
column_names = ['index1' , 'index2' , 'index3']
print('%s: program start' % datetime.datetime.now())
# 读取数据文件，以';'为间隔
print("open file: %s" % file_path)
data = pd.read_csv(file_path , header = None , sep = ';' , names = column_names)
print('%s: read csv complete' % datetime.datetime.now())


#################################################
# 第一组PDD值
# cut the data.indexx string list 
y_pdd1 = []
sign_pdd1 = []
for i in range(0, len(data.index)):
    y_pdd1.append(data.index1[i][-18:-15])
for i in range(0, len(data.index)):
    sign_pdd1.append(data.index1[i][-19])
# translate the origindata into integer
y_pdd1_dec = []    
for i in range(0 , len(data.index)):
    z = 8*int(y_pdd1[i] , base = 16)
    if sign_pdd1[i] == '8' or sign_pdd1[i] == 'f':
        if  z >= max_pdd:
            y_pdd1_dec.append(-max_pdd)
        else:
            y_pdd1_dec.append(-z)   
    else:
        if  z >= max_pdd:
            y_pdd1_dec.append(max_pdd)
        else:
            y_pdd1_dec.append(z)      
            
print('%s: generate pdd_data1 complete' % datetime.datetime.now())            
#################################################
# 第二组PDD值
# cut the data.indexx string list 
y_pdd2 = []
sign_pdd2 = []
for i in range(0, len(data.index)):
    y_pdd2.append(data.index1[i][-13:-10])
for i in range(0, len(data.index)):
    sign_pdd2.append(data.index1[i][-14])
# translate the origindata into integer
y_pdd2_dec = []    
for i in range(0 , len(data.index)):
    z = 8*int(y_pdd2[i] , base = 16)
    if sign_pdd2[i] == '8' or sign_pdd2[i] == 'f':
        if  z >= max_pdd:
            y_pdd2_dec.append(-max_pdd)
        else:
            y_pdd2_dec.append(-z)   
    else:
        if  z >= max_pdd:
            y_pdd2_dec.append(max_pdd)
        else:
            y_pdd2_dec.append(z) 
print('%s: generate pdd_data2 complete' % datetime.datetime.now())  
#################################################
# 第三组PDD值
# cut the data.indexx string list 
y_pdd3 = []
sign_pdd3 = []
for i in range(0, len(data.index)):
    y_pdd3.append(data.index1[i][-8:-5])
for i in range(0, len(data.index)):
    sign_pdd3.append(data.index1[i][-9])
# translate the origindata into integer
y_pdd3_dec = []    
for i in range(0 , len(data.index)):
    z = 8*int(y_pdd3[i] , base = 16)
    if sign_pdd3[i] == '8' or sign_pdd3[i] == 'f':
        if  z >= max_pdd:
            y_pdd3_dec.append(-max_pdd)
        else:
            y_pdd3_dec.append(-z)   
    else:
        if  z >= max_pdd:
            y_pdd3_dec.append(max_pdd)
        else:
            y_pdd3_dec.append(z) 
print('%s: generate pdd_data3 complete' % datetime.datetime.now())              
#################################################
# 第四组PDD值
# cut the data.indexx string list 
y_pdd4 = []
sign_pdd4 = []
for i in range(0, len(data.index)):
    y_pdd4.append(data.index1[i][-3:])
for i in range(0, len(data.index)):
    sign_pdd4.append(data.index1[i][-4])
# translate the origindata into integer
y_pdd4_dec = []    
for i in range(0 , len(data.index)):
    z = 8*int(y_pdd4[i] , base = 16)
    if sign_pdd4[i] == '8' or sign_pdd4[i] == 'f':
        if  z >= max_pdd:
            y_pdd4_dec.append(-max_pdd)
        else:
            y_pdd4_dec.append(-z)   
    else:
        if  z >= max_pdd:
            y_pdd4_dec.append(max_pdd)
        else:
            y_pdd4_dec.append(z) 
print('%s: generate pdd_data4 complete' % datetime.datetime.now())              
#################################################
# PLL值
# cut the data.indexx string list 
y_pll = []
for i in range(0, len(data.index)):
    y_pll.append(data.index2[i][-1])
# translate the origindata into integer
y_pll_dec = []    
for i in range(0 , len(data.index)):
    y_pll_dec.append(int(y_pll[i] , base=16))
##############################################
# DA值
# cut the data.indexx string list 
y_davalue = []
for i in range(0, len(data.index)):
    y_davalue.append(data.index3[i][-4:])
# translate the origindata into integer
y_davalue_dec = []    
for i in range(0 , len(data.index)):
    y_davalue_dec.append(int(y_davalue[i] , base=16))
####################################################
print('%s: generate all data complete' % datetime.datetime.now())
    
x = np.linspace(1, len(data.index), len(data.index))
# 创建全部PDD值曲线
plt.figure()
plt.title("PDD VALUE FIGURE")
plt.plot(x,y_pdd1_dec,label = 'REF_VS_LOC')
plt.plot(x,y_pdd2_dec,label = '4B0_VS_LOC')
plt.plot(x,y_pdd3_dec,label = 'UBLOX_VS_LOC')
plt.plot(x,y_pdd4_dec,label = '4B0_VS_UBLOX')
plt.legend()
# 限制Y轴范围
plt.ylim(max_visual_value_minus , max_visual_value_plus)

# 创建PDD1值曲线
plt.figure()
plt.title("REF_VS_LOC VALUE FIGURE")
plt.plot(x,y_pdd1_dec,label = 'REF_VS_LOC')
plt.legend()
# 限制Y轴范围
plt.ylim(max_visual_value_minus , max_visual_value_plus)

# 创建 PDD2 值曲线
plt.figure()
plt.title("4B0_VS_LOC VALUE FIGURE")
plt.plot(x,y_pdd2_dec,label = '4B0_VS_LOC')
plt.legend()
# 限制Y轴范围
plt.ylim(max_visual_value_minus , max_visual_value_plus)

# 创建 PDD3 值曲线
plt.figure()
plt.title("UBLOX_VS_LOC VALUE FIGURE")
plt.plot(x,y_pdd3_dec,label = 'UBLOX_VS_LOC')
plt.legend()
# 限制Y轴范围
plt.ylim(max_visual_value_minus , max_visual_value_plus)

# 创建 PDD4 值曲线
plt.figure()
plt.title("4B0_VS_UBLOX VALUE FIGURE")
plt.plot(x,y_pdd4_dec,label = '4B0_VS_UBLOX')
plt.legend()
# 限制Y轴范围
plt.ylim(max_visual_value_minus , max_visual_value_plus)

# 创建PLL 、DA 以及 REF_VS_LOC PDD 曲线
plt.figure()

plt.subplot(311)
# plt.title("PLL VALUE FIGURE")
plt.plot(x,y_pll_dec,label = 'pll value')
plt.legend()

plt.subplot(312)
# plt.title("DA VALUE FIGURE")
plt.plot(x,y_davalue_dec , label = 'da value')
plt.legend()

plt.subplot(313)
# plt.title("REF_VS_LOC FIGURE")
plt.plot(x,y_pdd1_dec , label = 'REF_VS_LOC')
plt.legend()
# 限制Y轴范围
plt.ylim(max_visual_value_minus , max_visual_value_plus)

print('%s: generate figure complete' % datetime.datetime.now())
plt.show() 



