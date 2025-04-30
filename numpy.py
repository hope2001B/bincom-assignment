import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import seaborn as sns


def load_cancer_data(file_path):
    """Load cancer incidence data from a CSV file"""
    try:
        data = pd.read_csv(file_path)
        print(f"Successfully loaded cancer data with {data.shape[0]} rows and {data.shape[1]} columns")
        print("\nFirst 5 rows of the data:")
        print(data.head())
        print("\nSummary statistics for key variables:")

        # Focus on key columns of interest
        key_columns = ['Age-Adjusted Incidence Rate', 'Average Annual Count', 'Recent Trend', '5-Year Trend']
        key_columns = [col for col in key_columns if col in data.columns]

        print(data[key_columns].describe())
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


def cancer_regression_analysis(data, test_size=0.2, random_state=42):
    """Perform regression analysis for cancer incidence data"""
    # Define variables
    x_column = 'Average Annual Count'
    y_column = 'Age-Adjusted Incidence Rate'

    print(f"\nPerforming linear regression analysis with '{x_column}' as predictor and '{y_column}' as target")

    # Check if columns exist in the dataframe
    if x_column not in data.columns or y_column not in data.columns:
        print(f"Error: One or both of the specified columns do not exist in the dataset")
        print(f"Available columns: {data.columns.tolist()}")
        return

    # Check for missing values
    if data[x_column].isnull().sum() > 0 or data[y_column].isnull().sum() > 0:
        print(f"Warning: Missing values detected in the data")
        print(f"Missing values in {x_column}: {data[x_column].isnull().sum()}")
        print(f"Missing values in {y_column}: {data[y_column].isnull().sum()}")
        print("Removing rows with missing values")
        data = data.dropna(subset=[x_column, y_column])

    # Examine the distribution of key variables
    plt.figure(figsize=(12, 6))

    # Distribution of predictor variable
    plt.subplot(1, 2, 1)
    sns.histplot(data[x_column], kde=True, color='blue')
    plt.title(f'Distribution of {x_column}')
    plt.xlabel(x_column)
    plt.ylabel('Frequency')

    # Distribution of target variable
    plt.subplot(1, 2, 2)
    sns.histplot(data[y_column], kde=True, color='green')
    plt.title(f'Distribution of {y_column}')
    plt.xlabel(y_column)
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

    # Look at initial correlation
    print(f"\nCorrelation between {x_column} and {y_column}: {data[x_column].corr(data[y_column]):.4f}")

    # Prepare the data
    X = data[x_column].values.reshape(-1, 1)  # Independent variable (predictor)
    y = data[y_column].values  # Dependent variable (target)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    print(f"Training data size: {X_train.shape[0]} counties")
    print(f"Testing data size: {X_test.shape[0]} counties")

    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Evaluate the model
    train_mse = mean_squared_error(y_train, y_train_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    train_r2 = r2_score(y_train, y_train_pred)
    test_r2 = r2_score(y_test, y_test_pred)

    # Print the results
    print("\nCancer Incidence Linear Regression Results:")
    print(f"Slope (coefficient): {model.coef_[0]:.8f}")
    print(f"Intercept: {model.intercept_:.4f}")
    print(f"Regression equation: {y_column} = {model.coef_[0]:.8f} × {x_column} + {model.intercept_:.4f}")
    print("\nModel Evaluation:")
    print(f"Training MSE: {train_mse:.4f}")
    print(f"Testing MSE: {test_mse:.4f}")
    print(f"Training R²: {train_r2:.4f}")
    print(f"Testing R²: {test_r2:.4f}")

    # Visualize the results
    plt.figure(figsize=(16, 12))

    # Plot 1: Scatter plot with regression line
    plt.subplot(2, 2, 1)
    plt.scatter(X, y, color='blue', alpha=0.3, label='Counties')

    # Sort X_test for smoother line plotting
    sorted_indices = np.argsort(X_test.flatten())
    plt.plot(X_test[sorted_indices], y_test_pred[sorted_indices], color='red', linewidth=2, label='Regression line')

    plt.title(f'Linear Regression: {y_column} vs {x_column}')
    plt.xlabel(f'{x_column} (Average cases per year)')
    plt.ylabel(f'{y_column} (per 100,000 population)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    # Plot 2: Residuals plot
    plt.subplot(2, 2, 2)
    residuals = y_test - y_test_pred
    plt.scatter(y_test_pred, residuals, color='green', alpha=0.5)
    plt.axhline(y=0, color='red', linestyle='-')
    plt.title('Residuals Plot')
    plt.xlabel('Predicted Incidence Rate')
    plt.ylabel('Residuals')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Plot 3: Distribution of residuals
    plt.subplot(2, 2, 3)
    sns.histplot(residuals, kde=True, color='purple')
    plt.title('Distribution of Residuals')
    plt.xlabel('Residual Value')
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', alpha=0.7)

    # Plot 4: Actual vs Predicted
    plt.subplot(2, 2, 4)
    plt.scatter(y_test, y_test_pred, color='orange', alpha=0.5)
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
    plt.title('Actual vs Predicted Incidence Rates')
    plt.xlabel('Actual Incidence Rate')
    plt.ylabel('Predicted Incidence Rate')
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

    # Create a prediction function for user queries
    def predict_incidence_rate(annual_count):
        return model.coef_[0] * annual_count + model.intercept_

    # Provide some example predictions
    example_counts = [10, 50, 100, 500, 1000, 5000]
    print("\nExample predictions:")
    print("Average Annual Count | Predicted Incidence Rate")
    print("-" * 45)
    for count in example_counts:
        prediction = predict_incidence_rate(count)
        print(f"{count:19d} | {prediction:.4f}")

    return model, (train_mse, test_mse, train_r2, test_r2)


def analyze_county_factors(data):
    """Analyze additional factors that might influence cancer incidence rates"""
    # Check if we have geographic or demographic data to use
    if 'FIPS' in data.columns and 'County' in data.columns:
        print("\nTop 10 counties with highest incidence rates:")
        top_counties = data.sort_values('Age-Adjusted Incidence Rate', ascending=False).head(10)
        print(top_counties[['County', 'Age-Adjusted Incidence Rate', 'Average Annual Count']])

        print("\nTop 10 counties with lowest incidence rates:")
        bottom_counties = data.sort_values('Age-Adjusted Incidence Rate').head(10)
        print(bottom_counties[['County', 'Age-Adjusted Incidence Rate', 'Average Annual Count']])

    # Check if we have trend data
    if 'Recent Trend' in data.columns:
        # Count by trend direction
        trend_counts = data['Recent Trend'].value_counts()
        print("\nDistribution of recent trends:")
        print(trend_counts)

        # Visualize trends
        plt.figure(figsize=(10, 6))
        sns.countplot(x='Recent Trend', data=data, palette='viridis')
        plt.title('Distribution of Recent Cancer Incidence Trends')
        plt.xlabel('Trend Direction')
        plt.ylabel('Number of Counties')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

        # Compare average incidence rates by trend group
        trend_avg = data.groupby('Recent Trend')['Age-Adjusted Incidence Rate'].mean().sort_values(ascending=False)
        print("\nAverage incidence rate by trend direction:")
        print(trend_avg)

        # Visualize the relationship
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Recent Trend', y='Age-Adjusted Incidence Rate', data=data, palette='viridis')
        plt.title('Incidence Rate Distribution by Trend Direction')
        plt.xlabel('Trend Direction')
        plt.ylabel('Age-Adjusted Incidence Rate')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()


def main():
    print("Cancer Incidence Linear Regression Analysis")
    print("------------------------------------------")

    # Get the file path
    file_path = input("Enter the path to your cancer incidence CSV file: ")

    # Load the data
    data = load_cancer_data(file_path)
    if data is None:
        return

    # Perform regression analysis
    model, metrics = cancer_regression_analysis(data)

    # Additional analyses
    analyze_county_factors(data)

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()