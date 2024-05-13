import transformer

import warnings

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    warnings.filterwarnings('ignore')
    config = transformer.get_config()
    transformer.translate(config)