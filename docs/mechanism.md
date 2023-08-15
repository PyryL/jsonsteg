# Mechanism

## Dictionary

The order of keys in a JSON dictionary does not matter.
This can be used to write additional data into JSON structure without
altering the actual content of it.

### Example

1.
Let's say that we want to store byte `01001100` as a payload into the following JSON dictionary:

```json
{
    "date": "2023-08-15T05:50:02Z",
    "type": "sunny",
    "temperature": 19.7,
    "dewpoint": 15.2,
    "precipitation": 0,
    "pressure": 1021,
    "windspeed": 3,
    "gustspeed": 7,
    "winddirection": 220
}
```

2.
Dictionary keys are sorted into alphabetical order:

```
date, dewpoint, gustspeed, precipitation, pressure, temperature, type, winddirection, windspeed
```

3.
Then the output is constructed by repeating the following operation for each bit of payload:

If the payload bit is zero, a key is picked from the _beginning_ of the list of ordred keys.
Otherwise a key from the _end_ of the key list is chosen.

* In our payload, `01001100`, the first bit is zero. Therefore the _first_ key in the list, `date`, is chosen.
* Second bit of our payload is one, and therefore the _last_ item of the list, `windspeed`, is picked.
* Third bit is zero again, but the first list item, `date`, was already used. That's why we choose the _first unused_ key, `dewpoint`.

At this point, our output dictionary looks like this:

```json
{
    "date": "2023-08-15T05:50:02Z",
    "windspeed": 3,
    "dewpoint": 15.2
}
```

The same process is repeated to every payload bit.
After that, rest of the unused keys can be added in arbitrary order.

In this case, the final output would be:

```json
{
    "date": "2023-08-15T05:50:02Z",
    "windspeed": 3,
    "dewpoint": 15.2,
    "gustspeed": 7,
    "winddirection": 220,
    "type": "sunny",
    "precipitation": 0,
    "pressure": 1021,
    "temperature": 19.7
}
```

### Limitations

In order to be able to read the payload, there must always be at least one spare key left unused in the dictionary.
Therefore payload of n bytes requires minimum of 8n+1 keys.


## Array of dictionaries

When we have an array whose each item is a dictionary,
we can split the payload into smaller chunks and write one chunk into one dictionary.
The dictionaries do not even need to be homogeneous and the chunk size may vary.
