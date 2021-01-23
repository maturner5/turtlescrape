import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="turtlescrape",
    version="1.0.0",
    author="Matt Turner",
    author_email="demexus2@gmail.com",
    description="A simple library used to make web scraping take up less lines"
                " of code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="
