import sys
from setuptools import setup, find_packages

sys.dont_write_bytecode = True

setup(
    name="EmadicBot",
    version="0.0.1",
    description='Emadic Bot.',
    long_description='',
    author='Mundia Mwala',
    author_email='mundiamwala@gmail.com',
    url='https://bot.emadic.com',
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "emadicbot=emadicbot.cli:run",
        ],
    },
    install_requires=[
        "Flask==2.0.1",
        "redis==4.1.1",
        "gunicorn==20.0.4",
        "python-dotenv==0.17.0",
    ],
    license="proprietary and confidential",
    python_requires=">=3.7",
)
