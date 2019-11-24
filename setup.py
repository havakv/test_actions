"""The setup script."""

from setuptools import setup, find_packages

requirements = [
    # 'feather-format>=0.4.0',
    'h5py>=2.9.0',
    'numba>=0.44',
    'scikit-learn>=0.21.2',
    'requests>=2.22.0',
    'torchtuples>=0.1.2',
]

setup(
    name='actions_upload_testing',
    version='0.1.1',
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
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.6'
)
