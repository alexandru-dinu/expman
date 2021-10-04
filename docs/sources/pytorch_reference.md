Refer to [main/pytorch_reference](https://github.com/opskrift/opskrift/tree/main/pytorch_reference) for code examples.

### PyTorch data model
- several data sources can be made into a PyTorch `Dataset` object
- an item is (possibly transformed and) prepared in `__getitem__` method
- a `collate` function will construct a batch
- finally, `DataLoader` wraps over a `Dataset` and emits batches of data
