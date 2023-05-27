class MyMixin(object):
    mixin_prop = ''
    pagination_num = 2

    def get_prop(self):
        return self.mixin_prop.upper()

    def get_upper(self, s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()

    def get_pagination_number():
        return 2
