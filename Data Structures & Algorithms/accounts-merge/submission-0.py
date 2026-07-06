class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        parent=[i for i in range(n)]
        size=[1]*n

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            rootx=find(x)
            rooty=find(y)
            if rootx==rooty:
                return 
            if size[rootx]<size[rooty]:
                rootx,rooty=rooty,rootx
            parent[rooty]=rootx
            size[rootx]=size[rooty]+size[rootx]
        emailid={}
        for i,a in enumerate(accounts):
            for email in a[1:]:
                if email in emailid:
                    union(i,emailid[email])
                else:
                    emailid[email]=i
        emailgroup=defaultdict(list)
        for e,i in emailid.items():
            leader=find(i)
            emailgroup[leader].append(e)
        res=[]
        for i,emails in emailgroup.items():
            name=accounts[i][0]
            res.append([name]+sorted(emailgroup[i]))
        return res