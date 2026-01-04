from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

class HousingRegressionPipeline:
    def __init__(self):
        self.scaler = StandardScaler()
        self.model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

    def fit(self, X_train, y_train):
        X_train_scaled = self.scaler.fit_transform(X_train)
        self.model.fit(X_train_scaled, y_train)

    def predict(self, X_new):
        X_new_scaled = self.scaler.transform(X_new)
        return self.model.predict(X_new_scaled)
