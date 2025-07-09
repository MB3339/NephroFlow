import setuptools

with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()


    __version__ = "0.0.0"

    Repo_name   = "NephroFlow"
    Author_name = "MB3339"
    src_name   = "cnnClassifier"
    author_email = "meetbhatt96.mb@gmail.com"



setuptools.setup(
    name=src_name,
    version=__version__,
    author=Author_name,
    author_email=author_email,
    description="A package for Kidney Disease Prediction using Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_name}/{Repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{Author_name}/{Repo_name}/issues",
    },
    packages=setuptools.find_packages(where="src"),
)