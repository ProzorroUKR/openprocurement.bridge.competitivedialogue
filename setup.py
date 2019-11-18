from setuptools import setup, find_packages
import os

version = '1.2.0dp'

requires = [
    'setuptools',
    'PyYAML',
    'gevent',
    'restkit',
    'openprocurement_client==1.0b2',
]

test_requires = requires + [
    'webtest',
    'python-coveralls',
    'mock',
]

docs_requires = requires + [
    'sphinxcontrib-httpdomain',
]

entry_points = {
    'console_scripts': [
        'competitive_dialogue_data_bridge = openprocurement.bridge.competitivedialogue.databridge:main'
    ]
}

here = os.path.abspath(os.path.dirname(__file__))

setup(name='openprocurement.bridge.competitivedialogue',
      version=version,
      description="",
      long_description=open("README.rst").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        ],
      keywords="web services",
      author='Quintagroup, Ltd.',
      author_email='info@quintagroup.com',
      url='https://github.com/ProzorroUKR/openprocurement.bridge.competitivedialogue',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['openprocurement', 'openprocurement.bridge'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      extras_require={'test': test_requires, 'docs': docs_requires},
      test_suite="openprocurement.bridge.competitivedialogue.tests.main.suite",
      entry_points=entry_points)
