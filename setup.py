from setuptools import setup

setup(
    name='auto_pete',
    packages=['app', 'auto_pete'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask_wtf', 'wtforms', 'email_validator'
    ],
)