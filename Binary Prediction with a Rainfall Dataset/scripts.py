import seaborn as sns
import matplotlib.pyplot as plt

def plot_boxplot(df, column, title=None):
    """
    Plota um boxplot para uma coluna específica de um DataFrame.
    
    Parâmetros:
    - df: DataFrame do pandas contendo os dados.
    - column: Nome da coluna a ser plotada.
    - title: Título opcional do gráfico.
    """
    if column not in df.columns:
        raise ValueError(f"A coluna '{column}' não está no DataFrame.")

    plt.figure(figsize=(6, 4))
    sns.boxplot(y=df[column])
    plt.title(title if title else f"Boxplot de {column}")
    plt.ylabel(column)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.show()


def plot_correlation_heatmap(df, title="Matriz de Correlação"):
    """
    Plota um heatmap da matriz de correlação de um DataFrame.

    Parâmetros:
    - df: DataFrame do pandas contendo os dados.
    - title: Título opcional do gráfico.
    """
    plt.figure(figsize=(10, 6))
    corr_matrix = df.corr()  # Calcula a matriz de correlação
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title(title)
    plt.show()
