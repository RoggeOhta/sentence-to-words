from main import sentence_to_words, get_wordnet_pos


class TestGetWordnetPos:
    def test_noun(self):
        assert get_wordnet_pos("NN") == "n"

    def test_verb(self):
        assert get_wordnet_pos("VBD") == "v"

    def test_adjective(self):
        assert get_wordnet_pos("JJ") == "a"

    def test_adverb(self):
        assert get_wordnet_pos("RB") == "r"

    def test_unknown_defaults_to_noun(self):
        assert get_wordnet_pos("DT") == "n"


class TestSentenceToWords:
    def test_basic_sentence(self):
        results = sentence_to_words("The cat sat on the mat")
        words = [r["word"] for r in results]
        assert words == ["The", "cat", "sat", "on", "the", "mat"]

    def test_positions_start_at_one(self):
        results = sentence_to_words("Hello world")
        assert results[0]["position"] == 1
        assert results[1]["position"] == 2

    def test_verb_lemmatization(self):
        results = sentence_to_words("The dogs were running")
        lemmas = {r["word"]: r["lemma"] for r in results}
        assert lemmas["were"] == "be"
        assert lemmas["running"] == "run"

    def test_noun_lemmatization(self):
        results = sentence_to_words("The cats chased mice")
        lemmas = {r["word"]: r["lemma"] for r in results}
        assert lemmas["cats"] == "cat"
        assert lemmas["mice"] == "mouse"

    def test_adjective_lemmatization(self):
        results = sentence_to_words("The bigger house is better")
        lemmas = {r["word"]: r["lemma"] for r in results}
        assert lemmas["bigger"] == "big"
        assert lemmas["better"] == "well"

    def test_empty_string(self):
        results = sentence_to_words("")
        assert results == []

    def test_single_word(self):
        results = sentence_to_words("Running")
        assert len(results) == 1
        assert results[0]["position"] == 1
        assert results[0]["word"] == "Running"

    def test_punctuation_included(self):
        results = sentence_to_words("Hello, world!")
        words = [r["word"] for r in results]
        assert "," in words
        assert "!" in words

    def test_result_structure(self):
        results = sentence_to_words("test")
        assert "position" in results[0]
        assert "word" in results[0]
        assert "lemma" in results[0]
