from setuptools import setup, find_packages

setup(
    name='recalbox-manifesto',
    version=__import__('recalbox_manifesto').__version__,
    description=__import__('recalbox_manifesto').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='sveetch@gmail.com',
    url='https://github.com/sveetch/recalbox-manifesto',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Jinja2 >= 2.6',
        'click==4.0',
        'colorama==0.3.2',
    ],
    entry_points={
        'console_scripts': [
            'recalbox-manifesto = recalbox_manifesto.builder:main',
        ]
    },
    include_package_data=True,
    zip_safe=False
)