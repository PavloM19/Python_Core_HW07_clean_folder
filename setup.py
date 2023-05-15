from setuptools import setup, find_namespace_packages

setup(
    name='package_sorting',
    version='0.2.1',
    description='Package for sorting files by category',
    author='Maksaiev Pavlo',
    author_email='mpa_dn@ua.fm',
    license='MIT',
    classifiers=['Programming Language :: Python :: 3'],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)