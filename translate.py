import transformer

import os

import warnings

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    config = transformer.get_config(lang_src=os.getenv('lang_src'), 
                                    lang_tgt=os.getenv('lang_tgt'), 
                                    seq_len=int(os.getenv('seq_len')), 
                                    preload=os.getenv('preload'), 
                                    num_epochs=int(os.getenv('num_epochs')), 
                                    train_preload=os.getenv('train_preload')) # Retrieving config settings
    transformer.translate(config)