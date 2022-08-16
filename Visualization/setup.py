from setuptools import setup, find_packages

setup(
    name="visualization",
    version="0.1",
    packages=find_packages(),
    install_requires=['core>=0.1'],
    entry_points={
        'code.visualization':
            ['visualization_plugin=visualization.services.visualize:Visualization'],
        'URL.load':
            ['Url=visualization', 'Path=visualization.urls'],
        'INSTALLED_APPS.load':
            ['Config=visualization.apps.VisualizationConfig'],
    },
    zip_safe=True
)
