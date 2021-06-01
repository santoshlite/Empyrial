# By Investors, For Investors.
<br><br><br><br><br><br>
<div align="center">
<img src="https://i.ibb.co/RjLg9VV/logo.png"/>
<br><br><br><br><br><br>
  
![](https://img.shields.io/badge/Downloads-5.8k-brightgreen)
![](https://img.shields.io/badge/license-MIT-orange)
![](https://img.shields.io/badge/version-0.2.6-blueviolet)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/activity-8.8/10-yellow)
![](https://camo.githubusercontent.com/97d4586afa582b2dcec2fa8ed7c84d02977a21c2dd1578ade6d48ed82296eb10/68747470733a2f2f6261646765732e66726170736f66742e636f6d2f6f732f76312f6f70656e2d736f757263652e7376673f763d313033)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ssantoshp/GetStartedEmpyrial/main?filepath=get_started_with_empyrial.ipynb)
  
 </div>
 
<br><br>

  
Empyrial is a Python-based **open source quantitative investment** library dedicated to **financial institutions** and **retail investors**, officially released in Mars 2021. Already used by **thousands of people working in the finance industry**, Empyrial aims to become a all-in-one platform for **portfolio management**, **analysis** and **optimization**.
<br><br><br>


<div align="center">
  
| Feature 📰 | Status |
| --                      | ------    |
| Empyrial (backtesting + performance analysis) | :star: [Released](https://colab.research.google.com/drive/1cj40dDqctfWNrVz_nK-FDhdWPay7fVBF?usp=sharing) on May 30, 2021 | 
| Oracle (prediction lens using several ML models)| :alien: [First Release](https://colab.research.google.com/drive/11rMpQqW9Om82wzh71cr5k3vDQSNMZ4V1?usp=sharing) on Jun 1, 2021 | 
| Fundamental lens | :smile_cat: In development...  |
| Risk lens | :smile_cat: In development...  | 
| Alpha lens | :smile_cat: In development... |
| Sentiment lens | :smile_cat: In development... | 
  
</div>

<br>

## Installation 🔥

To install Empyrial, you should do:

```
pip install empyrial
```

## Usage 

Here are the functions available with Empyrial:
- ```empyrial``` : quantitative and performance analysis of your portfolio | [See how to use it](https://colab.research.google.com/drive/1cj40dDqctfWNrVz_nK-FDhdWPay7fVBF?usp=sharing)
- ```oracle``` : prediction generation on your portfolio using several prediction models (Prophet, Auto-ARIMA, Fast Fourier Transform...) | [See how to use it](https://colab.research.google.com/drive/11rMpQqW9Om82wzh71cr5k3vDQSNMZ4V1?usp=sharing)
- ```get_returns```
- ```get_pricing```
- ```get_data```
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
 
## Download the tearsheet (to PDF)

### On Google Colab

Create another cell in your program and run that:

```py
!wget -nc https://raw.githubusercontent.com/brpy/colab-pdf/master/colab_pdf.py
from colab_pdf import colab_pdf
colab_pdf('name_of_the_actual_file.ipynb')
```

### On a Jupyter Notebook

Create another cell in your program and run:

```py
pip install nbconvert
```

Go to Files > Download as > HTML or PDF via LaTeX

(For Visual Studio Code: Click on the "export as" icon in the upper right corner)

If you get an error downloading it as a PDF, download it as a HTML file.

Now open that your_notebook_name.html file (click on it). It will be opened in a new tab of your browser.

Now go to print option (right-click on the page). From here you can save this file in pdf file format.

vn.py uses Github to host its source code, if you wish to contribute code please use the PR (Pull Request) process of github:

## Contribution and Issues

- [Create Issue](https://github.com/ssantoshp/Empyrial/issues/new/choose) - For the larger changes (such as new features, large refactoring, etc.) it is best to first open an issue to discuss, and smaller improvements (such as document improvements, bugfixes, etc.) can be sent directly to PR

- Fork [Empyrial](https://github.com/ssantoshp/Empyrial) - Click the **Fork** button in the upper right corner

- Clone your own fork: ```git clone https://github.com/ssantoshp/Empyrial.git```

	* If your fork is out of date, you need to manually sync: [Synchronization method](https://help.github.com/articles/syncing-a-fork/)

- If you want to make contributions to ```Empyrial```, please create [pull requests](https://github.com/ssantoshp/Empyrial/pulls). It'll waiting for review, need to continue to improve, or be merged!

## Contact us

You are welcome to contact us by email at santoshpassoubady@gmail.com or in Empyrial's [discussion space](https://github.com/ssantoshp/Empyrial/discussions)

## License

MIT
