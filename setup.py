from setuptools import setup

setup(
        name='create_brython_app',
        version='0.0.1',
        packages=['create_brython_app'],
        package_dir={'create_brython_app': 'create_brython_app'},
        package_data={'create_brython_app': ['*'],},
        url='',
        # scripts=['bin/create_brython_app.py'],
        entry_points={
                'console_scripts': ['create_brython_app=create_brython_app:main'],
        },
        license='',
        author='Kelly',
        author_email='',
        description=''
)
