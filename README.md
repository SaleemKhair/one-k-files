# one-k-files
This repository for tech community case studies only.


### Running
---
#### Linux

1. `python3 -m venv .venv`
2. `source ./.venv/bin/activate`
3. `python -m pip install -r requirements.txt`
4. `pyhon setup.py install`

> use the console entrypoint in `.venv/bin/one-k-files`.
```
$ ./venv/bin/one-k-files
```

The output directories are prefexed with `exported`.

#### Notes:

There are 2 aproaches to solve the problem in the project:
1. Datasource/Servie approach: Store here has the role of a Dao or a Repository that has direct access to the FileSystem, the Service here is a traditional service design that is responsible for talking to the Data Access Layer.

2. Producer/Consumer approach: Producer here is going to scan the directory and provide the input, the consumer is responsible for writing the data

A Stategy for the output directory is shared between both uproaches.
