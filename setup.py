"""The setup script."""

from setuptools import setup, find_packages

requirements = [
    'numpy>=1.16.0',
]

setup(
    name='src',
    version='0.1.0',
    description="Test actions",
    author="Haavard Kvamme",
    author_email='haavard.kvamme@gmail.com',
    url='https://github.com/havakv/test_actions',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    license="BSD-2 license",
    zip_safe=False,
    keywords='actions',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.6'
)