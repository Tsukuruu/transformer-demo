# Importing library of warnings
import warnings

import os
import sys

script_dir = os.path.dirname(__file__)
transformer_dir = os.path.join(script_dir, '..')
sys.path.append(transformer_dir)
import transformer

if __name__ == '__main__':
    warnings.filterwarnings('ignore') # Filtering warnings
    config = transformer.get_config(lang_src='en', lang_tgt='pl', seg_len=560) # Retrieving config settings
    transformer.train_model(config) # Training model with the config arguments