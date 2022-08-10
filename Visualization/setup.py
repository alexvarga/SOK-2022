from setuptools import setup, find_packages

setup(
    name="visualisation",
    version="0.1",
    packages=find_packages(),
    install_requires=['core>=0.1'],
    entry_points = {
        'code.visualization':
            ['visualization_code=visualization.visualization_code.visualize:Visualization'],
    },
    zip_safe=True
)