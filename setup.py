from setuptools import setup

setup(
	name='lastfm',
	version="0.0.1",
	description="a library for easy access to lastfm data for discord bots",
	long_description="...",
	long_description_content_type="text/markdown",
	author="cop-discord",
	author_email="z@rival.rocks",
	url="https://github.com/cop-discord/lastfm",
	packages=['lastfm'],
	install_requires=['aiohttp','discord','orjson'],
	package_data=[['*']],
	include_package_data=True,
	python_requires=">=3.6"
)
