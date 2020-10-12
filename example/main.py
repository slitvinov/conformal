import conformal

z = [11, 17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18, 15, 17]
z = [1, 2, 3, 4, 1, 2, 102, 103, 104, 108]
ans = conformal.gamma("mean", z, eps = 0.95)
print(ans)
