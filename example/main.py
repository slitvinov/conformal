import conformal

z = [17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18, 15, 17]
ans = conformal.gamma("nn", z, eps = 0.05)
print(ans)
