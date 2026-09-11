import numpy as np
import hitspy

X=np.loadtxt("X.txt")
X=X[:,1:]
X=np.transpose(X)
X = np.ascontiguousarray(X, dtype=np.float64)
print(X)
y=np.loadtxt("y.txt")
y=y[:,1]
print(y)

T = X.shape[0]
p = X.shape[1]          # attributes
#p_in = p + 1    # intercept + attributes
p_in = p     # intercept + attributes

#X = np.random.randn(p_in, T).astype(np.float64)
#y = np.random.choice([-1, 1], size=T).astype(np.int32)
b0 = -1.0 #Martins, Kordas
#b0 = 1.0 #Moro
d = 10           # domain parameter (currently unused in core logic)

#Martins
Nreps=30
for i in range(Nreps):
    attrs, coeffs, score = hitspy.run_tabu_search(X, y, b0, d, iSeed=12345+i)
    print("========",i+1,"========")
    print("Attributes:", attrs)
    print("Coeffs:", coeffs)
    print("Score:", score)

#Kordas
#Nreps=3
#for i in range(Nreps):
    #attrs, coeffs, score = tabu_search.run_tabu_search(X, y, b0, d, iSeed=12345+i)
#    attrs, coeffs, score = hitspy.run_tabu_search(X, y, b0, d, iSeed=123456+i)
#    print("========",i+1,"========")
#    print("Attributes:", attrs)
#    print("Coeffs:", coeffs)
#    print("Score:", score)

#Kordas
#Nreps=20
#for i in range(Nreps):
#    print("========",i+1,"========")
    #attrs, coeffs, score = tabu_search.run_tabu_search(X, y, b0, d, iSeed=12345+i)
    #attrs, coeffs, score = tabu_search.run_tabu_search(X, y, b0, d, iSeed=123456+i)
#    attrs, coeffs, score = hitspy.run_tabu_search(X, y, b0, d, iSeed=1234567 + i)
#    print("Attributes:", attrs)
#    print("Coeffs:", coeffs)
#    print("Score:", score)
