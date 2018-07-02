# ru_sentence_tokenizer
A simple and fast rule-based sentence segmentation. Tested on OpenCorpora and SynTagRus datasets.

# Installation
```
python3 -m pip install --index-url https://test.pypi.org/simple/ ru_sent_tokenize
```

# Running
```ipython
>>> from ru_sent_tokenize import ru_sent_tokenize
>>> ru_sent_tokenize('Эта шоколадка за 400р. ничего из себя не представляла. Артём решил больше не ходить в этот магазин')
['Эта шоколадка за 400р. ничего из себя не представляла.', 'Артём решил больше не ходить в этот магазин']
```

# Metrics

The tokenizer has been tested on OpenCorpora and SynTagRus. There are two important metrics. 

Precision. First one is we took single sentences from the datasets and measured how many times tokenizer didn't split them.  

Recall. Second metric is we took two consecutive sentences from the datasets and joined each pair with a space characted. We measured how many times tokenizer correctly splitted a long sentence into two.

|tokenizer|Precision (OpenCorpora)|Recall (OpenCorpora)|Execution Time (OpenCorpora)|Precision (SynTagRus)| Recall (SynTagRus)|Execution Time (OpenCorpora)|
|---|---|---|---|---|---|---|
|nltk.sent_tokenize|94.30|86.06|8.67|98.15|94.95|5.07|
|nltk.sent_tokenize(x, language='russian')| 95.53 | 88.37 | 8.54 | 98.44 | 95.45 | 5.68 |
|bureaucratic-labs.segmentator.split| 97.16 | 88.62 | 359 | (in process) | (in process)|(in process)|
|ru_sent_tokenize| 98.83 | 93.19 | 4.87 | 99.82 | 96.56 | 2.81 |





