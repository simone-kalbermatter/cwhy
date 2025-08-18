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

Export LLM endpoint to use local LLM:
```
export OPENAI_BASE_URL=http://localhost:8081/v1
```

# Run own examples
correct code:
```
cwhy --- python tests/python/code_fixer_example/correct.py 
```


Run own example code:
```
cwhy --llm meta-llama/Llama-3.2-3B-Instruct --- python tests/python/code_fixer_example/error_mutable_default_parameter.py 
```



# Useful flags
-  --show-prompt
-  --llm
-  
