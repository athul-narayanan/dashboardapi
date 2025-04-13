import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

class ProductRecommender:
    def __init__(self, df):
        self.df = df

    # Train Test split
    def split_dataset(self, df):
        split_index = int(len(df) * 0.8)
        train_df = df.iloc[:split_index]
        test_df = df.iloc[split_index:]
        return train_df, test_df

    # Customer-Item Matrix Generator
    def get_customer_item_matrix(self, df):
        return df.pivot_table(index='CustomerID',
                              columns='Description',
                              values='Quantity',
                              aggfunc='sum',
                              fill_value=0)

    # Build Model
    def build_model(self, country):
        df_country = self.df[self.df['Country'] == country].sort_values('InvoiceDate')
        print(df_country.shape)
        
        # Split train test set
        train_df, _ = self.split_dataset(df_country)

        # User-item matrix
        matrix = self.get_customer_item_matrix(train_df)

         # TF-IDF transformation
        item_user_matrix = matrix.T
        tfidf = TfidfTransformer()
        tfidf_matrix = tfidf.fit_transform(item_user_matrix)

        # Cosine similarity
        item_sim = cosine_similarity(tfidf_matrix)
        item_sim_df = pd.DataFrame(item_sim, index=item_user_matrix.index, columns=item_user_matrix.index)

        return matrix, item_sim_df

    # Recommend Product
    def recommend_products(self, country, user_id, top_k=10, top_n_similar=5):
        matrix, item_sim_df = self.build_model(country)

        if user_id not in matrix.index:
            return f"User {user_id} not found in {country} training data."

        purchased = matrix.loc[user_id]
        purchased_items = purchased[purchased > 0].index.tolist()

        scores = {}

        for item in purchased_items:
            if item not in item_sim_df:
                continue
            similar_items = item_sim_df[item].sort_values(ascending=False)[1:top_n_similar+1]
            for sim_item, score in similar_items.items():
                if sim_item not in purchased_items:
                    scores[sim_item] = scores.get(sim_item, 0) + score

        recommended = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
        return [item for item, _ in recommended]
