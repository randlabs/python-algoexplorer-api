import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="python-algoexplorer-api",
    description="Algorand SDK in Python",
    author="Randlabs.io",
    author_email="support@randlabs.io",
    version="1.0.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache-2.0",
    project_urls={
        "Source": "https://github.com/randlabs/python-algoexplorer-api",
    },
    install_requires=["py-algorand-sdk"],
    packages=["algoexplorersdk"],
    python_requires=">=3.5",
)