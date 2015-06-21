from setuptools import find_packages, setup

setup(
    name = "Srvr",
    version = "0.1",
    packages = find_packages(),
    scripts = ['src/srvr.py', 'src/authenticate.py', 'src/config.py', 'src/client'],

    entry_points = {
        "console_scripts": [
            "srvr = srvr:run"
            ]
        },

    install_requires = [
        "cement==2.4.0",
        "colorama==0.3.3",
        "pycrypto==2.6.1"
        ],

    author = "Dtripp",
    author_email = "dtrippx@gmail.com",
    description = "Customized real time server alerts & junk",
    license = "MIT",
    long_description = open("README.md").read(),
    url = "https://github.com/dtrip/srvr"
)

