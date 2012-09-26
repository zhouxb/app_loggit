def cut_head(seqence):
    head = seqence[0]
    body = seqence[1:] if len(seqence) > 1 else []
    return head, body

class RadixNode(object):
    __slots__ = ["children", "is_terminal"] # may save some memory, I wish

    def __init__(self, is_terminal=False):
        self.children = {}
        self.is_terminal = is_terminal

class RadixTree(object):
    '''
    A data structure similar with dict, but supporting looking up element by 
    prefix with *like* method
    e.g.
    >>> tree = RadixTree(split=lambda x: x.split("."), join=".".join)
    >>> tree.insert("www.google.com")
    >>> tree.insert("www.google")
    >>> tree.insert("www")
    >>> tree.like("www.google")
    ['www.google', 'www.gogle.com']
    '''
    def __init__(self, split=lambda x: x.split(), join=lambda xs: " ".join(xs)):
        self.split = split
        self.join  = join
        self.root = RadixNode(is_terminal=True)

    def insert(self, elem):
        def do_insert(node, parts):
            head, body = cut_head(parts)
            if head not in node.children:
                node.children[head] = RadixNode()
            if body:
                do_insert(node.children[head], body)
            else:
                node.children[head].is_terminal = True

        parts = self.split(elem)
        do_insert(self.root, parts)

    def items(self):
        all_items = []

        def do_get(node, node_name, parts):
            if node.is_terminal:
                all_items.append(self.join(parts + [node_name]))
            for name, child  in node.children.iteritems():
                do_get(child, name,  parts + [node_name])

        for name, child  in self.root.children.iteritems():
            do_get(child, name, [])

        return all_items

    def like(self, elem):
        like_item = []

        def get_childs(node, prefixes):
            if node.is_terminal:
                like_item.append(self.join(prefixes))
            for name, child in node.children.iteritems():
                get_childs(child, prefixes + [name])

        def find_like(node, parts):
            head, body = cut_head(parts)
            if head not in node.children:
                return
            if not body:
                get_childs(node.children[head], self.split(elem))
            else:
                find_like(node.children[head], body)

        find_like(self.root, self.split(elem))
        return like_item

    def __contains__(self, elem):
        parts = self.split(elem)

        def find_parts(node, parts):
            head, body = cut_head(parts)
            if head not in node.children:
                return False
            if not body:
                return node.children[head].is_terminal
            return find_parts(node.children[head], body)

        return find_parts(self.root, parts)

    def __delitem__(self, elem):
        if elem not in self:
            return

        # only mark item not used, do not really delete it
        def do_delete(node,  parts):
            head, body = cut_head(parts)

            if not body:
                node.children[head].is_terminal = False
            else:
                do_delete(node.children[head], body)

        do_delete(self.root, self.split(elem))

class RRadixTree(RadixTree):
    '''
    Reversed RadixTree, supports look up element by sufix with *like* method
    e.g.
    >>> tree = RRadixTree(split=lambda x: x.split("."), join=".".join)
    >>> tree.insert("www.google.com")
    >>> tree.insert("www.sina.com")
    >>> tree.insert("com")
    >>> tree.like("sina.com")
    ['www.sina.com']
    '''
    def __init__(self, split=lambda x: x.split(), join=lambda xs: " ".join(xs)):
        rsplit = lambda elem: split(elem)[::-1]
        rjoin  = lambda parts: join(parts[::-1])
        super(self.__class__, self).__init__(split=rsplit, join=rjoin)

def main():
    tree = RadixTree(split=lambda x: x.split("."), join=".".join)
    for i in xrange(1000000):
        tree.insert("www.google.%s.com" % i)

if __name__ == '__main__':
    main()
