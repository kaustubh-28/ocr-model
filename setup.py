from setuptools import setup


with open('requirements.txt') as f:
    packages = f.read().splitlines()

setup(
    name='ocrmodel',
    version='0.1.0',
    description='Optical Character Recognition model based on CRNN and CTC loss',
    author='Kaustubh Srivastava',
    author_email='kaustubh282.s@gmail.com',
    url='https://github.com/kaustubh-28/ocr-model',
    packages=['ocr'],
    install_requires=packages
)
