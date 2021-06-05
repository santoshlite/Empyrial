from setuptools import setup

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='empyrial',
    version='0.3.1',
    description='AI and data-driven quantitative portfolio management library for portfolio risk and performance analysis 投资组合管理',
    py_modules=['empyrial'],
    package_dir={'': 'src'},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ssantoshp/Empyrial',
    author="Santosh Passoubady",
    author_email="santoshpassoubady@gmail.com",
    license='MIT',
    install_requires=[
        'numpy',
        'matplotlib',
        'pandas_datareader',
        'datetime',
        'empyrical',
        'quantstats',
        'yfinance',
        'darts',
        'yahoo-fin',
        'yahoofinancials',
        'prompt-toolkit==3.0.18',
        'ipython==7.22.0'

    ],
)
