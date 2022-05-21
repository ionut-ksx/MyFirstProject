from setuptools import setup, find_packages

setup(
    name="pydemo",
    version="0.0.1",
    description="Python demo",
    author="Team",
    author_email="",
    # url="https://github.com/CleverSoftwareSolutions/fashion_flask/",
    package_dir={"": "src/"},
    packages=find_packages("src/"),
)
