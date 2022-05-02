import requests

# ~~~ make-request.py ~~~

urls = [ # all stolen from https://phishingquiz.withgoogle.com/ on 2022-04-27
  'https://drive--google.com/luke.johnson',
  'https://efax.hosting.com.mailru382.co/efaxdelivery/2017Dk4h325RE3',
  'https://drive.google.com.download-photo.sytez.net/AONh1e0hVP',
  'https://www.dropbox.com/buy',
  'westmountdayschool.org',
  'https://myaccount.google.com-securitysettingpage.ml-security.org/signonoptions/',
  'https://google.com/amp/tinyurl.com/y7u8ewlr',
  'www.tripit.com/uhp/userAgreement'
]

def do_request(urls):
    r = requests.post('http://localhost:5555/predict',json =urls)
  pass

# 1. First, `post` all the urls at the same time
do_request(urls)

# 2. Then, loop over the urls and post one at a time.
for url in urls:
  do_request([url])
