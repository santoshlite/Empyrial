from distutils.core import setup
setup(
  name = 'trafalgar',         # How you named your package folder (MyLib)
  packages = ['trafalgar'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Trafalgar is a python library to make development of portfolio analysis faster and easier',   # Give a short description about your library
  author = 'Santosh Passoubady',                   # Type in your name
  author_email = 'your.email@domain.com',      # Type in your E-Mail
  url = 'https://github.com/ssantoshp/trafalgar',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Portfolio management', 'Quantitative finance', 'Efficient frontier', 'Stock analysis', 'Porfolio analysis' ],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'tabulate',
          'datetime',
          'fix_yahoo_finance',
          'statsmodels',
          'seaborn'
      ],
  classifiers=[
    'Development Status :: Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers, Porfolio manager, quants',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
