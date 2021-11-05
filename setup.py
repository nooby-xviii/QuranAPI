import setuptools

with open("README.md") as f:
  README = f.read()
  
setuptools.setup(
  name="QuranAPI",
  version="1.5",
  description="Get Quran verses specifically or even randomly! Alongside the Quran we also provide prayer times thanks to Aladhan!",
  long_description=README,
  long_description_content_type="text/markdown",
  url = "https://github.com/zacharierrr/QuranAPI/",
  author="nooby xviii",
  author_email="xviii2008@gmail.com",
  packages=setuptools.find_packages(),
  include_package_data=True,
  install_requires=["aiohttp"],
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires=">=3.7"
  )
  
