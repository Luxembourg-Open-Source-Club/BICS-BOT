from setuptools import setup

package_name = "bics_bot"

setup(
    name=package_name,
    version="0.0.1",
    author="Pedro Soares",
    author_email="pmbs.123@gmail.com",
    packages=[package_name],
    description="Code source of the discord BICS bot",
    install_requires=[
        "nextcord",
    ],
)