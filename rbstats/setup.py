from setuptools import setup, find_packages

PACKAGE="RB-Stats"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""RB-Stats extension for Review Board""",
    author="Mike Conley",
    packages=["rbstats"],
    entry_points={
        'reviewboard.extensions':
        '%s = rbstats.extension:RBStatsExtension' % PACKAGE,
    },
    package_data={
        'rbstats': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/rbstats/*.html',
            'templates/rbstats/*.txt',
        ],
    },
    install_requires=['RB-Defects>=0.1']
)


