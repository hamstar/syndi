from random import choice

def rustle(phenny, input):
    with open('/home/and/phenny/modules/verbs') as f:
         l = f.readlines()
         verb = choice(l).strip('\n')
    with open('/home/and/phenny/modules/nouns') as f:
         l = f.readlines()
         noun = choice(l).strip('\n')
         
    phenny.say('That really {0} my {1}.'.format(verb, noun))

rustle.commands = ['rustle']
rustle.priority = 'high'
