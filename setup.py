from setuptools import setup

setup(name='snel',
      version='0.0.1',
      author='Andrew Udvare',
      author_email='audvare@gmail.com',
      url='https://github.com/Tatsh/snel',
      python_requires='>=3.5',
      py_modules=['snel'],
      description='Unofficial client to Google Lens.',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3 :: Only',
          'Topic :: Utilities',
      ],
            entry_points={
                      'console_scripts': [
                                    'snel = snel:main'
                                    ]},
      install_requires=['requests>=2.26.0'])
