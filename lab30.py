def ranking(first, second, third):
    print(f"1st:[{first}],2nd:[{second}],3rd:[{third}]")


ranking("Mark", "Ken", "Tim")
l1 = ["Mark", "Ken", 'Tim']
ranking(*l1)
l2 = ["Mark", "Ken"]
ranking("mary", *l2)
ranking(*l2, "Mary")