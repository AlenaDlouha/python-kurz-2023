import pandas as pd
u202 = pd.read_csv("u202.csv").dropna()
u203 = pd.read_csv("u203.csv").dropna()
u302 = pd.read_csv("u302.csv").dropna()
u202["mistnost"] = "u202"
u203["mistnost"] = "u203"
u302["mistnost"] = "u302"
