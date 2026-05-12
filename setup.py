from setuptools import setup

APP = ['launcher.py']

OPTIONS = {
    'argv_emulation': True,
    'packages': ['flask', 'schedule', 'bs4', 'requests', 'stem'],
    'resources': ['onion_sites.txt', 'data', 'screenshots']
}

setup(
    app=APP,
    name='DarkLeakScanner',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
