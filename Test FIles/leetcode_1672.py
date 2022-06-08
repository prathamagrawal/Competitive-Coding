from traceback import print_tb


accounts = [[1,2,3],[3,2,1]]
rows=len(accounts)
columns = len(accounts[0])
print("rows"+str(rows)+" columns"+str(columns))
for i in range(rows):
    for j in range(columns):
        print(accounts[i][j])
        print("\n")