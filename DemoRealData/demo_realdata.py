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
b0 = -1.0
d = 1e4           # domain parameter (currently unused in core logic)

#attrs, coeffs, score = tabu_search.run_tabu_search(X, y, b0, d)
#attrs, coeffs, score = tabu_search.run_tabu_search(X, y, b0, d, iSeed=12345)
#attrs, coeffs, score = tabu_search.run_tabu_search(X, y, b0, d, iSeed=123456)
attrs, coeffs, score = hitspy.run_tabu_search(X, y, b0, d, iSeed=123456)

print("Attributes:", attrs)
print("Coeffs:", coeffs)
print("Score:", score)
