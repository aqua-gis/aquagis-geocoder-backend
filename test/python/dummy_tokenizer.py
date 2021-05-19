"""
Tokenizer for testing.
"""

def create(dsn, data_dir):
    """ Create a new instance of the tokenizer provided by this module.
    """
    return DummyTokenizer(dsn, data_dir)

class DummyTokenizer:

    def __init__(self, dsn, data_dir):
        self.dsn = dsn
        self.data_dir = data_dir
        self.init_state = None
        self.analyser_cache = {}


    def init_new_db(self, *args, **kwargs):
        assert self.init_state is None
        self.init_state = "new"


    def init_from_project(self):
        assert self.init_state is None
        self.init_state = "loaded"


    @staticmethod
    def finalize_import(_):
        pass


    def name_analyzer(self):
        return DummyNameAnalyzer(self.analyser_cache)


class DummyNameAnalyzer:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()


    def __init__(self, cache):
        self.analyser_cache = cache
        cache['countries'] = []


    def close(self):
        pass

    @staticmethod
    def normalize_postcode(postcode):
        return postcode

    @staticmethod
    def update_postcodes_from_db():
        pass

    def update_special_phrases(self, phrases, should_replace):
        self.analyser_cache['special_phrases'] = phrases

    def add_country_names(self, code, names):
        self.analyser_cache['countries'].append((code, names))

    @staticmethod
    def process_place(place):
        return {}
