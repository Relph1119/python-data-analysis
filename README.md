# 数据分析工具的学习记录
&emsp;&emsp;其中包括pandas、numpy、seaborn等。  

## 版本
numpy：1.18.1  
pandas：1.0.1  
seaborn：0.10.0  
matplotlib：3.2.0

## 解题总结
**numpy练习题：**      
1. 第49题：将`np.set_printoptions(threshold=np.nan)`修改成`np.set_printoptions(threshold=np.inf)`
2. 第75、80、98、100题不好理解

**pandas练习题**
1. 第6章-Wind_Stats中的步骤7，将`data.shape[0] - data.isnull().sum()`修改成`data.notnull().sum()`
2. 第6章-Wind_Stats中的步骤11，将`january_winds = data.query('month == 1')`修改成`january_winds = data[data.month == 1]`

**seaborn练习题**
1. seaborn高于0.8版本，需要显式使用seaborn样式：`sns.set()`
2. 第2章，需要安装ipyweights（一个jupyter的插件）

## 参考资料
1. [numpy练习题](https://github.com/rougier/numpy-100)
2. [pandas练习题](https://github.com/guipsamora/pandas_exercises)
3. [seaborn练习题](https://github.com/blueliberty/Seaborn)
4. [Python数据分析，numpy、pandas及其思维导图](https://www.jianshu.com/p/9a9742693b0e)
5. [这十套练习，教你如何用Pandas做数据分析](https://www.kesci.com/api/notebooks/5c69407b336a0d002c184f46/RenderedContent)