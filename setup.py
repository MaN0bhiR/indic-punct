from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="indic-punct",
    version='2.0.7',
    description='Punctuation and inverse text normalization for Indic languages and English',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Open-Speech-EkStep/indic-punct',
    keywords='nlp, punctuation, Indic languages, deep learning',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=[
        'wget',
        'certifi==2020.12.5',
        'inflect',
        
        'pandas',
        'python-dateutil',
        'pytz',
        'six',
        'tqdm',
        'torch',
        'scipy',
        'sentencepiece',
        'tokenizers',
        'torchvision==0.16.0',
        'transformers',
        'indic-nlp-library==0.81',
        'numpy'
    ],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Text Processing :: Linguistic',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python ',
    ],
    include_package_data=True,
)
