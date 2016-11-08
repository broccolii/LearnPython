from twitter import *

token = '2925550651-7LKsc1biQxQ8ntR9ZqRc0gBP6lzzhwWCC0365LE'
token_secret = 's33Fo0KPaJaNZ6STmxKXeuVYbHhuk2ZR7o9ztM1twz7lh'
consumer_key = 'tUNZTiVPgQ6bL00lHBArSfxah'
consumer_secret = 'IkgUOVS1cbp1Ocpy8wQmetRSf3Ml0BqJ8f2kJ4jl4w0TEn1M5j'
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))
pythonTweets = t.search.tweet(q="#python")
print(ptyhonTweets)