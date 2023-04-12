import setuptools

setuptools.setup(
    include_package_data = True,
    name = 'setuptoos',
    version = '0.0.1',
    description = 'calc example for Pypi',
    author = 'taegyeomha',
    author_email = 'htk00524@gmail.com',
    url = 'https://github.com/choigochoigo/setuptoos',
    download_url = 'https://github.com/choigochoigo/setuptoos/archive/refs/tags/v.0.0.1.zip',
    install_requires = ['pytest'],
    packages = ['setuptoos'],
    long_description = 'oss-dev calculator example',
    long_description_content_type = 'text/markdown',
    classifiers = [
        "Programming Language :: Python :: 3",
        "Operatig System :: OS Independent"
    ]
)
