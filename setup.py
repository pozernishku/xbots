from setuptools import find_packages, setup

setup(
    name="xbots",
    version="0.1.0",
    packages=find_packages(),
    url="https://github.com/pozernishku/xbots",
    license="no license",
    author="Anton Shyshko",
    author_email="pozernishku@gmail.com",
    description="Telegram bots stuff",
    python_requires=">=3.9",  # TODO: change to 3.10 (3.9 for pythonanywhere.com)
    install_requires=[
        "python-dotenv",
        "pytelegrambotapi",
        "aiogram",
        "schedule",
        "pdfplumber",
        "jmespath",
    ],
)
