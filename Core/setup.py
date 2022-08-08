from setuptools import setup, find_packages

setup(
    name="core",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=1.10'],

    package_data={'core': ['static/core/*.*', 'templates/core/*.html']},
    zip_safe=False
)
