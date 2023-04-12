import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="RealESRGAN",
    py_modules=["RealESRGAN"],
    version="1.0",
    description="",
    author="Sberbank AI, Xintao Wang",
    url='https://github.com/ai-forever/Real-ESRGAN',
    packages=find_packages(include=['RealESRGAN']),
    package_data={'': ['RealESRGAN_x4.pth']},
    include_package_data=True,
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ]
)
