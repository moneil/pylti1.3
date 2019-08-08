class DeepLinkResource(object):
    _type = 'ltiResourceLink'
    _title = None
    _url = None
    _lineitem = None
    _custom_params = []
    _target = 'iframe'

    def get_type(self):
        return self._type

    def set_type(self, value):
        self._type = value
        return self

    def get_title(self):
        return self._title

    def set_title(self, value):
        self._title = value
        return self

    def get_url(self):
        return self._url

    def set_url(self, value):
        self._url = value
        return self

    def get_lineitem(self):
        return self._lineitem

    def set_lineitem(self, value):
        self._lineitem = value
        return self

    def get_custom_params(self):
        return self._custom_params

    def set_custom_params(self, value):
        self._custom_params = value
        return self

    def get_target(self):
        return self._target

    def set_target(self, value):
        self._target = value
        return self

    def to_dict(self):
        res = {
            'type': self._type,
            'title': self._title,
            'url': self._url,
            'presentation': {
                'documentTarget': self._target
            },
            'custom': self._custom_params
        }
        if self._lineitem:
            res['lineItem'] = {
                'scoreMaximum': self._lineitem.get_score_maximum(),
                'label': self._lineitem.get_label()
            }
        return res
