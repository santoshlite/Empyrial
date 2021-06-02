# By Investors, For Investors.
<br><br><br><br>
<div align="center">
<img src="https://i.ibb.co/RjLg9VV/logo.png"/>
<br><br><br><br><br><br>
  
![](https://img.shields.io/badge/Downloads-6.1k-brightgreen)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/version-0.2.7-blueviolet)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/activity-8.8/10-ff69b4)
![](https://img.shields.io/badge/Open%20source-💜-white)	
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ssantoshp/GetStartedEmpyrial/main?filepath=get_started_with_empyrial.ipynb)
  
 </div>
 
<br><br>

Want to read this in **English**? Click [**here**](READMEd.md)

Empyrial是一个基于Python的**开源量化投资**库，致力于为**金融机构**和**零售投资者**，于2021年正式发布。Empyrial已经被数以千计的金融业从业人员使用，它的目标是成为一个集**投资组合管理、**分析和**优化于一身的平台。

Empyrial通过带来不同的金融方法，如**风险分析**、**定量分析**、**基本面分析**、**因素分析**和**预测**，增强了投资组合管理**的能力。

有了Empyrial，你可以用这些不同的方法轻松地分析证券或投资组合，并

<br>

<br>

<div align="center">
  
| 目录 📖 | 
| --                     
| 1. [安装](#安装) | 
| 2. [特点](#特点) | 
| 3. [使用实例](#用法) |
| 4. [下载泪水表](#下载泪水表) |
| 5. [贡献和问题](#贡献和问题) | 
| 6. [撰稿人和鸣谢](#撰稿人和鸣谢) |
| 7. [联系我们](#联系) |
| 8. [许可证](#许可证) |
	
</div>


## 安装

要安装Empyrial，你应该这样做。

```
pip install empyrial
```

## 特点

<div align="center">
  
| 特征 📰 | 状态 |
| -- | ------ |
| Empyrial (回溯测试+性能分析) | :star: [已发布](https://github.com/ssantoshp/Empyrial/releases/tag/v0.2.4) 2021年5月30日 |  
| Oracle (使用几个ML模型的预测镜头)| :外星人: [Beta](https://github.com/ssantoshp/Empyrial/releases/tag/0.2.7) 于2021年6月1日 | 
| Fundamental lens | :smile_cat: 正在开发中...  |
| Risk lens | :smile_cat: 在发展中...  | 
| Alpha lens | :smile_cat: 正在开发中... |
| Sentiment lens | :smile_cat: 正在开发中... | 
  
</div>

<br />

以下是Empyrial的可用功能。
- ``empyrial'``：对您的投资组合进行定量和性能分析 | [查看如何使用它](https://colab.research.google.com/drive/1cj40dDqctfWNrVz_nK-FDhdWPay7fVBF?usp=sharing)
- ``oracle``：使用几种预测模型（预言家、Auto-ARIMA、快速傅里叶变换...）对您的投资组合进行预测| [见如何使用它](https://colab.research.google.com/drive/11rMpQqW9Om82wzh71cr5k3vDQSNMZ4V1?usp=sharing)


## 用法

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2020-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], 
                  benchmark = ["SPY"] 
)

empyrial(portfolio)
```

Output:

![report](https://user-images.githubusercontent.com/61618641/120065794-8203ef00-c073-11eb-84a8-8dda6908da4c.png)<br/><br /><br />

<div align="center">
  
  ![return](https://user-images.githubusercontent.com/61618641/120065822-afe93380-c073-11eb-915d-8b8b27c6fd38.png)<br /><br /><br />

  ![creturn](https://user-images.githubusercontent.com/61618641/120065881-ea52d080-c073-11eb-84a5-11da5dbf0bcb.png)<br /><br /><br />

  ![heatmap](https://user-images.githubusercontent.com/61618641/120065930-2ab24e80-c074-11eb-8861-e1996a950774.png)<br /><br /><br />

  ![drawdonw](https://user-images.githubusercontent.com/61618641/120065973-6cdb9000-c074-11eb-99cb-f3ee8110576f.png)<br /><br /><br />

  ![top](https://user-images.githubusercontent.com/61618641/120065975-6fd68080-c074-11eb-93f9-cbb3f2dd859d.png)<br /><br /><br />

  ![rolling](https://user-images.githubusercontent.com/61618641/120065977-74029e00-c074-11eb-92c6-8d0bee2a6234.png)
 </div>
 
## 下载泪水表

泪水表将以PDF或HTML文件的形式下载。

### 在Google Colab上

在你的程序中创建另一个单元格并运行该单元格。

```py
!wget -nc https://raw.githubusercontent.com/brpy/colab-pdf/master/colab_pdf.py
from colab_pdf import colab_pdf
colab_pdf('name_of_the_actual_file.ipynb')
```

###在Jupyter笔记本上

在你的程序中创建另一个单元并运行。

```py
pip install nbconvert
```

进入文件 > 下载为 > HTML或PDF通过LaTeX

(对于Visual Studio代码。点击右上角的 "导出为 "图标)

如果你在下载为PDF时出错，就把它下载为HTML文件。

现在打开your_notebook_name.html文件（点击它）。它将在你的浏览器的一个新标签中打开。

现在去打印选项（在页面上点击右键）。从这里你可以把这个文件保存为pdf文件格式。

## 贡献和问题

- [Create an Issue](https://github.com/ssantoshp/Empyrial/issues/new/choose) - 对于较大的改动（如新功能、大型重构等），最好先开一个问题来讨论，较小的改进（如文档改进、bug修复等）可以直接发给PR

- Fork [Empyrial](https://github.com/ssantoshp/Empyrial) - 点击右上角的**Fork**按钮

- 克隆你自己的分叉: ``git clone https://github.com/ssantoshp/Empyrial.git````。

	*如果你的分叉已经过期，你需要手动同步。[同步方法](https://help.github.com/articles/syncing-a-fork/)

- Empyrial使用Github来托管其源代码，如果您想贡献代码，请使用github的PR（拉动请求）程序。[pull requests](https://github.com/ssantoshp/Empyrial/pulls)。它将等待审查、检查/修改并被合并!

## 撰稿人和鸣谢

感谢以下为本项目做出贡献的人/组织。

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
