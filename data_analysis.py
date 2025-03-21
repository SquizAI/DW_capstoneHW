import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import json

# Set the style for seaborn
sns.set(style="whitegrid")

# Load the dataset
df = pd.read_csv('car_dataset.csv')

# Create directory for outputs
os.makedirs('outputs', exist_ok=True)

# ----- 1. Metadata Analysis -----
def generate_metadata():
    """Extract and save metadata about the dataset"""
    metadata = {
        "dataset_name": "Used Cars Dataset",
        "source": "GitHub - Machine Learning with R datasets",
        "num_records": len(df),
        "num_columns": len(df.columns),
        "columns": list(df.columns),
        "column_dtypes": {col: str(df[col].dtype) for col in df.columns},
        "missing_values": df.isnull().sum().to_dict(),
        "numerical_columns_stats": {
            col: {
                "min": float(df[col].min()) if pd.api.types.is_numeric_dtype(df[col]) else None,
                "max": float(df[col].max()) if pd.api.types.is_numeric_dtype(df[col]) else None,
                "mean": float(df[col].mean()) if pd.api.types.is_numeric_dtype(df[col]) else None,
                "median": float(df[col].median()) if pd.api.types.is_numeric_dtype(df[col]) else None,
                "std": float(df[col].std()) if pd.api.types.is_numeric_dtype(df[col]) else None
            } for col in df.columns
        },
        "categorical_columns_unique_values": {
            col: df[col].unique().tolist() 
            for col in df.columns if pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_categorical_dtype(df[col])
        }
    }
    
    # Save metadata to JSON file
    with open('outputs/metadata.json', 'w') as f:
        json.dump(metadata, f, indent=4)
    
    return metadata

# ----- 2. Data Extract -----
def create_data_extract():
    """Create and save a data extract with key information"""
    # Create a data extract with summary statistics
    data_extract = df.describe(include='all').transpose()
    
    # Add count of unique values for each column
    data_extract['unique_values'] = [df[col].nunique() for col in df.columns]
    
    # Save to CSV
    data_extract.to_csv('outputs/data_extract.csv')
    
    # Create a sample extract of the actual data
    df.head(50).to_csv('outputs/data_sample.csv', index=False)
    
    return data_extract

# ----- 3. Visualizations -----
def create_visualizations():
    """Create four basic visualizations"""
    
    # Visualization 1: Price Distribution by Year (Boxplot)
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='year', y='price', data=df)
    plt.title('Car Price Distribution by Year')
    plt.xlabel('Year')
    plt.ylabel('Price ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/viz1_price_by_year.png')
    plt.close()
    
    # Visualization 2: Mileage vs Price Scatter Plot with Transmission
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='mileage', y='price', hue='transmission', data=df)
    plt.title('Price vs Mileage by Transmission Type')
    plt.xlabel('Mileage')
    plt.ylabel('Price ($)')
    plt.tight_layout()
    plt.savefig('outputs/viz2_price_vs_mileage.png')
    plt.close()
    
    # Visualization 3: Color Distribution (Count Plot)
    plt.figure(figsize=(12, 6))
    color_counts = df['color'].value_counts()
    sns.barplot(x=color_counts.index, y=color_counts.values)
    plt.title('Car Color Distribution')
    plt.xlabel('Color')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/viz3_color_distribution.png')
    plt.close()
    
    # Visualization 4: Model Distribution (Count Plot)
    plt.figure(figsize=(12, 6))
    model_counts = df['model'].value_counts().head(10)
    sns.barplot(x=model_counts.index, y=model_counts.values)
    plt.title('Top 10 Car Models')
    plt.xlabel('Model')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/viz4_model_distribution.png')
    plt.close()
    
    # Create interactive Plotly versions for the dashboard
    
    # Interactive Visualization 1: Price Distribution by Year
    fig1 = px.box(df, x='year', y='price', title='Car Price Distribution by Year')
    fig1.update_layout(xaxis_title='Year', yaxis_title='Price ($)')
    fig1.write_html('outputs/interactive_viz1.html')
    
    # Interactive Visualization 2: Mileage vs Price Scatter Plot
    fig2 = px.scatter(df, x='mileage', y='price', color='transmission', 
                    title='Price vs Mileage by Transmission Type')
    fig2.update_layout(xaxis_title='Mileage', yaxis_title='Price ($)')
    fig2.write_html('outputs/interactive_viz2.html')
    
    # Interactive Visualization 3: Color Distribution
    color_df = color_counts.reset_index()
    color_df.columns = ['color', 'count']  # Rename columns after reset_index
    fig3 = px.bar(color_df, x='color', y='count', 
                title='Car Color Distribution')
    fig3.update_layout(xaxis_title='Color', yaxis_title='Count')
    fig3.write_html('outputs/interactive_viz3.html')
    
    # Interactive Visualization 4: Model Distribution
    model_df = model_counts.reset_index()
    model_df.columns = ['model', 'count']  # Rename columns after reset_index
    fig4 = px.bar(model_df, x='model', y='count', 
                title='Top 10 Car Models')
    fig4.update_layout(xaxis_title='Model', yaxis_title='Count')
    fig4.write_html('outputs/interactive_viz4.html')
    
    print("Visualizations created successfully!")

if __name__ == "__main__":
    # Generate metadata
    metadata = generate_metadata()
    print("Metadata generated and saved to outputs/metadata.json")
    
    # Create data extract
    data_extract = create_data_extract()
    print("Data extract created and saved to outputs/data_extract.csv")
    
    # Create visualizations
    create_visualizations()
    print("All visualizations saved to the outputs directory")
