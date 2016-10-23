#
# Copyright (c) 2016, Michael Conroy
#


from setuptools import setup, find_packages


setup(
    name='elevator',
    version='0.1.0',
    description='An elevator system simulation',
    long_description=open('README.rst', 'r').read(),
    keywords='elevator system algorithm',
    author='Michael Conroy',
    author_email='sietekk@gmail.com',
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        # TODO: Implement PY3 support
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
        'Topic :: Education',
        'Topic :: Games/Entertainment :: Simulation',
    ],
    url='https://github.com/sietekk/elevator',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    zip_safe=True,
    include_package_data=True,
    #namespace_packages=['elevator'],
    # TODO: Implement CLI
    #entry_points={
    #    'console_scripts': [
    #        'elevate = elevate.scripts',
    #    ]
    #},
    install_requires=[
        'six>=1.5,<2',
        'transitions==0.4.2',
    ],
    extras_require={
        'dev': [
            'pbbt>=0.1.4,<1',
            'coverage>=3.7,<4',
            'nose>=1.3,<2',
            'nosy>=1.1,<2',
            'prospector[with_pyroma]>=0.12,<0.13',
            'twine>=1.5,<2',
            'wheel>=0.24,<0.25',
            'Sphinx>=1.3,<2',
            'sphinx-autobuild>=0.5,<0.6',
            'tox>=2,<3',
            'flake8>=2.5.0,<3',
        ],
    },
    test_suite='nose.collector',
)
