from setuptools import find_packages, setup

setup(
    name="xbots",
    version="0.1.0",
    packages=find_packages(),
    url="https://",
    license="no license",
    author="Anton Shyshko",
    author_email="pozernishku@gmail.com",
    description="Telegram bots stuff",
    install_requires=[
        "python-dotenv",
        "pytelegrambotapi",
        "schedule",
    ],
)
