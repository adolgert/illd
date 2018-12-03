from setuptools import setup, PEP420PackageFinder

setup(
    name="illd",
    version="0.0.1",
    packages=PEP420PackageFinder.find("src"),
    package_data={},
    package_dir={"": "src"},
    extras_require={
        "testing": ["hypothesis", "pytest", "pytest-mock"],
        "documentation": ["sphinx", "sphinx_rtd_theme", "sphinx-autobuild", "sphinxcontrib-napoleon"],
        "ihme_databases": ["db_tools", "db_queries", "save_results", "hierarchies"],
    },
    entry_points={
        "console_scripts": [
            ["illserver=illd.app:entry"],
        ]
    },
    scripts=[],
    zip_safe=False,
    classifiers=[
        "Intendend Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Statistics",
    ],
)
