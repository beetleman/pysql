import setuptools

setuptools.setup(
    name="pysql",
    version="0.1.0",
    url="https://github.com/beetleman/pysql",

    author="Mateusz Probachta",
    author_email="mateusz.probachta@gmail.com",

    description="DSL for SQL",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
