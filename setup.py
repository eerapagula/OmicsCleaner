from setuptools import setup

setup(
    name="omicscleaner",
    version="1.0",
    py_modules=["omicscleaner"],
    package_dir={"": "src"},
    install_requires=[
        "biopython",
        "pandas",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "omicscleaner=omicscleaner:main"
        ]
    },
)
