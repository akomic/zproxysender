from distutils.core import setup

setup(name='ZabbixProxySender',
      version='0.0.1',
      description='Simple Zabbix Proxy Sender',
      long_description=open('README.md', 'r').read() + '\n\n' + open(
          'CHANGELOG.md', 'r').read(),
      author='Alen Komic',
      author_email='akomic@gmail.com',
      url='https://github.com/akomic/zproxysender',
      packages=['ZabbixProxySender'],
      keywords='zabbix proxy sender monitoring',
      license='Apache Software License',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Networking :: Monitoring',
          'Topic :: System :: Systems Administration'
      ]
      )
