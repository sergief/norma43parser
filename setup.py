from distutils.core import setup

setup(
    name="norma43parser",
    packages=["norma43parser"],
    version="1.0",
    license="MIT",
    description="Parser for Bank Account information files formatted in Norma 43",
    author="Sergi Espinar",
    author_email="sergief@users.noreply.github.com",
    url="https://github.com/sergief/norma43parser",
    download_url="https://github.com/sergief/norma43parser/archive/master.zip",
    keywords=["norma43", "parser", "bank", "account", "n43", "csb"],
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
