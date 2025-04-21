from setuptools import setup, find_packages

setup(
    name='canvasapiutils',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'canvasapi>=3.0.0',
        'requests>=2.25.0'
    ],
    author='Joshua Hveem',
    author_email='jhveem@btech.edu',
    description='Utilities for simplifying interaction with the Canvas LMS via canvasapi',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/btech-cdd/canvasapiutils',  # Optional if you use GitHub
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
