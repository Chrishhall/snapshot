from setuptools import setup

setup(
    name="snapshot",
    version="0.1",
    author="Chris Hall",
    author_email='chrishhall@hotmail.com',
    description='Tool to manage Snapshots on AWS',
    license='GPLv3+',
    packages=['shotty'],
    url="https://github.com/Chrishhall/snapshot",
    install_requires=['click','boto3'],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',

)
