class RangeDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, range):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)


class TupleDict(dict):
    def __getitem__(self, item):
        if not isinstance(item, tuple):
            for key in self:
                if item in key:
                    return self[key]
            raise KeyError(item)
        else:
            return super().__getitem__(item)

class Tree(dict):
    def __missing__(self, key):
        value = self[key] = type(self)()
        return value
