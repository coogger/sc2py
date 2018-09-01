from setuptools import setup

setup(
    name="steem-connect",
    version = "0.7.3",
    packages = ["steemconnect"],
    description = "SteemConnect with pyhton",
    author = "Hakan Çelik",
    author_email = "hakancelik96@outlook.com",
    url = "https://github.com/hakancelik96/steemconnect",
    python_requires='>=3.5.0',
    long_description=read('README.md'),
    py_modules=['steemconnect'],
    include_package_data = True,
    install_requires = ["requests"],
    keywords = ["steem", "steemit", "steemconnect", "sc2", "steem-connect"],
    license = "MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
