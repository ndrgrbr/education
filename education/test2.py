class ReprMixin(object):
    def __repr__(self):
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(['{}={}'.format(k, v) for k, v in self.__dict__.items()])
        )
class EqMixin(object):
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
