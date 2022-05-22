# fizzbuzz-api

``docker build -t fizzbuzz_image .``

```
docker run \
--name fizzbuzz 
-p 8000:8000 
-v $(pwd):/code 
fizzbuzz_image
```
