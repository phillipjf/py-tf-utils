import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_requirements(env=""):
    path = os.path.dirname(os.path.abspath(__file__))
    fn = "requirements{}{}.txt".format(("-" if env else ""), env)
    with open(os.path.join(path, fn)) as fp:
        return [x.strip() for x in fp.read().split("\n") if not x.startswith("#")]


install_requires = get_requirements()

setuptools.setup(
    name="py-tf-utils",
    version="0.2.0",
    author="Phillip Ferentinos",
    author_email="phillip.jf@gmail.com",
    description="Various Terraform Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phillipjf/tf-utils",
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3"],
    python_requires=">=3.6",
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        tf-utils=tf_utils.main:main
    """,
)
