# fizzbuzz-api

``docker build -t fizzbuzz_image .``

```
docker run \
--name fizzbuzz 
-p 8000:8000 
-v $(pwd):/code 
fizzbuzz_image
```

### Install pre-commit
In order to remain focus on logic during development while not wasting time with trivial style nitpicks, 
pre-commit - a useful tool upon which it is able to install hooks - has been used. In this project 
* black was used to format the code 
* flake8 was used to check compliance with PEP8

You can run pre-commit either in a virtualenv or in the docker container.

Install pre-commit with
```sh
    pre-commit install
```
Run pre-commit on all files
```sh
    pre-commit run --all-files
```
Uninstall pre-commit
```sh
    pre-commit uninstall
```
