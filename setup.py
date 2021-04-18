import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setuptools.setup(
    name="valeria", 
    version="1.0",
    author="dylan14567",
    author_email="",
    description="valeria es un chatbot y es tu asistente virtual",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dylan14567/valeria",
    scripts = ['valeria'],
    project_urls={
        "Bug Tracker": "https://github.com/dylan14567/valeria/issues",
    },
    install_requires=[
        "wheel",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="server",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
)
