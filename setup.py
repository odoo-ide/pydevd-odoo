from setuptools import setup, find_packages

setup(
    name='pydevd-odoo',
    version='1.0',
    description='PyDev.Debugger plugin for Odoo',
    url='https://github.com/trinhanhngoc/pydevd-odoo',
    author='Trinh Anh Ngoc',
    author_email='atw1990@gmail.com',
    packages=find_packages(),
    namespace_packages=['pydevd_plugins.extensions'],
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
