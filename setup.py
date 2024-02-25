from setuptools import setup,find_packages

setup(
    name='data_ingestion',
    version='0.1',
    packages= find_packages(),
    install_requires=['sqlalchemy','pandas'],
    author="Taha Rochdi",
    author_email='rochditaha1998@gmail.com',
    description="a package for data ingestion tasks",
)