
# By Investors, For Investors.
<br><br><br><br>
<div align="center">
<img src="https://user-images.githubusercontent.com/61618641/120909011-98f8a180-c670-11eb-8844-2d423ba3fa9c.png"/>
<br><br><br><br><br><br><br><br>
  
![](https://img.shields.io/badge/Downloads-19k/month-brightgreen)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/version-1.9.1-blueviolet)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/activity-9.7/10-ff69b4)
![](https://img.shields.io/badge/Open%20source-💜-white)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NqTkkP2u1p1g8W8erU-Y-rSSVbPUDvq2?usp=sharing)
  
 </div>
 
<br><br>

Want to read this in [**English**?](README.md)

Empyrial是一个基于Python的**开源量化投资**库，致力于为**金融机构**和**零售投资者**，于2021年正式发布。Empyrial已经被数以千计的金融业从业人员使用，它的目标是成为一个集**投资组合管理、**分析和**优化于一体的平台。

Empyrial通过将**业绩和风险分析的精华纳入一个**易于理解的**、**灵活的**和**强大的框架**，使投资组合管理**更加强大**。

通过Empyrial，您可以轻松地分析证券或投资组合，以便**从中获得最佳的洞察力**。

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

_注意：macOS用户需要安装[命令行工具](https://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)._

_注意：如果你是在windows上，你首先需要安装C++。([下载](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16), [安装说明](https://drive.google.com/file/d/0B4GsMXCRaSSIOWpYQkstajlYZ0tPVkNQSElmTWh1dXFaYkJr/view))_
	
## 功能

<div align="center">

| 特征 📰 | 状态 |
| -- | ------ |
| 引擎（回溯测试+性能分析） | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.2.4) 于2021年5月30日 | |
| 优化器 | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.3.6) 于2021年6月7日 | |
| 重新平衡 | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.5.0) 于2021年6月27日 | | 风险管理人
| 风险管理人 | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/v1.7.3)于2021年7月5日 | |沙盒
| 沙盒 | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/v1.9.1) 于2021年7月17日|||||| [发布](https://github.com/ssantoshp/Empyrial/releases/tag/v1.9.1)

</div>

<br />

## 使用方法

**Empyrial**

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2018-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #默认情况下是等权重
                  benchmark = ["SPY"] #SPY是默认设置的
)

empyrial(portfolio)
```

**日历的重新平衡**

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2018-06-09", 
                  portfolio = ["BABA", "PDD", "KO", "AMD", "^IXIC"], 
		  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #默认设置为等额加权
                  benchmark = ["SPY"], #SPY是默认设置的
		  rebalance = "1y"
)

empyrial(portfolio)
```

可用于重新平衡的时间段是```2y```,```1y```,```6mo```,```quarterly```,```monthly```。

<br />

**自定义再平衡**

你可以通过这样做来决定自定义的再平衡日期。

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2018-06-09", 
                  portfolio = ["BABA", "PDD", "KO", "AMD", "^IXIC"], 
		  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #默认情况下是等权重的
                  benchmark = ["SPY"], #默认为SPY
		  rebalance = ["2018-06-09", "2019-01-01", "2020-01-01", "2021-01-01"]
)

empyrial(portfolio)
```
⚠️在这种情况下，确保列表的第一个元素对应于```start_date```，最后一个元素对应于```end_date```，默认是**今天的日期。

<br/>

**优化器**

你可以使用自定义权重。

```py
from empyrial import empyrial, Engine

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = ["BABA", "PDD", "KO", "AMD", "^IXIC"], 
      weights = [0.1, 0.3, 0.15, 0.25, 0.2], #自定义权重
      rebalance = "1y" #每年重新平衡一次
)

empyrial(portfolio)
```

<br/>

你也可以使用我们**的内置优化器**。有5个优化器可用。

- ```"EF"```: **全球有效边际**

- ```"MEANVAR"```: **平均波动率** (在这种情况下，你必须定义一个你不想超过的最大波动率)

- ```"HRP"```: **分层风险平价**。

- ```"MINVAR"```: **最小方差**

- ```"BL"```: **Black Litterman**（在这种情况下，你必须定义你对你投资的资产的看法和信任度)

_注意：默认的优化器是**平等权重**_。


```py
from empyrial import empyrial, Engine

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = "BABA", "PDD", "KO", "AMD", "^IXIC"】。]
      optimizer ="EF"。
      rebalance = "1y" #每年重新平衡一次
)

portfolio.weights
```

输出。

```
[0.31409, 0.0, 0.03472, 0.00046, 0.0, 0.0, 0.069, 0.08831, 0.00854, 0.48489]
```

我们可以看到，分配已经被优化。

<br />

**风险经理**

有3个风险经理可供选择。

- **最大缩水**: ```{"Max Drawdown" : -0.3}```
- **获取利润t**: ```{"Take Profit" : 0.4}```
- **止损**: ```{"Stop Loss" : -0.2}```

```py
from empyrial import empyrial, Engine

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio= ["BABA", "PDD", "KO", "AMD","^IXIC"], 
      optimizer = "EF",
      rebalance = "1y", #每年重新平衡一次
      risk_manager = {"Max Drawdown" : -0.2} #当跌幅超过-20%时停止投资
)

empyrial(portfolio)
``` 

**工业输出**

<div align="center">

![image](https://user-images.githubusercontent.com/61618641/126879140-ea03ff17-a7c6-481a-bb3e-61c055b31267.png)
![image](https://user-images.githubusercontent.com/61618641/126879203-4390813c-a4f2-41b9-916b-e03dd8bafffb.png)
![image](https://user-images.githubusercontent.com/61618641/126879204-01fe1eca-00b8-438e-b489-0213535dd31b.png)
![image](https://user-images.githubusercontent.com/61618641/126879210-9fd61e2b-01ab-4bfd-b679-3b1867d9302d.png)
![image](https://user-images.githubusercontent.com/61618641/126879215-e24c929a-55be-4912-8e2c-043e31ff2a95.png)
![image](https://user-images.githubusercontent.com/61618641/126879221-455b8ffa-c958-4ac9-ae98-d15b4c5f0826.png)
![image](https://user-images.githubusercontent.com/61618641/126879222-08906643-16db-441e-a099-7ac3b00bdbd7.png)
![image](https://user-images.githubusercontent.com/61618641/126879223-f1116dc3-cceb-493c-93b3-2d3810cae789.png)
![image](https://user-images.githubusercontent.com/61618641/126879225-dc879b71-2070-46ed-a8ad-e90880050be8.png)
![image](https://user-images.githubusercontent.com/61618641/126879297-cb78743a-6d43-465b-8021-d4b62a659828.png)

</div>

## 下载泪水表

你也可以下载由Empyrial生成的PDF格式的泪水表。

```py
from empyrial import get_report, Engine

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = ["BLK", "BAC", "AAPL", "TM", "JPM", "JD", "INTU", "NVDA", "DIS", "TSLA"],
      optimizer = "EF",
      rebalance = "1y", #每年重新平衡一次
      risk_manager = {"Stop Loss" : -0.2}
)

get_report(portfolio)
``` 

输出。

![image](https://user-images.githubusercontent.com/61618641/126879406-3ff8eb14-e08b-4103-b46d-02597634d469.png)

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
