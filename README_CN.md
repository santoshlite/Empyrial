
# By Investors, For Investors.
<br><br><br><br>
<div align="center">
<img src="https://user-images.githubusercontent.com/61618641/120909011-98f8a180-c670-11eb-8844-2d423ba3fa9c.png"/>
<br><br><br><br><br><br><br><br>
  
![](https://img.shields.io/badge/Downloads-11k/month-brightgreen)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/version-1.5.2-blueviolet)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/activity-8.8/10-ff69b4)
![](https://img.shields.io/badge/Open%20source-💜-white)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NqTkkP2u1p1g8W8erU-Y-rSSVbPUDvq2?usp=sharing)
  
 </div>
 
<br><br>

Want to read this in [**English**?](README.md)

Empyrial是一个基于Python的**开源量化投资**库，致力于为**金融机构**和**零售投资者**，于2021年正式发布。Empyrial已经被数以千计的金融业从业人员使用，它的目标是成为一个集**投资组合管理、**分析和**优化于一体的平台。

Empyrial通过带来不同的金融方法，如**风险分析**、**定量分析**、**基本面分析**、**因素分析**和**预测**，增强了投资组合管理**的能力。

有了Empyrial，你可以用这些不同的方法轻松地分析证券或投资组合，并**从中获得最佳的洞察力**。

<br>

<br>

<div align="center">
  
|目录 📖 | 
| --                     
| 1. [安装](#安装) |  
| 2. [功能](#功能) |  
| 3. [使用实例](#使用方法) | 
| 4. [下载拆页](#下载泪水表) | 
| 5. [观星者随时间推移](#观星者随时间推移) | 
| 6. [贡献和问题](#贡献和问题) | 
| 7. [贡献者和鸣谢](#贡献者) |
| 8. [联系](#联系) | 
| 9. [许可证](#许可证) | 
	
</div>


## 安装

你可以使用pip安装Empyrial。

```
pip install empyrial
```

为了获得更好的体验，**我们建议你在笔记本上使用Empyrial**（Jupyter、Google Colab...）。
	
## 功能

<div align="center">
  
| 特征 📰 | 状态 |
| -- | ------ |
| Empyrial (回测+性能分析) | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.2.4)于2021年5月30日 | |
| Oracle | :alien: [Beta](https://github.com/ssantoshp/Empyrial/releases/tag/1.2.7) 2021年6月1日 | 
| Fundlens | :alien: [Beta](https://github.com/ssantoshp/Empyrial/releases/tag/1.3.1) 2021年6月6日 |
| 优化器 | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.3.6) 2021年6月7日 |
| 重新平衡 | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.5.0) 于2021年6月27日 | | 风险因素镜头
| 风险因素透镜 | :smile_cat: 正在开发中...  | 
| 情绪透镜 | :smile_cat: 正在开发中... | 

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
                  start_date= "2018-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #equal weighting by default
                  benchmark = ["SPY"] #SPY by default
)

empyrial(portfolio)
```

[>>查看输出](https://github.com/ssantoshp/Empyrial/wiki/Empyrial)

如果你想在你的策略中加入**再平衡**（基于日历），你可以这样做。

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2018-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  benchmark = ["SPY"] #SPY by default
		  optimizer = "EF",
		  rebalance = "1y"
)

empyrial(portfolio)
```

可用于重新平衡的时间段是```2y```,```1y```,```6mo```,```季度```,```月```。

<br/>

**资金来源**

```py
from empyrial import fundlens, Engine

portfolio = Engine(    
                  start_date= "2020-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #optional
                  benchmark = ["SPY"] #optional
)

fundlens(portfolio)
```

[>> See the output](https://camo.githubusercontent.com/7cfaebabf9280c7f13ebd9af98585841aaf14e9e34e118a6b434ed45e23acb47/68747470733a2f2f692e6962622e636f2f51486259316e332f323032312d30362d30362d30316831382d34382e706e67)

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

[>> See the output](https://camo.githubusercontent.com/bd2efb1afccb5454aec60f21cbd3bdd1e1ea55b2e5905e8eeb2db3c8a7f363c9/68747470733a2f2f692e6962622e636f2f5750386e6b316d2f323032312d30362d30322d32326831372d30382e706e67)

<br />

**优化器**

有3个优化器可用。

- ```"EF"```: **全球有效边界**

- ```"MV"```: **平均波动率** （在这种情况下，你必须定义一个你不想超过的最大波动率）。

- ```"HRP"```: **分层风险平价**。

注意：默认的优化器是**平等权重**_。

有两种方法可以使用Empyrial的优化器。

1) 直接用引擎优化分配

```py
from empyrial import*

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = ["BLK", "BAC", "AAPL", "TM", "JPM","JD", "INTU", "NVDA", "DIS", "TSLA"],
      optimizer = "EF" 
)

portfolio.weights
```

输出。

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

#for efficient frontier
optimizer(portfolio, "EF")

#for hierarchical risk parity
optimizer(portfolio, "HRP")

#for mean variance
optimizer(portfolio, "MV", vol_max=0.15)
```
[>> See the output](https://user-images.githubusercontent.com/61618641/121251316-04c44f80-c8a7-11eb-9451-e96b9fd7eff5.png) 

## 下载泪水表

想以PDF或HTML文件的形式下载分析报告的泪页吗？你可以查看[文档](https://github.com/ssantoshp/Empyrial/wiki/Downloading-the-generated-tearsheet)，看看如何做到这一点 :)

## 观星者随时间推移

<div align="center">
	
![追星族的时间](https://starchart.cc/ssantoshp/empyrial.svg)
	
</div>

## 贡献和问题

- [Create Issue](https://github.com/ssantoshp/Empyrial/issues/new/choose) - 对于较大的改动（如新功能、大型重构等），最好先开一个问题来讨论，而较小的改进（如文档改进、bug修复等）可以直接发送到PR。

- Fork [Empyrial](https://github.com/ssantoshp/Empyrial) - 点击右上角的**Fork**按钮

- 克隆你自己的分叉: ```git clone https://github.com/ssantoshp/Empyrial.git```。

	*如果你的分叉已经过期，你需要手动同步。[同步方法](https://help.github.com/articles/syncing-a-fork/)

- Empyrial使用Github来托管其源代码，如果您想贡献代码，请使用github的PR（拉动请求）程序。[pull requests](https://github.com/ssantoshp/Empyrial/pulls)。它将等待审查、检查/修改和合并!

## 贡献者

感谢这些优秀的人（[表情符号键](https://allcontributors.org/docs/en/emoji-key)）。

[![All Contributors](https://img.shields.io/badge/all_contributors-8-orange.svg?style=flat-square)](#contributors-)

<table>
  <tr>
    <td align="center"><a href="https://github.com/rslopes"><img src="https://avatars.githubusercontent.com/u/24928343?v=4" width="100px;" alt=""<br /><sub><b>Renan Lopes</b></sub></a><br /><a title="代码">💻</a> <a title="错误报告">🐛 </a></td>
    <td align="center"><a href="https://github.com/diegodalvarez"><img src="https://avatars.githubusercontent.com/u/48641554?v=4" width="100px;" alt=""<br /><sub><b>Diego Alvarez</b></sub></a><br /><a title="代码">💻</a></td>
    <td align="center"><a href="https://github.com/rakeshbhat9"><img src="https://avatars.githubusercontent.com/u/11472305?v=4" width="100px;" alt=""<br /><sub><b>Rakesh Bhat</b></sub></a><br /><a title="代码">💻</a></td>
    <td align="center"><a href="https://github.com/Haizzz"><img src="https://avatars.githubusercontent.com/u/5275680?v=4" width="100px;" alt=""<br /><sub><b>Anh Le</b></sub></a><br /><a title="bug report">🐛</a></td>
    <td align="center"><a href="https://github.com/TonyZhangkz"><img src="https://avatars.githubusercontent.com/u/65281213?v=4" width="100px;" alt=""<br /><sub><b>Tony Zhang</b></sub></a><br /><a title="代码">💻</a></td>
    <td align="center"><a href="https://github.com/eltociear"><img src="https://avatars.githubusercontent.com/u/22633385?v=4" width="100px;" alt=""<br /><sub><b>Ikko Ashimine</b></sub></a><br /><a title="代码">✒️</a></td>
    <td align="center"><a href="https://www.youtube.com/watch?v=-4qx3tbtTgs"><img src="https://avatars.githubusercontent.com/u/50767660?v=4" width="100px;" alt=""<br /><sub><b>QuantNomad</b></sub></a><br /><a title="代码">📹</a></td>
    <td align="center"><a href="https://github.com/agn35"><img src="https://lh3.googleusercontent.com/a-/AOh14GhXGFHHpVQTL2r23oEXFssH0f7RyoGDihrS_HmT=s48" width="100px;" alt=""><br /><sub><b>Adam Nelsson</b></sub></a><br /><a title="代码"></a></td>
  </tr>
</table>

本项目遵循[all-contributors](https://github.com/all-contributors/all-contributors)规范。**欢迎任何形式的贡献！**。

## 联系

欢迎通过电子邮件（santoshpassoubady@gmail.com）或在Empyrial的[讨论空间](https://github.com/ssantoshp/Empyrial/discussions)联系我们。

## 许可证

MIT
