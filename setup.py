import pathlib  
import setuptools 
  
requires = [  # Declare required packages for using this plugin
  "flake8 > 3.0.0",  
  "pytest",  
]  
  
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
  
setuptools.setup(
  name="flake8_alembic",  # Define module name
  license="MIT",  
  version="0.1.0",  
  description=(  
    "A plugin to check Alembic migrations."  
  ),  
  author="Igor Nikolaev",  
  author_email="igor.nikolaev@nikisoft.ru",  
  classifiers=[  
    "Programming Language :: Python :: 3.10",  
    "Framework :: Flake8",  
  ],  
  py_modules=[  
    "flake8_alembic",  
    "visitor",
  ],  
  install_requires=requires,  
  entry_points={  # The entry poing for running Flake8 plugin
    "flake8.extension": [
	    "T100 = flake8_alembic:Plugin"
    ],  
  },  
)
