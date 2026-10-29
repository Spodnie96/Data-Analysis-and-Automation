import pandas as pd

# Używam słownika, bo to najprostszy sposób na szybkie zasymulowanie tabeli w kodzie
data = {
    'Transaction_ID': [101, 102, 103, 104, 105],
    'Region': ['Europe', 'Europe', 'North America', 'Europe', 'North America'],
    'Sales_Value': [1200.50, None, 3400.00, 2100.00, 1500.00],
    'Status': ['Completed', 'Pending', 'Completed', 'Completed', 'Cancelled']
}

df = pd.DataFrame(data)

# Używam fillna, bo to najszybsza metoda na uzupełnienie braków (wstawiamy średnią)
mean_sales = df['Sales_Value'].mean()
df['Sales_Value'].fillna(mean_sales, inplace=True)

# Filtruję tylko zakończone transakcje, bo tylko one nas interesują do raportu
completed_sales = df[df['Status'] == 'Completed']

# Używam groupby, bo najprościej i najszybciej wyciąga podsumowanie po regionach
summary = completed_sales.groupby('Region')['Sales_Value'].agg(['sum', 'mean', 'count']).reset_index()
summary.rename(columns={'sum': 'Total_Sales', 'mean': 'Avg_Sales', 'count': 'Transaction_Count'}, inplace=True)

print("Podsumowanie sprzedaży według regionu:")
print(summary)
