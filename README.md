✋ 🛑 **DISCLAIMER: Trafalgar became Empyrial**
Trafalgar is still usable but it will not be maintaned. Empyrial is still in development so there are **bugs** but there will be a lot more than Trafalgar!

# By Investors, for Investors.
<br><br><br><br><br><br>
<div align="center">
<img src="https://i.ibb.co/RjLg9VV/logo.png"/>
<br><br><br><br><br><br>
  
![](https://img.shields.io/badge/Users-1.2k-brightgreen)
![](https://img.shields.io/badge/license-MIT-blue)
![](https://img.shields.io/badge/flow%20level-A++-brightgreen)
![](https://img.shields.io/badge/language-python🐍-blue)
![](https://img.shields.io/badge/views-+11k-red)
![](https://img.shields.io/badge/activity-8.8/10-yellow)
![](https://camo.githubusercontent.com/97d4586afa582b2dcec2fa8ed7c84d02977a21c2dd1578ade6d48ed82296eb10/68747470733a2f2f6261646765732e66726170736f66742e636f6d2f6f732f76312f6f70656e2d736f757263652e7376673f763d313033)

<br>
Featured on
<br><br>

<img align="left" src="https://www.libhunt.com/assets/logo/logo-og-12f445719d17ec887b4f67216c07a38850ebfbc93ed81fa8b3bbb338d63a7adb.png" width="200"/>
<img align="left" src="https://cdn-images-1.medium.com/max/1200/1*NHYVDHC_WbdaUicoYyJFrA.png" width="100"/>
<img align="left" src="https://cdn-images-1.medium.com/max/1200/1*yAqDFIFA5F_NXalOJKz4TA.png" width="100"/>
<img align="left"src="https://pychina.org/img/pycon.png" width="100"/><br><br>
<img align="left"src="https://i.ibb.co/r4ZzyLQ/Capture.jpg" width="200"/>
</div>



<br><br><br><br><br><br>

## Installation 🔥

To install Empyrial, you should do:

```
pip install empyrial
```

## Usage 
```py
from empyrial import returns, empyrial
import pandas as pd

#define your portfolio
portfolio = ["BABA", "RELIANCE.NS", "KO", "^DJI","^IXIC"]
wts = [0.2, 0.2, 0.2, 0.2, 0.2]

#calculate the portfolio returns
port_ret = returns(portfolio, wts, period="1y", plot=False)
port_ret = pd.DataFrame(port_ret['Portfolio returns'])

#calculate benchmark returns
bench = returns(["SPY"], period="1y", plot=False)

#execute
empyrial(port_ret,bench)
```

Output:

 <img src="https://i.ibb.co/1JS42qK/pic.png"/>





