from radixtree import RRadixTree

def tails(sequence):
    '''
    >>> tails("abcd")
    ['abcd', 'bcd', 'cd', 'd']
    '''
    if not sequence:
        return []
    else:
        return [sequence[i:] for i in xrange(len(sequence))]

class UniqDomainContainer:
    '''
    A Container allow insert generic domain into it. it will auto resovle 
    conflict cases
    e.g.
    >>> uniq = UniqDomainContainer()
    >>> uniq.insert("*.baidu.com")
    >>> uniq.insert("*.img.baidu.com")
    >>> uniq.insert("*.video.baidu.com")
    >>> uniq.items()
    ['*.baidu.com']
    '''
    def __init__(self):
        self.tree = RRadixTree(split=lambda x: x.split("."), join=".".join)

    def insert(self, generic_domain):
        base = generic_domain[2:]

        for tail in tails(base.split(".")):
            superdomain = "*." + ".".join(tail)
            if superdomain in self.tree:
                return

        for domain in self.tree.like(base):
            del self.tree[domain]

        self.tree.insert(generic_domain)

    def batch_insert(self, domains):
        for domain in domains:
            self.insert(domain)

    def items(self):
        return self.tree.items()

def rule_update(old_rules, new_rule):
    uniq = UniqDomainContainer()
    uniq.batch_insert(old_rules)
    uniq.insert(new_rule)
    new_rules = uniq.items()

    add_rules = list(set(new_rules) - set(old_rules))
    del_rules = list(set(old_rules) - set(new_rules))

    return add_rules, del_rules




