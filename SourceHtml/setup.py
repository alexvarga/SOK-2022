from setuptools import setup, find_packages

setup(
    name="html-source",
    version="0.1",
    packages=find_packages(),
    install_requires=['core>=0.1'],
    entry_points={
        'code.source':
            ['source_from_html=source_html.services.source_from_html:HtmlSource'],
        'URL.load':
            ['Url=source_html', 'Path=source_html.urls'],
        'INSTALLED_APPS.load':
            ['Config=source_html.apps.SourceHtmlConfig'],
    },
    zip_safe=True
)
