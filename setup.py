from importlib.machinery import SourceFileLoader

from setuptools import find_packages, setup

version = SourceFileLoader('version', 'envioclick/version.py').load_module()

test_requires = [
    'pytest',
    'pytest-vcr',
    'pycodestyle',
    'pytest-cov',
    'black',
    'isort[pipfile]',
    'flake8',
    'mypy',
]

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='envioclick',
    version=version.__version__,  # type: ignore
    author='Cuenca',
    author_email='dev@cuenca.com',
    description='Client library for api.envioclickpro.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cuenca-mx/envioclick-python',
    packages=find_packages(),
    include_package_data=True,
    package_data=dict(mati=['py.typed']),
    python_requires='>=3.7',
    install_requires=[
        'dataclasses>=0.6;python_version<"3.7"',
        'requests>=2.22.0,<3.0.0',
    ],
    setup_requires=['pytest-runner'],
    tests_require=test_requires,
    extras_require=dict(test=test_requires),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
