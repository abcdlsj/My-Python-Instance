import random
import string
def Makepass(length=20, chars=string.ascii_letters+string.digits+'string.punctuation'):
        return ''.join([random.choice(chars) for i in range(length)])

if __name__=='__main__':
    print(Makepass())