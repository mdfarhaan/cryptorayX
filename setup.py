from setuptools import setup, find_packages

long_desc = open('README.txt').read()

setup(
  name='cryptoflash',
  version='0.0.1',
  py_modules=['cryptoflash'],
  url='https://github.com/mdfarhaan/cryptoflash',
  author='Mohammed Farhaan',
  author_email='farhaanm110@gmail.com',
  description='Lightweight Python module to get Crypto currency price',
  long_description=long_desc,  
  packages=find_packages(),
  license='MIT',
  install_requires=[
    'requests==2.21.0',
    'CurrencyConverter==0.16'
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
  ],
)

