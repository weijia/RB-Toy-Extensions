from setuptools import setup, find_packages

PACKAGE="RB-ReviewLines"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""Review lines extension for Review Board""",
    author="Wang Weijia",
    packages=["rbreviewlines"],
    entry_points={
        'reviewboard.extensions':
        '%s = rbreviewlines.extension:RBReviewLinesExtension' % PACKAGE,
    },
    package_data={
        'rbreviewlines': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/extd/*.html',
            'templates/extd/*.txt',
        ],
    },
    install_requires=['RB-Stats>=0.1']
)


