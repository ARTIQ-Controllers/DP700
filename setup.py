from setuptools import setup, find_packages

setup(
    name="DP700",
    version="0.1",
    description="ARTIQ support for RIGOL DP700 series power supplies",
    author="OregonIons",
    url="https://github.com/ARTIQ-Controllers/DP700",
    download_url="https://github.com/ARTIQ-Controllers/DP700",
    install_requires=["sipyco", "pyserial"],
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "aqctl_DP700 = DP700.aqctl_DP700:main",
        ],
    },
)