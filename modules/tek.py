import feedparser

def videos:
  """Returns the videos RSS from the site"""
  d = feedparser.parse('http://teksyndicate.com/rss/videos')
  return d.entries

def find_in_videos(title):
  vids = videos
  found = false
  i = -1
  while found == false:
    i+= 1
    if vids[i].title.startswith(title):
      found = true
  if not vids[i].title.startswith(title):
    return false
  return vids[i]
    
def latest_tek:
  return find_in_videos('The Tek')

def the_tek(ep):
  return find_in_videos('The Tek 00'+ep)

def tek(phenny, input):
  ep = input.group(2)
  if not ep:
    return phenny.reply('Latest Tek is '+latest_tek.link)
  ep.strip("0")
  tek = the_tek(ep)
  if not tek:
    return phenny.reply('Latest Tek is '+latest_tek.link)
  return phenny.reply('Tek 00'+ep+': '+latest_tek.link)

tek.commands = ['tek']
tek.priority = 'high'
