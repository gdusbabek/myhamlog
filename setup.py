import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()
long_description="Logs to N3FJP from the command line"

setuptools.setup(
    name="n3fjp-gdusbabek",
    version="0.0.1",
    author="Gary Dusbabek",
    author_email="gdusbabek@gmail.com",
    description=long_description,
    long_description=long_description,
    long_description_content_type="text/text",
    url="https://github.com/gdusbabek",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7",
    scripts=["scripts/n3fjp"],
)