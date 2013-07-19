import base
import async
import models.post
import models.admin
import models.user

class Save(base.BaseView):
    @models.user.admin_only
    def post(self):
        conf = models.admin.SiteConfiguration.load_persist()
        conf.title = self.request.get('title').strip()
        conf.style = self.request.get('style').strip()
        conf.post_html = self.request.get('post_html').strip()
        models.admin.SiteConfiguration.save(conf)
        self.redirect('/c/siteconf')
