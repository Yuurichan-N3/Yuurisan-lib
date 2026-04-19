from setuptools import setup, find_packages

setup(
    name='yuurisan',
    version='1.0.1',
    description='Shared Utility Library for Yuuri Bots',
    long_description_content_type="text/markdown",
    author='Yuurisandesu',
    url='https://github.com/Yuurichan-N3/Yuurisan-lib',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'pyfiglet'
    ],
    python_requires='>=3.10',
)
