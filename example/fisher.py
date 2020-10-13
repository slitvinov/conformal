import conformal

z = [17, 20, 10, 17, 12, 15, 19, 22, 17, 19, 14, 22, 18, 17, 13, 12, 18, 15, 17]
print("nn:    ", conformal.gamma("nn", z, eps = 0.05))
print("mean:  ", conformal.gamma("mean", z, eps = 0.05))
print("median:", conformal.gamma("median", z, eps = 0.05))
print("fisher:", conformal.fisher(z, eps = 0.05))
