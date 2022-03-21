import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='signal-cli-socket',
    version='0.5',
    packages=["signal_cli_socket"],
    author="Nickwasused",
    author_email="nickwasused.social@protonmail.com",
    description="A package to use with the signal-cli made by AsamK.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nickwasused/signal-cli-socket",
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
         "Operating System :: OS Independent",
     ],
)