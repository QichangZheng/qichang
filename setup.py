from setuptools import setup, find_packages

setup(
    name='qichang',
    version='0.0.1',
    author='Qichang Zheng',
    author_email='qichangzheng@uchicago.edu',
    description='A Python library for interacting with various language model APIs',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://qichangzheng.net',
    packages=find_packages(),
    install_requires=[
        'requests',
        'ping3'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='language models API client developed by Qichang Zheng',
    python_requires='>=3.7',
)
