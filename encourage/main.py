import pyttsx3
import random
import stat
import copy
import optparse
from encourage.cnf import *



usage = '''
Usage : use default cnf path {} to set ecourage words

eg:
    nickname  linda
    repeat    tomorrow will be better
    you are a good girl
    have a nice day

if you above  words to this file ,'linda, tomorrow will be better 'will be speaked out by encourage speaker.\n
if you drop repeat keyword before line ,then one random line will be speaked out.

if no content in cnf file , default nickname and default encurage words will be used.
'''.format(CNF_PATH)



def main():

    parser = optparse.OptionParser(usage=usage)
    options , args = parser.parse_args()
    if args:
        parser.print_usage()

    # init a speaker engine
    engine = pyttsx3.init()
    nick_name = copy.copy(NICK_NAME)

    # make default cnf dir and cnf
    if not os.path.exists(CNF_PATH):
        if not os.path.exists(CNF_DIR):
            os.makedirs(CNF_DIR)

        open(CNF_DIR, 'w').close()
        os.chmod(CNF_PATH, stat.S_IRUSR | stat.S_IWUSR)

    f = open(CNF_PATH,"r")

    beautiful_words = []

    for line in f.readlines():
        if 'nickname' in line:
            nick_name = line.strip().replace("nickname","")
            continue
        if 'repeat' in line:
            beautiful_words = [line.strip().replace("repeat","")]
            break
        beautiful_words.append(line.strip())

    if beautiful_words:
        engine.say("{} , {}".format(nick_name, beautiful_words))
        engine.runAndWait()

    if len(beautiful_words) == 0:
        # if no good words in cnf file , speak a random courage words
        engine.say("{} , {}".format(nick_name,random.choice(BEAUTIFUL_WORDS)))
        engine.runAndWait()


if __name__ == '__main__':
    main()
