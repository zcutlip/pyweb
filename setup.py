from setuptools import setup

setup(name='python-webserver',
      version='0.2',
      description='A basic localhost web server to use in your home directory.',
      url="TBD",
      packages=['pyweb'],
      entry_points={
          'console_scripts': ['pyweb=pyweb.command_line:main',
                              'pyweb-add-content=pyweb.installer_cmd:main']},
      python_requires='>=3.7',
      )
