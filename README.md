# ru_sentence_tokenizer
A simple and fast rule-based sentence segmentation. Tested on OpenCorpora and SynTagRus datasets.

# Installation
```
python3 -m pip install --index-url https://test.pypi.org/simple/ ru_sent_tokenize
```

# Running
```python
>>> from ru_sent_tokenize import ru_sent_tokenize
>>> ru_sent_tokenize('Эта шоколадка за 400р. ничего из себя не представляла. Артём решил больше не ходить в этот магазин')
['Эта шоколадка за 400р. ничего из себя не представляла.', 'Артём решил больше не ходить в этот магазин']```