#### 📢 公告

好消息！你现在可以通过 EigenLedger 使用维护的 [empyrical](https://github.com/quantopian/empyrical) 库版本了！🎉
<br>
👉 在[这里](https://eigenledger.gitbook.io/eigenledger/using-empyrical/using-empyrical)了解如何使用它，并阅读[此公告帖子](https://github.com/santoshlite/EigenLedger/discussions/128)了解更多信息。
<br>

# 投资者为投资者打造
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/470f1d59-09c6-4b95-af7e-f142764d8195"/>
<br><br><br><br>

![](https://img.shields.io/badge/Downloads-245k-brightgreen)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/version-2.1.6-blueviolet)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/Open%20source-💜-white)	
[![在 Colab 中打开](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TyNgudyFcsgob7o49PwfDJHLaHvluxaU?usp=sharing)
  
</div>

<br>

想要阅读**英文版 🇺🇸**？请点击[**这里**](README.md)

EigenLedger（原名 "Empyrial"）是一个基于 Python 的**开源量化投资**库，专为**金融机构**和**散户投资者**打造，正式发布于 2021 年。EigenLedger 已被**数千名金融行业人士**使用，旨在成为集**投资组合管理**、**分析**和**优化**于一体的平台。

EigenLedger 通过在一个**易于理解**、**灵活**和**强大**的框架中提供最佳的**绩效和风险分析**，**赋能投资组合管理**。

使用 EigenLedger，您可以轻松分析证券或投资组合，以**获得最佳洞察**。它主要是**Quantstats** 和 **PyPortfolioOpt** 等金融分析库的**封装器**。

<br>

<br>



<div align="center">
  
| 目录 📖 | 
| --                     
| 1. [安装](#安装) | 
| 2. [文档](#文档) | 
| 3. [快速开始](#快速开始) |
| 4. [贡献和问题](#贡献和问题) | 
| 5. [贡献者](#贡献者) |
| 6. [联系方式](#联系方式) |
| 7. [许可证](#许可证) |
  
</div>




## 安装

您可以使用 pip 安装 EigenLedger：

```
pip install EigenLedger
```

为了获得更好的体验，**我们建议您在笔记本环境中使用 EigenLedger**（例如，Jupyter，Google Colab）

_注意：macOS 用户需要安装 [Xcode 命令行工具](https://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)。_

_注意：Windows 用户需要安装 C++。([下载](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16)，[安装说明](https://drive.google.com/file/d/0B4GsMXCRaSSIOWpYQkstajlYZ0tPVkNQSElmTWh1dXFaYkJr/view))_



## 文档

这是我们的完整[文档](https://eigenledger.gitbook.io/documentation)！查看我们的完整文档，获取详细指南、所有功能，以及充分利用此库的技巧。



## 快速开始

```py
from EigenLedger import portfolio_analysis, Engine

portfolio = Engine(
    start_date = "2018-08-01", 
    portfolio = ["BABA", "PDD", "KO", "AMD","^IXIC"], 
    weights = [0.2, 0.2, 0.2, 0.2, 0.2],  # 默认设置为等权重
    benchmark = ["SPY"]  # 默认设置为 SPY
)

portfolio_analysis(portfolio)
```



<div align="center">

![image](https://user-images.githubusercontent.com/61618641/126879140-ea03ff17-a7c6-481a-bb3e-61c055b31267.png)
![image](https://user-images.githubusercontent.com/61618641/126879203-4390813c-a4f2-41b9-916b-e03dd8bafffb.png)
![image](https://user-images.githubusercontent.com/61618641/128025087-04afed7e-96ab-4730-9bd8-98f5491b2b5d.png)
![image](https://user-images.githubusercontent.com/61618641/126879204-01fe1eca-00b8-438e-b489-0213535dd31b.png)
![image](https://user-images.githubusercontent.com/61618641/126879210-9fd61e2b-01ab-4bfd-b679-3b1867d9302d.png)
![image](https://user-images.githubusercontent.com/61618641/126879215-e24c929a-55be-4912-8e2c-043e31ff2a95.png)
![image](https://user-images.githubusercontent.com/61618641/126879221-455b8ffa-c958-4ac9-ae98-d15b4c5f0826.png)
![image](https://user-images.githubusercontent.com/61618641/126879222-08906643-16db-441e-a099-7ac3b00bdbd7.png)
![image](https://user-images.githubusercontent.com/61618641/126879223-f1116dc3-cceb-493c-93b3-2d3810cae789.png)
![image](https://user-images.githubusercontent.com/61618641/126879225-dc879b71-2070-46ed-a8ad-e90880050be8.png)
![image](https://user-images.githubusercontent.com/61618641/126879297-cb78743a-6d43-465b-8021-d4b62a659828.png)

</div>


## 星标数随时间变化

<div align="center">
	
![星标数随时间变化](https://starchart.cc/ssantoshp/empyrial.svg)
	
</div>

## 贡献和问题
EigenLedger 使用 GitHub 来托管其源代码。*了解更多关于 [GitHub 流程](https://docs.github.com/en/get-started/quickstart/github-flow)的信息。*  

对于较大的更改（例如，新功能请求、大型重构），请先打开一个 issue 进行讨论。  

* 如果您想创建一个新的 Issue，请[点击这里创建新 Issue](https://github.com/ssantoshp/EigenLedger/issues/new/choose)。  

较小的改进（例如，文档改进、错误修复）可以通过 GitHub 的 Pull Request 流程处理：[拉取请求](https://github.com/ssantoshp/EigenLedger/pulls)。  

* 要贡献代码，您需要执行以下操作：  

 * [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) [EigenLedger](https://github.com/ssantoshp/EigenLedger) - 点击本页面右上角的 **Fork** 按钮。 
 * [克隆您自己的 fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository)。例如，```git clone https://github.com/ssantoshp/EigenLedger.git```  
  *如果您的 fork 过期了，您需要手动同步您的 fork：[同步方法](https://help.github.com/articles/syncing-a-fork/)*  
 * 使用您的 **fork** 作为 `compare head repository`，[创建一个 Pull Request](https://github.com/ssantoshp/EigenLedger/pulls)。  

您的贡献将被审核，可能会被修改，并希望合并到 EigenLedger 中。  

## 贡献者

感谢这些了不起的人（[emoji 说明](https://allcontributors.org/docs/en/emoji-key)）：

[![All Contributors](https://img.shields.io/badge/all_contributors-11-orange.svg?style=flat-square)](#contributors-)

<table>
  <tr>
    <td align="center"><a href="https://github.com/BrendanGlancy"><img src="https://avatars.githubusercontent.com/u/61941978?v=4" width="100px;" alt=""/><br /><sub><b>Brendan Glancy</b></sub></a><br /><a title="Code">💻</a> <a title="Bug report">🐛</a></td>
    <td align="center"><a href="https://github.com/rslopes"><img src="https://avatars.githubusercontent.com/u/24928343?v=4" width="100px;" alt=""/><br /><sub><b>Renan Lopes</b></sub></a><br /><a title="Code">💻</a> <a title="Bug report">🐛</a></td>
    <td align="center"><a href="https://github.com/markthebault"><img src="https://avatars.githubusercontent.com/u/3846664?v=4" width="100px;" alt=""/><br /><sub><b>Mark Thebault</b></sub></a><br /><a title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/diegodalvarez"><img src="https://avatars.githubusercontent.com/u/48641554?v=4" width="100px;" alt=""/><br /><sub><b>Diego Alvarez</b></sub></a><br /><a title="Code">💻🐛</a></td>
    <td align="center"><a href="https://github.com/rakeshbhat9"><img src="https://avatars.githubusercontent.com/u/11472305?v=4" width="100px;" alt=""/><br /><sub><b>Rakesh Bhat</b></sub></a><br /><a title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Haizzz"><img src="https://avatars.githubusercontent.com/u/5275680?v=4" width="100px;" alt=""/><br /><sub><b>Anh Le</b></sub></a><br /><a title="Bug report">🐛</a></td>
    <td align="center"><a href="https://github.com/TonyZhangkz"><img src="https://avatars.githubusercontent.com/u/65281213?v=4" width="100px;" alt=""/><br /><sub><b>Tony Zhang</b></sub></a><br /><a title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/eltociear"><img src="https://avatars.githubusercontent.com/u/22633385?v=4" width="100px;" alt=""/><br /><sub><b>Ikko Ashimine</b></sub></a><br /><a title="Code">✒️</a></td>
    <td align="center"><a href="https://www.youtube.com/watch?v=-4qx3tbtTgs"><img src="https://avatars.githubusercontent.com/u/50767660?v=4" width="100px;" alt=""/><br /><sub><b>QuantNomad</b></sub></a><br /><a title="Code">📹</a></td>
    <td align="center"><a href="https://github.com/buckleyc"><img src="https://avatars.githubusercontent.com/u/4175900?v=4" width="100px;" alt=""/><br /><sub><b>Buckley</b></sub></a><br /><a title="Code">✒️💻</a></td>
    <td align="center"><a href="https://github.com/agn35"><img src="https://lh3.googleusercontent.com/a-/AOh14GhXGFHHpVQTL2r23oEXFssH0f7RyoGDihrS_HmT=s48" width="100px;" alt=""/><br /><sub><b>Adam Nelsson</b></sub></a><br /><a title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/rgleavenworth"><img src="https://avatars.githubusercontent.com/u/87843950?v=4" width="100px;" alt=""/><br /><sub><b>Ranjan Grover</b></sub></a><br /><a title="Code">🐛💻</a></td>
  </tr>
</table>

本项目遵循 [all-contributors](https://github.com/all-contributors/all-contributors) 规范。**欢迎任何形式的贡献！**

## 致谢

由于这些令人难以置信的人的工作，这个库才成为可能：
- [**Ran Aroussi**](https://github.com/ranaroussi) 的 [**Quantstats 库**](https://github.com/ranaroussi/quantstats) 
- [**Robert Martin**](https://github.com/robertmartin8) 的 [**PyPortfolioOpt**](https://github.com/robertmartin8/PyPortfolioOpt) 

## 联系方式

欢迎通过电子邮件 **santoshpassoubady@gmail.com** 或在 EigenLedger 的[讨论空间](https://github.com/ssantoshp/EigenLedger/discussions)与我们联系

## 许可证

Apache 许可证 2.0
