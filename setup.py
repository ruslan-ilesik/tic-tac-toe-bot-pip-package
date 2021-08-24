from setuptools import setup, find_packages

setup(name='tic_tac_toe_bot',
      version='2.4',
      description='simple bot for tic tac toe',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
      ],
      keywords='tic_tac_toe bot api game_api ',
      url='https://github.com/ruslan-ilesik/tic-tac-toe-bot-pip-package',
      author='lesikr',
      license='MIT',
      packages=['tic_tac_toe'],
      install_requires=[],
      include_package_data=True,
      zip_safe=False,
      )
