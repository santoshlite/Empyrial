
# By Investors, For Investors.
<br><br><br><br>
<div align="center">
<img src="https://user-images.githubusercontent.com/61618641/120909011-98f8a180-c670-11eb-8844-2d423ba3fa9c.png"/>
<br><br><br><br><br><br>
  
![](https://img.shields.io/badge/Downloads-16k/month-brightgreen)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/version-1.8.7-blueviolet)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/activity-9.7/10-ff69b4)
![](https://img.shields.io/badge/Open%20source-💜-white)	
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1NqTkkP2u1p1g8W8erU-Y-rSSVbPUDvq2?usp=sharing)
  
 </div>
 
<br><br>

Want to read this in **Chinese**? Click [**here**](README_CN.md)

Empyrial is a Python-based **open-source quantitative investment** library dedicated to **financial institutions** and **retail investors**, officially released in Mars 2021. Already used by **thousands of people working in the finance industry**, Empyrial aims to become an all-in-one platform for **portfolio management**, **analysis**, and **optimization**.

Empyrial **empowers portfolio management** by bringing the best of **performance and risk analysis** in an **easy to understand**, **flexible** and **powerful framework**.

With Empyrial, you can easily analyze security or a portfolio in order to **get the best insights from it**.

<br>

<br>

<div align="center">
  
| Table of Contents 📖 | 
| --                     
| 1. [Installation](#installation) | 
| 2. [Features](#features) | 
| 3. [Usage example](#usage) |
| 4. [Download the tearsheet](#download-the-tearsheet) |
| 5. [Contribution and Issues](#contribution-and-issues) | 
| 6. [Contributors](#contributors) |
| 7. [Contact](#contact) |
| 8. [License](#license) |
	
</div>


## Installation

You can install Empyrial using pip:

```
pip install empyrial
```

For a better experience, **we advise you to use Empyrial on a notebook** (Jupyter, Google Colab...)

## Features

<div align="center">
  
| Feature 📰 | Status |
| --                      | ------    |
| Engine (backtesting + performance analysis) | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.2.4) on May 30, 2021 |
| Optimizer | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.3.6) on Jun 7, 2021 |
| Rebalancing | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.5.0) on Jun 27, 2021 |
| Risk manager | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/v1.7.3) on Jul 5, 2021 |
| Sandbox | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/v1.8.9) on Jul 17, 2021 |
  
</div>

## Usage

**Empyrial**

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2018-06-09", 
                  portfolio= ["BABA", "PDD", "KO", "AMD","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #equal weighting by default
                  benchmark = ["SPY"] #SPY by default
)

empyrial(portfolio)
```
<br>

**Calendar Rebalancing**

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2018-06-09", 
                  portfolio= ["BABA", "PDD", "KO", "AMD","^IXIC"], 
		  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #equal weighting by default
                  benchmark = ["SPY"], #SPY by default
		  rebalance = "1y"
)

empyrial(portfolio)
```

Time periods available for rebalancing are ```2y```,```1y```,```6mo```,```quarterly```,```monthly```

<br/>

**Custom Rebalancing**

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2018-06-09", 
                  portfolio= ["BABA", "PDD", "KO", "AMD","^IXIC"], 
		  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #equal weighting by default
                  benchmark = ["SPY"], #SPY by default
		  rebalance = ["2018-06-09", "2019-01-01", "2020-01-01", "2021-01-01"]
)

empyrial(portfolio)
```

<br/>

**Optimizer**

There are 5 optimizers available:

- ```"EF"```: **Global Efficient Frontier**

- ```"MEANVAR"```: **Mean-Variance** (in this case, you'll have to define a max volatility that you don't want to exceed)

- ```"HRP"```: **Hierarchical Risk Parity**

- ```"MINVAR"```: **Minimum-Variance**

- ```"BL"```: **Black Litterman** (in this case, you'll have to define you're views and confidences on the assets you invest in)

_Note: the default optimizer is **equal weighting**_


```py
from empyrial import empyrial, Engine

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = ["BLK", "BAC", "AAPL", "TM", "JPM","JD", "INTU", "NVDA", "DIS", "TSLA"],
      optimizer = "EF" 
)

portfolio.weights
```

Output:

```
[0.31409, 0.0, 0.03472, 0.00046, 0.0, 0.0, 0.069, 0.08831, 0.00854, 0.48489]
```

**Risk Manager**

3 Risk managers are available:

- **Max Drawdown**: ```{"Max Drawdown" : -0.3}```
- **Take Profit**: ```{"Take Profit" : 0.4}```
- **Stop Loss**: ```{"Stop Loss" : -0.2}```

```py
from empyrial import empyrial, Engine

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = ["BLK", "BAC", "AAPL", "TM", "JPM","JD", "INTU", "NVDA", "DIS", "TSLA"],
      optimizer = "EF",
      risk_manager = {"Stop Loss" : -0.2}
)
``` 


## Download the Tearsheet

Want to download a tear sheet of the analysis as a PDF or HTML file? You can check out [documentation](https://github.com/ssantoshp/Empyrial/wiki/Downloading-the-generated-tearsheet) to find out how to do this.

## Stargazers over time

<div align="center">
	
![追星族的时间](https://starchart.cc/ssantoshp/empyrial.svg)
	
</div>

## Contribution and Issues

- [Create Issue](https://github.com/ssantoshp/Empyrial/issues/new/choose) - For the larger changes (such as new features, large refactoring, etc.) it is best to first open an issue to discuss, and smaller improvements (such as document improvements, bugfixes, etc.) can be sent directly to PR

- Fork [Empyrial](https://github.com/ssantoshp/Empyrial) - Click the **Fork** button in the upper right corner

- Clone your own fork: ```git clone https://github.com/ssantoshp/Empyrial.git```

	* If your fork is out of date, you need to manually sync: [Synchronization method](https://help.github.com/articles/syncing-a-fork/)

- Empyrial uses GitHub to host its source code, if you wish to contribute code please use the PR (Pull Request) process of GitHub: [pull requests](https://github.com/ssantoshp/Empyrial/pulls). It'll waiting for review, checked/modified and be merged!

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-8-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/rslopes"><img src="https://avatars.githubusercontent.com/u/24928343?v=4" width="100px;" alt=""/><br /><sub><b>Renan Lopes</b></sub></a><br /><a title="Code">💻</a> <a title="Bug report">🐛</a></td>
    <td align="center"><a href="https://github.com/diegodalvarez"><img src="https://avatars.githubusercontent.com/u/48641554?v=4" width="100px;" alt=""/><br /><sub><b>Diego Alvarez</b></sub></a><br /><a title="Code">💻🐛</a></td>
    <td align="center"><a href="https://github.com/rakeshbhat9"><img src="https://avatars.githubusercontent.com/u/11472305?v=4" width="100px;" alt=""/><br /><sub><b>Rakesh Bhat</b></sub></a><br /><a title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/Haizzz"><img src="https://avatars.githubusercontent.com/u/5275680?v=4" width="100px;" alt=""/><br /><sub><b>Anh Le</b></sub></a><br /><a title="Bug report">🐛</a></td>
    <td align="center"><a href="https://github.com/TonyZhangkz"><img src="https://avatars.githubusercontent.com/u/65281213?v=4" width="100px;" alt=""/><br /><sub><b>Tony Zhang</b></sub></a><br /><a title="Code">💻</a></td>
    <td align="center"><a href="https://github.com/eltociear"><img src="https://avatars.githubusercontent.com/u/22633385?v=4" width="100px;" alt=""/><br /><sub><b>Ikko Ashimine</b></sub></a><br /><a title="Code">✒️</a></td>
    <td align="center"><a href="https://www.youtube.com/watch?v=-4qx3tbtTgs"><img src="https://avatars.githubusercontent.com/u/50767660?v=4" width="100px;" alt=""/><br /><sub><b>QuantNomad</b></sub></a><br /><a title="Code">📹</a></td>
    <td align="center"><a href="https://github.com/agn35"><img src="https://lh3.googleusercontent.com/a-/AOh14GhXGFHHpVQTL2r23oEXFssH0f7RyoGDihrS_HmT=s48" width="100px;" alt=""/><br /><sub><b>Adam Nelsson</b></sub></a><br /><a title="Code">📓</a></td>
  </tr>
</table>

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. **Contributions of any kind are welcome!**


## Contact

You are welcome to contact us by email at santoshpassoubady@gmail.com or in Empyrial's [discussion space](https://github.com/ssantoshp/Empyrial/discussions)

## License

MIT
