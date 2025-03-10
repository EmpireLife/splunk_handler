from setuptools import setup

setup(
    name='python-sumo-handler',
    version='2.0.8.2',
    license='MIT License',
    description='A Python logging handler that sends your logs to Sumo',
    long_description=open('README.md').read(),
    url='https://github.com/EmpireLife/python-sumo-handler',
    packages=['sumo_handler'],
    install_requires=['requests >= 2.6.0, < 3.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Logging'
    ]
)
