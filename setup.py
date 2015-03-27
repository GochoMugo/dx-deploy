'''
Setup script for dxdeploy
'''


from setuptools import setup
import dxdeploy


def get_requirements():
    '''Return a list of requirements for installation as listed in the
    requirements.txt file'''
    with open("requirements.txt", "r") as reqsFile:
      reqs = reqsFile.read()
      return reqs.strip().split("\n")


setup(
    name="dxdeploy",
    version=dxdeploy.__version__,
    author="Gocho Mugo I",
    author_email="mugo@forfuture.co.ke",
    url="https://github.com/GochoMugo/dx-deploy",
    download_url="https://github.com/GochoMugo/dx-deploy/zipball/master",
    description="deploy packages to dropbox",
    keywords=["dropbox", "deploy", "packages"],
    license="MIT",
    long_description=dxdeploy.__doc__,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools"
    ],
    packages=["dxdeploy"],
    install_requires=get_requirements()
)
