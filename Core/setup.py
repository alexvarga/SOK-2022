from setuptools import setup, find_packages

setup(
    name="core",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=1.10'],
    package_data={'core': ['static/core/*.*', 'templates/core/*.html']},
    entry_points={
        'INSTALLED_APPS.load':
            ['Config=core.apps.CoreConfig'],
        'URL.load':
            ['Url=core', 'Path=Core.urls']
    },

    zip_safe=False
)
