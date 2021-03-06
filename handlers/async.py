import json
import base
import models.tag
import models.post
import utils.dumpjson
import utils.escape

class AsyncHandler(base.BaseView):
    def post(self):
        self.args = json.loads(self.request.body)
        self.response.out.write(json.dumps(self.serve()))
