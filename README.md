<div id="top">
  <h1 align="center">FizzBuzz API</h1>
</div>

## Getting Started

### Installation

Clone the repo
   ```sh
   git clone https://github.com/flsworld/fizzbuzz-api.git && cd fizzbuzz-api
   ```

Use the following command to :
* build the container
```
docker build -t fizzbuzz_image .
```
* launch the container

```
docker run \
--name fizzbuzz 
-p 8000:8000 
-v $(pwd):/code 
fizzbuzz_image
```

If you need to run the container after having stopped it ```docker start fizzbuzz```

You should now be able to access the documentation at
http://localhost:8000/docs

If you want to open a shell in the container, run the following command
```
docker exec -it fizzbuzz bash
```


## Usage

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

### Launch tests suite
Open a shell in the web container and run all tests with 
```sh
    pytest
```
After having launched the tests, it is possible to see the coverage. To do so, 
open the following file `fizzbuzz/htmlcov/index.html` in your browser
