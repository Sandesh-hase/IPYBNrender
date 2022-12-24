import setuptools

with open("README.md", "r", encoding="uif-8") as f:
    long_decsription = f.read()

__version__ = "0.0.0"

REPO_NAME = "IPYNBrenderer"
AUTHOR_USER_NAME = "Sandesh-Hase"
SRC_REPO = "IPYNBrenderer"
AUTHOR_EMAIL ="andeshhase15@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_decsription,
    long_decsription_content="text/markdown",
    url=f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={
        "Bug Tracker": f"https://github.com{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
)