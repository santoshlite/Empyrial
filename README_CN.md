
# By Investors, For Investors.
<br><br><br><br>
<div align="center">
<img src="https://user-images.githubusercontent.com/61618641/120909011-98f8a180-c670-11eb-8844-2d423ba3fa9c.png"/>
<br><br><br><br><br><br><br><br
  
![](https://img.shields.io/badge/Downloads-7.3k-brightgreen)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/version-1.3.6-blueviolet)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/activity-8.8/10-ff69b4)
![](https://img.shields.io/badge/Open%20source-💜-白色)	
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ssantoshp/GetStartedEmpyrial/main?filepath=get_started_with_empyrial.ipynb)
  
 </div>
 
<br><br>

想用**中文阅读此文？请点击[**这里**](README_CN.md)

Empyrial是一个基于Python的**开源量化投资**库，致力于为**金融机构**和**零售投资者**，于2021年正式发布。Empyrial已经被数以千计的金融业从业人员使用，它的目标是成为一个集**投资组合管理、**分析和**优化于一体的平台。

Empyrial通过带来不同的金融方法，如**风险分析**、**定量分析**、**基本面分析**、**因素分析**和**预测**，增强了投资组合管理**的能力。

有了Empyrial，你可以用这些不同的方法轻松地分析证券或投资组合，并**从中获得最佳的洞察力**。

<br>

<br>

<div align="center">
  
|目录 📖 | 
| --                     
| 1. [安装](#安装) | 2. 
| 2. [功能](#功能) | 3. 
| 3. [使用实例](#使用) | 4.
| 4. [下载拆页](#download-the-tearsheet) | 5.
| 5. [贡献和问题](#贡献和问题) | 6. 
| 6. [贡献者和鸣谢](#贡献者和鸣谢) | 7.
| 7. [联系](#contact) | 8.
| 8. [许可证](#license) | 8.
	
</div>


## 安装

要安装Empyrial，你应该这样做。

```
pip install empyrial
```

## 功能

<div align="center">
  
| 特征 📰 | 状态 |
| -- | ------ |
| Empyrial (backtesting + performance analysis) | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.2.4) on May 30, 2021 | |
| Oracle (使用几个ML模型的预测镜头)| :alien: [测试版](https://github.com/ssantoshp/Empyrial/releases/tag/1.2.7) 于2021年6月1日 | 
| 基本镜头 | :alien: [Beta](https://github.com/ssantoshp/Empyrial/releases/tag/1.3.1) 2021年6月6日 |
| 优化器 | :alien: [Beta](https://github.com/ssantoshp/Empyrial/releases/tag/1.3.6) on Jun 7, 2021 |
| 风险因素透镜 | :smile_cat: 正在开发中...  | 
| 情感透镜 | :smile_cat: 正在开发中... | 
  
</div>

<br />

以下是Empyrial的可用功能。

- ```empyrial``` : **量化投资组合分析** | [Demo](https://colab.research.google.com/drive/1cj40dDqctfWNrVz_nK-FDhdWPay7fVBF?usp=sharing) | [文档](https://github.com/ssantoshp/Empyrial/wiki/Empyrial)

- ```oracle``` : **预测生成**对你的投资组合使用几种预测模型（先知，自动-ARIMA，快速傅里叶变换...） | [Demo](https://colab.research.google.com/drive/11rMpQqW9Om82wzh71cr5k3vDQSNMZ4V1?usp=sharing) | [文档](https://github.com/ssantoshp/Empyrial/wiki/Oracle)

- ```fundlens``` : **对您的投资组合中的每一项资产进行**基本面分析 | [Demo](https://colab.research.google.com/drive/1t2RfYwIJDZ3YN1z5MbS41unRGxGf0dif?usp=sharing) | [文档](https://github.com/ssantoshp/Empyrial/wiki/Fundlens)

- ```optimizer```。**优化你的投资组合中的资产配置** | [Demo](https://colab.research.google.com/drive/12CfYznbdabSDYUbtSwamqyILOIwR7Sje?usp=sharing)

## 使用方法

**Empyrial**

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2020-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #默认情况下是等权重
                  benchmark = ["SPY"] 
)

empyrial(portfolio)
```

Output:

<img src="https://user-images.githubusercontent.com/61618641/120065794-8203ef00-c073-11eb-84a8-8dda6908da4c.png"/>

[>> See the full output](https://github.com/ssantoshp/Empyrial/wiki/Empyrial)

<br />

**Oracle**

```py
from empyrial import oracle, Engine

portfolio = Engine(    
                  start_date= "2020-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], 
                  benchmark = ["SPY"] 
)

oracle(portfolio)
```

Output:

<div align="center">
	
![2021-06-08_22h39_56](https://user-images.githubusercontent.com/61618641/121254539-aa2cf280-c8aa-11eb-809e-e20174f5e742.png)

</div>

[了解如何解释这些预测](https://github.com/ssantoshp/Empyrial/wiki/Oracle)

<br />

**Fundlens**

```py
from empyrial import fundlens, Engine

portfolio = Engine(    
                  start_date= "2020-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], # 可选
                  benchmark = ["SPY"] # 可选
)

fundlens(portfolio)
```

Output:

<div align="center"/>

<img src="https://camo.githubusercontent.com/7cfaebabf9280c7f13ebd9af98585841aaf14e9e34e118a6b434ed45e23acb47/68747470733a2f2f692e6962622e636f2f51486259316e332f323032312d30362d30362d30316831382d34382e706e67"/>

</div>

<br />

**Optimizer**

有3个优化器可用。

- ````"EF"````: **全球有效前沿**

- ```"MV"```: **平均波动率** （在这种情况下，你必须定义一个你不想超过的最大波动率）。

- ```"HRP"```: **分层风险平价**。

注意：默认的优化器是**平等权重**。

有两种方法来使用Empyrial的优化器。

1) 直接用引擎优化分配

```py
from empyrial import*

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = ["BLK", "BAC", "AAPL", "TM", "JPM","JD", "INTU", "NVDA", "DIS", "TSLA"],
      optimizer = "EF"
      
      #for Mean Variance
      #optimizer = "MV"
      #max_vol = 0.15   
)

portfolio.weights
```

Output:

```
[0.31409, 0.0, 0.03472, 0.00046, 0.0, 0.0, 0.069, 0.08831, 0.00854, 0.48489]
```

2) 查看一个优化器的性能

```py
from empyrial import*

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = ["BLK", "BAC", "AAPL", "TM", "JPM","JD", "INTU", "NVDA", "DIS", "TSLA"]
)

optimizer(portfolio, "EF")

#for mean variance
optimizer(portfolio, "MV", vol_max=0.15)
```

Output:

<div align="center">
	
![2021-06-08_22h15_09](https://user-images.githubusercontent.com/61618641/121251316-04c44f80-c8a7-11eb-9451-e96b9fd7eff5.png)

</div>

<br />

##下载泪水表

想以PDF或HTML文件的形式下载分析报告的泪页吗？你可以查看[文档](https://github.com/ssantoshp/Empyrial/wiki/Downloading-the-generated-tearsheet)，看看如何做到这一点 :)


## 贡献和问题

- [Create Issue](https://github.com/ssantoshp/Empyrial/issues/new/choose) - 对于较大的改动（如新功能、大型重构等），最好先开一个问题来讨论，而较小的改进（如文档改进、bug修复等）可以直接发送到PR。

- Fork [Empyrial](https://github.com/ssantoshp/Empyrial) - 点击右上角的**Fork**按钮

- 克隆你自己的分叉: ```git clone https://github.com/ssantoshp/Empyrial.git```。

	*如果你的分叉已经过期，你需要手动同步。[同步方法](https://help.github.com/articles/syncing-a-fork/)

- Empyrial使用Github来托管其源代码，如果您想贡献代码，请使用github的PR（拉动请求）程序。[pull requests](https://github.com/ssantoshp/Empyrial/pulls)。它将等待审查、检查/修改和合并!

## 贡献者和鸣谢

感谢以下为这个项目做出贡献的人/组织。

- [@rslopes](https://github.com/rslopes)
- [@TonyZhangkz](https://github.com/TonyZhangkz)
- [@rakeshbhat9](https://github.com/rakeshbhat9)
- [@Haizzz](https://github.com/Haizzz)
- [quantstats](https://github.com/ranaroussi/quantstats)
- [quantopian](https://github.com/quantopian)
- [unit8co](https://github.com/unit8co)

## 联系

欢迎通过电子邮件（santoshpassoubady@gmail.com）或在Empyrial的[讨论空间](https://github.com/ssantoshp/Empyrial/discussions)联系我们。

## 许可证

MIT
