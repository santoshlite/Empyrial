#### 📢 Announcement 
Good news! You can now use a patched version of the library [empyrical](https://github.com/quantopian/empyrical) through EigenLedger! 🎉
<br>
👉 Learn [how to use it here](https://eigenledger.gitbook.io/eigenledger/using-empyrical/using-empyrical) and read more in [this announcement post](https://github.com/santoshlite/EigenLedger/discussions/128).
<br>

# By Investors, For Investors.
<br>
<div align="center">
<img src="https://github.com/user-attachments/assets/470f1d59-09c6-4b95-af7e-f142764d8195"/>
<br><br><br><br>

![](https://img.shields.io/badge/Downloads-245k-brightgreen)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/version-2.1.6-blueviolet)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/Open%20source-💜-white)	
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1TyNgudyFcsgob7o49PwfDJHLaHvluxaU?usp=sharing)
  
 </div>

<br>

Want to read this in **Mandarin 🇨🇳**? Click [**here**](README_CN.md)

EigenLedger (prev. "Empyrial") is a Python-based **open-source quantitative investment** library dedicated to **financial institutions** and **retail investors**, officially released in 2021. Already used by **thousands of people working in the finance industry**, EigenLedger aims to become an all-in-one platform for **portfolio management**, **analysis**, and **optimization**.

EigenLedger **empowers portfolio management** by bringing the best of **performance and risk analysis** in an **easy-to-understand**, **flexible** and **powerful framework**.

With EigenLedger, you can easily analyze security or a portfolio in order to **get the best insights from it**. This is mainly a **wrapper** of financial analysis libraries such as **Quantstats** and **PyPortfolioOpt**.

<br>

<br>



<div align="center">
  
| Table of Contents 📖 | 
| --                     
| 1. [Installation](#installation) | 
| 2. [Documentation](#documentation) | 
| 3. [Quickstart](#quickstart) |
| 4. [Contribution and Issues](#contribution-and-issues) | 
| 5. [Contributors](#contributors) |
| 6. [Contact](#contact) |
| 7. [License](#license) |
	
</div>




## Installation

You can install EigenLedger using pip:

```
pip install EigenLedger
```

For a better experience, **we advise you to use EigenLedger on a notebook** (e.g., Jupyter, Google Colab)

_Note: macOS users will need to install [Xcode Command Line Tools](https://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/)._

_Note: Windows users will need to install C++. ([download](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16), [install instructions](https://drive.google.com/file/d/0B4GsMXCRaSSIOWpYQkstajlYZ0tPVkNQSElmTWh1dXFaYkJr/view))_



## Documentation

Here is our full [documentation](https://eigenledger.gitbook.io/documentation)! Check it out our full documentation for detailed guides, all features, and tips on getting the most out of this library.



## Quickstart

```py
from EigenLedger import portfolio_analysis, Engine

portfolio = Engine(
    start_date = "2018-08-01", 
    portfolio = ["BABA", "PDD", "KO", "AMD","^IXIC"], 
    weights = [0.2, 0.2, 0.2, 0.2, 0.2],  # equal weighting is set by default
    benchmark = ["SPY"]  # SPY is set by default
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


## Stargazers over time

<div align="center">
	
![追星族的时间](https://starchart.cc/ssantoshp/empyrial.svg)
	
</div>

## Contribution and Issues
EigenLedger uses GitHub to host its source code.  *Learn more about the [Github flow](https://docs.github.com/en/get-started/quickstart/github-flow).*  

For larger changes (e.g., new feature request, large refactoring), please open an issue to discuss first.  

* If you wish to create a new Issue, then [click here to create a new issue](https://github.com/ssantoshp/EigenLedger/issues/new/choose).  

Smaller improvements (e.g., document improvements, bugfixes) can be handled by the Pull Request process of GitHub: [pull requests](https://github.com/ssantoshp/EigenLedger/pulls).  

* To contribute to the code, you will need to do the following:  

 * [Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository) [EigenLedger](https://github.com/ssantoshp/EigenLedger) - Click the **Fork** button at the upper right corner of this page. 
 * [Clone your own fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository).  E.g., ```git clone https://github.com/ssantoshp/EigenLedger.git```  
  *If your fork is out of date, then will you need to manually sync your fork: [Synchronization method](https://help.github.com/articles/syncing-a-fork/)*
 * [Create a Pull Request](https://github.com/ssantoshp/EigenLedger/pulls) using **your fork** as the `compare head repository`. 

You contributions will be reviewed, potentially modified, and hopefully merged into EigenLedger.  

## Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

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

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. **Contributions of any kind are welcome!**

## Credit

This library has also been made possible because of the work of these incredible people:
- [**Ran Aroussi**](https://github.com/ranaroussi) for the [**Quantstats library**](https://github.com/ranaroussi/quantstats) 
- [**Robert Martin**](https://github.com/robertmartin8) for the [**PyPortfolioOpt**](https://github.com/robertmartin8/PyPortfolioOpt) 

## Contact

You are welcome to contact us by email at **santoshpassoubady@gmail.com** or in EigenLedger's [discussion space](https://github.com/ssantoshp/EigenLedger/discussions)

## License

Apache License 2.0