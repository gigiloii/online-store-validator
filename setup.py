from setuptools import setup, find_packages

setup(
    name='online-store-validator',  # Replace with your own package name
    version='0.1.0',  # Initial version
    author='gigiloii',  # Your name or your organization
    author_email='your_email@example.com',  # Your email
    description='A package for validating online store inputs and outputs.',  # Short description of the package
    long_description=open('README.md').read(),  # Long description from README
    long_description_content_type='text/markdown',
    url='https://github.com/gigiloii/online-store-validator',  # Project URL
    packages=find_packages(),  # Automatically find packages in the directory
    classifiers=[  # List of classifiers
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Required Python version
)