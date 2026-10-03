import pandas as pd
import pyodbc
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Connect to your local SQL Server instance and query your biopolymer table
conn_str = (
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=.\SQLEXPRESS;"
    r"DATABASE=agri_biopolymer_db;"
    r"Trusted_Connection=yes;"
)

# Pulling real experimental data from your SSMS table
query = "SELECT Purity_Percentage, Yield_Percentage FROM dbo.BIOPOLYMER_EXTRACTIONS"

print("Connecting to SQL Server and loading experimental data...")
df = pd.read_sql(query, pyodbc.connect(conn_str))
print("Data loaded successfully from SQL Server!")
print(df.head())

# 2. Separate features (X) and target (y)
X = df[["Purity_Percentage"]]
y = df["Yield_Percentage"]

# 3. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Test the model and view predictions against actual values
predictions = model.predict(X_test)
print("\nActual Yields on Test Set:", list(y_test))
print("Predicted Yields on Test Set:", list(predictions))