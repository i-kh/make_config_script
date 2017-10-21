from setuptools import setup
setup(
  name = 'config_maker',
  packages = ['config_maker'],
  scripts=['bin/make_config'],
  version = '0.0.1',
  description = 'config_maker creates a configuration file in INI format from environment variables',
  author = 'Irina Kharitonova',
  author_email = '',
  url = 'https://github.com/i-kh/make_config_script',
  download_url = 'https://github.com/i-kh/make_config_script/archive/master.zip',
  keywords = ['configs'],
  classifiers = [],
)
