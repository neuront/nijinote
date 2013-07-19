from google.appengine.ext import db
from google.appengine.api import memcache

class SiteConfiguration(db.Model):
    title = db.StringProperty(multiline=False)
    style = db.StringProperty(multiline=False)

    @staticmethod
    def load_persist():
        conf = SiteConfiguration.all()
        if conf.count() == 0:
            conf = SiteConfiguration()
            conf.title = 'A NijiPress Site'
            conf.style = 'midnight'
            return conf
        return conf[0]

    @staticmethod
    def load():
        cache = memcache.get('siteconf')
        if cache == None:
            cache = SiteConfiguration.load_persist()
            memcache.set('siteconf', cache)
        return cache

    @staticmethod
    def save(conf):
        memcache.set('siteconf', conf)
        conf.put()
