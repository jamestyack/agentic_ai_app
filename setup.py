from setuptools import setup, find_packages

setup(
    name='agentic_ai_app',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'crewai==0.28.8',
    ],
    entry_points={
        'console_scripts': [
            'agentic_ai_app=src.main:main',
        ],
    },
)