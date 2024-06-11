from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pickle

# モデルのトレーニングデータを用意
X_train = [[1], [2], [3], [4], [5]]
y_train = [1, 4, 9, 16, 25]

# PolynomialFeaturesの適用
poly_reg = PolynomialFeatures(degree=6)
X_poly = poly_reg.fit_transform(X_train)

# モデルのトレーニング
model = LinearRegression()
model.fit(X_poly, y_train)

# モデルの保存
with open('model4.pkl', 'wb') as file:
    pickle.dump(model, file)