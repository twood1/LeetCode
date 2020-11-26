import collections
class UnionFind():
    def __init__(self):
        self.parent = list(range(10001))

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry


class Solution:
    def accountsMerge(self, accounts):

        email2name = {}
        email2index = {}
        i = 0
        uf = UnionFind()
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email2index:
                    email2name[email] = name
                    email2index[email] = i
                    i += 1
                uf.union(email2index[account[1]], email2index[email])
        emailGroup = collections.defaultdict(list)
        for email in email2index:
            emailGroup[uf.find(email2index[email])].append(email)

        return [[email2name[emails[0]]] + sorted(emails) for emails in emailGroup.values()]


sol = Solution()
retval = sol.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"],
                            ["John", "johnnybravo@mail.com"],
                            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                            ["Mary", "mary@mail.com"]])

print(retval)

