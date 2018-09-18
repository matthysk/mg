from setuptools import setup

setup(
    name='django-mg',
    version='0.0.2',
    author = "Matthys Kroon",
    author_email = "matthysk@gmail.com",
    description='Django app for keeping track of things in the garden.',
    license = "gpl3",
    packages=['mg'],
    include_package_data=True,
    install_requires=[
        "django<=1.12",
    ]
)
