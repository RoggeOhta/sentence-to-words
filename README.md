# Sentence to Words

A Python CLI tool that tokenizes an English sentence and returns each word's position, original form, and lemma (root form).

Uses [NLTK](https://www.nltk.org/) for tokenization, POS tagging, and lemmatization via WordNet.

## Examples

### Simple — basic noun plurals

```
$ uv run python main.py I like dogs
Pos    Word                 Lemma
----------------------------------------------
1      I                    i
2      like                 like
3      dogs                 dog
```

### Medium — mixed verb tenses, adjective comparison, irregular plurals

```
$ uv run python main.py The children were happily playing with their bigger toys
Pos    Word                 Lemma
----------------------------------------------
1      The                  the
2      children             child
3      were                 be
4      happily              happily
5      playing              play
6      with                 with
7      their                their
8      bigger               big
9      toys                 toy
```

### Hard — subordinate clauses, punctuation, irregular plurals, passive voice

```
$ uv run python main.py "The geese, which had been swimming in the lakes, were frightened by the wolves' howling."
Pos    Word                 Lemma
----------------------------------------------
1      The                  the
2      geese                goose
3      ,                    ,
4      which                which
5      had                  have
6      been                 be
7      swimming             swim
8      in                   in
9      the                  the
10     lakes                lake
11     ,                    ,
12     were                 be
13     frightened           frighten
14     by                   by
15     the                  the
16     wolves               wolf
17     '                    '
18     howling              howling
19     .                    .
```

## Requirements

- Python >= 3.9
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
```

NLTK data (`punkt_tab`, `wordnet`, `averaged_perceptron_tagger_eng`) is downloaded automatically on first run.

## Usage

### CLI with arguments

```bash
uv run python main.py The cats were running quickly
```

### Pipe input

```bash
echo "She has been reading books" | uv run python main.py
```

### Interactive mode

```bash
uv run python main.py
Enter a sentence: The cats were running quickly
```

### As a library

```python
from main import sentence_to_words

results = sentence_to_words("The dogs were running")
# [
#     {"position": 1, "word": "The",     "lemma": "the"},
#     {"position": 2, "word": "dogs",    "lemma": "dog"},
#     {"position": 3, "word": "were",    "lemma": "be"},
#     {"position": 4, "word": "running", "lemma": "run"},
# ]
```

## Tests

```bash
uv run pytest test_main.py -v
```
