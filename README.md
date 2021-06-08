
# By Investors, For Investors.
<br><br><br><br>
<div align="center">
<img src="https://user-images.githubusercontent.com/61618641/120909011-98f8a180-c670-11eb-8844-2d423ba3fa9c.png"/>
<br><br><br><br><br><br>
  
![](https://img.shields.io/badge/Downloads-7.3k-brightgreen)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/version-1.3.6-blueviolet)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/activity-8.8/10-ff69b4)
![](https://img.shields.io/badge/Open%20source-💜-white)	
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ssantoshp/GetStartedEmpyrial/main?filepath=get_started_with_empyrial.ipynb)
  
 </div>
 
<br><br>

Want to read this in **Chinese**? Click [**here**](README_CN.md)

Empyrial is a Python-based **open-source quantitative investment** library dedicated to **financial institutions** and **retail investors**, officially released in Mars 2021. Already used by **thousands of people working in the finance industry**, Empyrial aims to become an all-in-one platform for **portfolio management**, **analysis**, and **optimization**.

Empyrial **empowers portfolio management** by bringing different financial approaches such as **risk analysis**, **quantitative analysis**, **fundamental analysis**, **factor analysis** and **prediction making**.

With Empyrial, you can easily analyze security or a portfolio with these different approaches and **get the best insights from it**.

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
| 6. [Contributors and Acknowledgments](#contributors-and-acknowledgments) |
| 7. [Contact](#contact) |
| 8. [License](#license) |
	
</div>


## Installation

To install Empyrial, you should do:

```
pip install empyrial
```

## Features

<div align="center">
  
| Feature 📰 | Status |
| --                      | ------    |
| Empyrial (backtesting + performance analysis) | :star: [Released](https://github.com/ssantoshp/Empyrial/releases/tag/1.2.4) on May 30, 2021 |
| Oracle (prediction lens using several ML models)| :alien: [Beta](https://github.com/ssantoshp/Empyrial/releases/tag/1.2.7) on Jun 1, 2021 | 
| Fundamental lens | :alien: [Beta](https://github.com/ssantoshp/Empyrial/releases/tag/1.3.1) on Jun 6, 2021 |
| Optimizer | :alien: [Beta](https://github.com/ssantoshp/Empyrial/releases/tag/1.3.6) on Jun 7, 2021 |
| Risk factors lens | :smile_cat: In development...  | 
| Sentiment lens | :smile_cat: In development... | 
  
</div>

<br />

Here are the functions available with Empyrial:

- ```empyrial``` : **quantitative portfolio analytics** | [Quickstart](https://colab.research.google.com/drive/1cj40dDqctfWNrVz_nK-FDhdWPay7fVBF?usp=sharing) | [Documentation](https://github.com/ssantoshp/Empyrial/wiki/Empyrial)

- ```oracle``` : **prediction generation** on your portfolio using several prediction models (Prophet, Auto-ARIMA, Fast Fourier Transform...) | [Quickstart](https://colab.research.google.com/drive/11rMpQqW9Om82wzh71cr5k3vDQSNMZ4V1?usp=sharing) | [Documentation](https://github.com/ssantoshp/Empyrial/wiki/Oracle)

- ```fundlens``` : **fundamental analysis** of each of the assets in your portfolio | [Quickstart](https://colab.research.google.com/drive/1t2RfYwIJDZ3YN1z5MbS41unRGxGf0dif?usp=sharing) | [Documentation](https://github.com/ssantoshp/Empyrial/wiki/Fundlens)

- ```optimizer``` : **optimize the asset's allocation** in your portfolio | [Quickstart](https://colab.research.google.com/drive/12CfYznbdabSDYUbtSwamqyILOIwR7Sje?usp=sharing)

## Usage

**Empyrial**

```py
from empyrial import empyrial, Engine

portfolio = Engine(    
                  start_date= "2020-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #equal weighting by default
                  benchmark = ["SPY"] 
)

empyrial(portfolio)
```
[See the output](https://github.com/ssantoshp/Empyrial/wiki/Empyrial)

<br />

**Oracle**

```py
from empyrial import oracle, Engine

portfolio = Engine(    
                  start_date= "2020-06-09", 
                  portfolio= ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"], 
                  weights = [0.2, 0.2, 0.2, 0.2, 0.2], #equal weighting by default
                  benchmark = ["SPY"] #optionnal
)

oracle(portfolio)
```

[See the output](https://github.com/ssantoshp/Empyrial/wiki/Oracle)

<br />

**Fundlens**

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

[See the output](https://github.com/ssantoshp/Empyrial/wiki/Fundlens)

<br />

**Optimizer**

There is two ways to use the Empyrial's optimizer :

1) Optimize allocation directly with Engine
```py
from empyrial import*

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

2) See the performance of an optimizer
```py
from empyrial import*

portfolio = Engine(
      start_date = "2018-01-01",
      portfolio = ["BLK", "BAC", "AAPL", "TM", "JPM","JD", "INTU", "NVDA", "DIS", "TSLA"]
)

optimizer(portfolio, "EF")
```

Output:

<div align="center">
	
![2021-06-08_22h15_09](https://user-images.githubusercontent.com/61618641/121251316-04c44f80-c8a7-11eb-9451-e96b9fd7eff5.png)

</div>

<br />

## Download the tearsheet

Want to download of a tearsheet of the analysis as a PDF or a HTML file? You can check the [documentation](https://github.com/ssantoshp/Empyrial/wiki/Downloading-the-generated-tearsheet) to see how to do it :)


## Contribution and Issues

- [Create Issue](https://github.com/ssantoshp/Empyrial/issues/new/choose) - For the larger changes (such as new features, large refactoring, etc.) it is best to first open an issue to discuss, and smaller improvements (such as document improvements, bugfixes, etc.) can be sent directly to PR

- Fork [Empyrial](https://github.com/ssantoshp/Empyrial) - Click the **Fork** button in the upper right corner

- Clone your own fork: ```git clone https://github.com/ssantoshp/Empyrial.git```

	* If your fork is out of date, you need to manually sync: [Synchronization method](https://help.github.com/articles/syncing-a-fork/)

- Empyrial uses Github to host its source code, if you wish to contribute code please use the PR (Pull Request) process of github: [pull requests](https://github.com/ssantoshp/Empyrial/pulls). It'll waiting for review, checked/modified and be merged!

## Contributors and Acknowledgments

Thanks to the following people/organizations who have contributed to this project:

- [@rslopes](https://github.com/rslopes)
- [@TonyZhangkz](https://github.com/TonyZhangkz)
- [@rakeshbhat9](https://github.com/rakeshbhat9)
- [@Haizzz](https://github.com/Haizzz)
- [quantstats](https://github.com/ranaroussi/quantstats)
- [quantopian](https://github.com/quantopian)
- [unit8co](https://github.com/unit8co)

## Contact

You are welcome to contact us by email at santoshpassoubady@gmail.com or in Empyrial's [discussion space](https://github.com/ssantoshp/Empyrial/discussions)

## License

MIT
