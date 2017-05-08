# Prediction API Client

This is a command line tool which is using the [Prediction API](https://github.com/alex-min/prediction-api)


Usage:
```shell
$ ./prediction_client.py <input file> <api host>
```

One example [input.txt](input.txt) file is available in the repository.
The input file should have each teams separated with an ampersand.

- Returns T if the probability is greater than 50%
- Returns F otherwise

Example output: ```TFTFFFT```


## Project setup

This project is using python3, your system must have python3 installed, to install the necessary packages execute pip3

```
pip3 -r requirements.txt
```


