import argparse
import sys

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download("punkt_tab", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("averaged_perceptron_tagger_eng", quiet=True)

WORDNET_POS_MAP = {
    "J": "a",  # adjective
    "V": "v",  # verb
    "N": "n",  # noun
    "R": "r",  # adverb
}


def get_wordnet_pos(treebank_tag: str) -> str:
    return WORDNET_POS_MAP.get(treebank_tag[0], "n")


def sentence_to_words(sentence: str) -> list[dict]:
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    lemmatizer = WordNetLemmatizer()

    results = []
    for i, (word, tag) in enumerate(tagged):
        wn_pos = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(word.lower(), pos=wn_pos)
        results.append({"position": i + 1, "word": word, "lemma": lemma})
    return results


def print_results(results: list[dict]):
    print(f"{'Pos':<6} {'Word':<20} {'Lemma':<20}")
    print("-" * 46)
    for item in results:
        print(f"{item['position']:<6} {item['word']:<20} {item['lemma']:<20}")


def main():
    parser = argparse.ArgumentParser(description="Tokenize a sentence and show each word's lemma.")
    parser.add_argument("sentence", nargs="*", help="the sentence to analyze")
    args = parser.parse_args()

    if args.sentence:
        sentence = " ".join(args.sentence)
    elif not sys.stdin.isatty():
        sentence = sys.stdin.read().strip()
    else:
        sentence = input("Enter a sentence: ")

    if not sentence:
        return

    print_results(sentence_to_words(sentence))


if __name__ == "__main__":
    main()
