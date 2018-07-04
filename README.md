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

<table>
  <tr>
    <th rowspan=2>tokenizer</th>
    <th colspan=3>OpenCorpora</th>
    <th colspan=3>SynTagRus</th>
  </tr>
  <tr>
    <th>Precision</th>
    <th>Recall</th>
    <th>Execution Time (sec)</th>
    <th>Precision</th>
    <th>Recall</th>
    <th>Execution Time (sec)</th>
  </tr>
  <tbody>
    <tr>
      <td>nltk.sent_tokenize</td>
      <td>94.30</td>
      <td>86.06</td>
      <td>8.67</td>
      <td>98.15</td>
      <td>94.95</td>
      <td>5.07</td>
    </tr>
    <tr>
      <td>nltk.sent_tokenize(x, language='russian')</td>
      <td>95.53</td>
      <td>88.37</td>
      <td>8.54</td>
      <td>98.44</td>
      <td>95.45</td>
      <td>5.68</td>
    </tr>
    <tr>
      <td>bureaucratic-labs.segmentator.split</td>
      <td>97.16</td>
      <td>88.62</td>
      <td>359</td>
      <td>96.79</td>
      <td>92.55</td>
      <td>210</td>
    </tr>
    <tr>
      <td>ru_sent_tokenize</td>
      <td>98.73</td>
      <td>93.45</td>
      <td>4.92</td>
      <td>99.81</td>
      <td>98.59</td>
      <td>2.87</td>
    </tr>
  </tbody>
</table>

[Notebook](https://github.com/deepmipt/ru_sentence_tokenizer/blob/master/metrics/calculate.ipynb) shows how the table above was calculated 