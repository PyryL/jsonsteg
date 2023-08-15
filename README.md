# JSON steganography

_Write payload into JSON without modifying it_	

![Build status](https://github.com/PyryL/jsonsteg/actions/workflows/main.yml/badge.svg)
![Branch coverage](https://codecov.io/gh/PyryL/jsonsteg/branch/main/graph/badge.svg?token=YT08CLBMMK)


## Usage

Use command line interface via `jsonsteg` command.

### Writing

Write payload `mysecret` to JSON found in file `data.json`:

```
jsonsteg write --input mysecret data.json
```

Write the contents of file `message.txt` as a payload to JSON of file `data.json`:

```
jsonsteg write --input-file message.txt data.json
```

Instead of modifying `data.json` file, you can output the altered JSON to `output.json` file:

```
jsonsteg write --input mysecret --output output.json data.json
```

### Reading

Write the payload of JSON in file `data.json` and print it to console:

```
jsonsteg read data.json
```

Instead of printing, the output can also be saved to file `output.txt`:

```
jsonsteg read --output output.txt data.json
```

### Help

Learn more about possible options with these commands:

```
jsonsteg --help
jsonsteg read --help
jsonsteg write --help
```


## Development

After cloning the git repository, install development dependencies
by running the following command in project root:

```
poetry install
```

Run unit tests with

```
poetry run invoke test
```

Run coverage test with

```
poetry run invoke coverage
```

and create HTML coverage report with

```
poetry run invoke coverage-report
```


## How is it done?

Read more about the mechanism [here](docs/mechanism.md).
