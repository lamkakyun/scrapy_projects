# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.path.abspath('../misc'))

import mix_config
import db_helper
from db_model.Word import Word

# import db_helper
# from db_model.Word import Word



if __name__ == '__main__':
    db_session = db_helper.get_word_session()

    path = os.path.join(mix_config.MC_CURRENT_DIR, 'data', 'words_alpha.txt')
    
    with open(path, 'r') as f:
        count = 0
        for line in f:
            count += 1
            word = Word(word=line.strip())
            db_session.add(word)

            if count == 1000:
                db_session.commit()

            print(line)

    db_session.commit()
    db_session.close()

    print('main thread exit')