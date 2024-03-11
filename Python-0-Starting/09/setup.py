from setuptools import setup, find_packages

setup(
	name='ft_package',
	version='0.0.1',
	summary='test de mise en package',
	License= 'MIT',
	author='nwyseur',
	author_email='nwyseur@student.42.fr',
	packages=find_packages(),
	Installer='pip',
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)