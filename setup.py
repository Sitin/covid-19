import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="covid_19",  # Replace with your own username
    version="0.0.1",
    author="Mykhailo Ziatin",
    author_email="mikhail.zyatin@gmail.com",
    description="Notebooks & charts about COVID-19",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sitin/covid-19",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
