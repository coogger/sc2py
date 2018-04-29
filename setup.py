from setuptools import setup

setup(
    name="sc2py",
    version = "0.6",
    packages = ["sc2py"],
    description = "SteemConnect2 with pyhton",
    author = "Hakan Çelik",
    author_email = "hakancelik96@outlook.com",
    url = "https://github.com/hakancelik96/sc2py",
    python_requires='>=3.5.0',
    py_modules=['sc2py'],
    include_package_data = True,
    install_requires = ["requests"],
    keywords = ["steem","steemit","sc2py","steemconnect","sc2"],
    download_url = "https://github.com/hakancelik96/sc2py/archive/0.6.tar.gz",
    license = "MIT",
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
