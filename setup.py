import setuptools

with open("README.md", "r", encoding='utf8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="rusenttokenize",
    version="0.0.5",
    author="Marat Zaynutdinov",
    author_email="tsundokum@gmail.com",
    description="Rule-based sentence tokenizer for Russian language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepmipt/ru_sentence_tokenizer",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    test_suite="tests",
)
