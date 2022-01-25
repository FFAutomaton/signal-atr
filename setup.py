import setuptools

REQUIRED_PACKAGES = []

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="signal_atr",
    version="1.0",
    author="turkish gekko",
    author_email="turkish-gekko@turkish-gekko.org",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/turkish-gekko/signal-atr",
    install_requires=REQUIRED_PACKAGES,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
