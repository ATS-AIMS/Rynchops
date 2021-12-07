import re
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    M2M100ForConditionalGeneration,
    M2M100Tokenizer,
)

SPLIT_MODES = {"Sentence": ". ", "Newline": "\n", "Paragraph": "\n\n", "None": None}


class mT5:
    def __init__(self):
        """Create the mT5 model for summarization
        """
        source = "csebuetnlp/mT5_multilingual_XLSum"
        self.tokenizer = AutoTokenizer.from_pretrained(source)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(source)

    @staticmethod
    def whitespace_handler(k):
        """whitespace correction method suggested by mT5 model code.
        k (str): text to correct.
        """
        return re.sub("\s+", " ", re.sub("\n+", " ", k.strip()))

    def run(self, text):
        """Summarize model input.

        Args:
            text (str): Text to summarize

        Returns:
            str: Summarized text.
        """
        input_ids = self.tokenizer(
            [self.whitespace_handler(text)],
            return_tensors="pt",
            padding="max_length",
            truncation=True,
            max_length=512,
        )["input_ids"]

        output_ids = self.model.generate(
            input_ids=input_ids, max_length=84, no_repeat_ngram_size=2, num_beams=4
        )[0]

        summary = self.tokenizer.decode(
            output_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False
        )

        return summary


class M2M100:
    def __init__(self, src_lang="ar"):
        """Create M2M100 Language translation model.
        
        Args:
            src_lang (str, optional): Language to translate from. Defaults to "ar".
        """
        source = "facebook/m2m100_418M"
        self.model = M2M100ForConditionalGeneration.from_pretrained(source)
        self.tokenizer = M2M100Tokenizer.from_pretrained(
            source, src_lang=src_lang, tgt_lang="en"
        )

    def run(self, text):
        """Translate text to english.

        Args:
            text (str): Text to translate

        Returns:
            str: Translated text.
        """
        model_inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model.generate(
            **model_inputs, forced_bos_token_id=self.tokenizer.get_lang_id("en")
        )
        with self.tokenizer.as_target_tokenizer():
            translated = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translated


class DemoModel:
    def __init__(self, src_lang="ar"):
        """Creates a stacked mT5/m2m100 model.

        Args:
            src_lang (str, optional): Language of the text to translate. Defaults to "ar".
        """
        self.mt5 = mT5()
        self.m2m100 = M2M100(src_lang=src_lang)

    def split_text(self, text, split_mode="Paragraph"):
        """Split text according to a particular mode.

        Args:
            text (str): Text to split
            split_mode (str, optional): Mode of splitting, one of SPLIT_MODES. Defaults to "Paragraph".

        Returns:
            list: list of strings.
        """
        assert (
            split_mode in SPLIT_MODES
        ), f"split_mode must be one of {list(SPLIT_MODES.keys())}."

        if split_mode == "None":
            return [text]

        elif split_mode == "Sentence":
            return [tu + "." for tu in text.split(SPLIT_MODES[split_mode])]

        else:
            return text.split(SPLIT_MODES[split_mode])

    def marshall(self, text, method, explain_error=False):
        """Marshalling code for a classmethod run on a string or list wit error handling.

        Args:
            text (str or list): Text to run through method.
            method (method): method to run over text.
            explain_error (bool, optional): Instead of no output, insert error into list. Defaults to False.

        Returns:
            list: list of text post-processing.
        """
        outputs = []

        if isinstance(text, str):
            text = [text]

        for text_unit in text:
            try:
                outputs.append(method(text_unit))

            except Exception as e:
                if explain_error:
                    outputs.append(str(e))

        return outputs

    def summarize(self, text):
        """Use mt5 to summarize

        Args:
            text (str or list of str): text to summarize

        Returns:
            list: summarized text
        """
        return self.marshall(text, self.mt5.run, explain_error=False)

    def translate(self, text):
        """Use m2m100 to translate

        Args:
            text (str or list of str): text to translate

        Returns:
            list: translated text
        """
        return self.marshall(text, self.m2m100.run, explain_error=False)

    def run(self, text, split_mode="Paragraph", do_translate=True):
        """Summarize and translate text.
        

        Args:
            text (str or list of str): Text to summatrans
            split_mode (str, optional): Mode of splitting text for summarization, one of SPLIT_MODES. Defaults to "Paragraph".
            do_translate (bool, optional): Translate text to English? Defaults to True.

        Returns:
            list: Summatransed text
        """
        text = self.split_text(text, split_mode)
        text = self.summarize(text)

        if do_translate:
            text = self.translate(text)

        return text


XLSUM_LANGS = [
    ["English", 301444],
    ["Ukrainian", 57952],
    ["Russian", 52712],
    ["Hindi", 51715],
    ["Spanish", 44413],
    ["Indonesian", 44170],
    ["Urdu", 40714],
    ["Arabic", 40327],
    ["Chinese", 39810],
    ["Turkish", 29510],
    ["Persian", 25783],
    ["Portuguese", 23521],
    ["Vietnamese", 23468],
    ["Tamil", 17846],
    ["Pashto", 15274],
    ["Welsh", 11596],
    ["Telugu", 11308],
    ["Marathi", 11164],
    ["Swahili", 10005],
    ["Pidgina", 9715],
    ["Gujarati", 9665],
    ["French", 9100],
    ["Punjabi", 8678],
    ["Bengali", 8226],
    ["Japanese", 7585],
    ["Azerbaijani", 7332],
    ["Serbian (Cyrillic)", 7317],
    ["Serbian (Latin)", 7263],
    ["Thai", 6928],
    ["Yoruba", 6316],
    ["Hausa", 6313],
    ["Oromo", 5738],
    ["Somali", 5636],
    ["Kirundi", 5558],
    ["Amharic", 5461],
    ["Nepali", 5286],
    ["Burmese", 5002],
    ["Uzbek", 4944],
    ["Tigrinya", 4827],
    ["Igbo", 4559],
    ["Korean", 4281],
    ["Sinhala", 3414],
    ["Kyrgyz", 2315],
    ["Scottish (Gaelic)", 1101],
]
