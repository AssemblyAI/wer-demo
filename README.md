## Running demo

```
python score.py
```

## Normalizing to other languages

For now, you'll need to change the integer expansion (7 -> seven) to expand integers in your local language by changing [this line](https://github.com/AssemblyAI/wer-demo/blob/master/normalize.py#L10). For example, for Russian you'd change the line to:

```
expanded = num2words.num2words(int(token), lang='ru')
```

The full list of languages supported can be [found here](https://github.com/savoirfairelinux/num2words#usage).
