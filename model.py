import pandas as pd
from sklearn.cluster import KMeans

def cluster_customers():
    df = pd.read_csv("mall_customers.csv")
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    
    kmeans = KMeans(n_clusters=5, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    # Format data for frontend
    result = df[['CustomerID', 'Annual Income (k$)', 'Spending Score (1-100)', 'Cluster']].to_dict(orient='records')
    return result
