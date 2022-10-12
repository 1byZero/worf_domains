from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in worf_domains/__init__.py
from worf_domains import __version__ as version

setup(
	name="worf_domains",
	version=version,
	description="Domain name buy,sell and availability tool.",
	author="Amit Kumar",
	author_email="amitkp66@live.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
