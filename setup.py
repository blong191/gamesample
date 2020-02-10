import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="sample-game"
    version="0.0.1",
    author="Ben Long",
    author_email="bmlong@steavenscollege.edu",
    url="https://github.com/yourusername/yourproject",
    description="what does yourproject do?",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
