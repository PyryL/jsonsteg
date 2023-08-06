# Mechanism

## Dictionary

In JSON the order of keys in a dictionary does not matter.
This can be used to write additional data into JSON structure without
altering the actual content of it.

1.
Payload bytes are converted to bits, i.e. ones and zeros.

2.
The keys of a dictionary are sorted into ascending alphabetical order.

3.
An output dictionary is constructed item-by-item by picking items from the original dictionary using the following rules:

* if the payload bit is one, key is picked from the _beginning_ of unused keys.
* if the payload bit is one, key is picked from the _end_ of unused keys.

When each payload bit has been written,
rest of the unused keys can be added in an arbitrary order.

---

Reading the payload from the output dictionary can be done by taking the steps in reversed order.
