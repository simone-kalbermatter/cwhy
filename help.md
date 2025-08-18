# Set up venv for dev
activate venv for dev:
```
source .venv/bin/activate
```

deactivate venv:
```
deactivate
```

# Run examples
Run python example:
```
cwhy --- python tests/python/concatenate-str-to-int.py 
```

Run c++ example:
```
cwhy --- g++ tests/c++/missing-hash.cpp 
```

# Run own examples
correct code:
```
cwhy --- python tests/python/code_fixer_example/correct.py 
```


Run c++ example:
```
cwhy --- python tests/python/code_fixer_example/error_mutable_default_parameter.py 
```