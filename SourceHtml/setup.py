from setuptools import setup, find_packages

setup(
    name="html-source",
    version="0.1",
    packages=find_packages(),
    install_requires=['core>=0.1'],
    entry_points={
        'code.source':
            ['source_from_html=source_html.code_html.source_from_html:LoadHtmlSource'],
    },
    zip_safe=True
)
