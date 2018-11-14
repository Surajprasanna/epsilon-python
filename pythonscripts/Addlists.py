l1=[1,2,3]
l2=[4,5,6]

def Addlist(list1,list2):
        Sumlist=[]
	for v1,v2 in zip(list1,list2):
		Sumlist.append(Summation)
        return Sumlist

'''
def Addlist(list1,list2):
	Sumlist=[]
	for index in list(range(len(l1))):
		Summation=list1[index]+list2[index]
		Sumlist.append(Summation)
	return Sumlist
'''

Result=Addlist(l1,l2)
print(Result)
