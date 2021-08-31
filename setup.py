from setuptools import find_packages, setup

setup(
    name="soda-spark",
    packages=find_packages("src/"),
    version="0.1.0",
    description="Soda SQL API for PySpark data frame",
    author="Soda",
    extras_require={
        "dev": [
            "pre-commit==2.14.1",
            "pytest-spark==0.6.0",
            "pytest-cov==2.12.1",
            "pyspark==3.1.2",
        ]
    },
    package_dir={"": "src"},
)