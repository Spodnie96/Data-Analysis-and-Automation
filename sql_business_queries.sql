-- Łączę tabele przez JOIN, bo to standardowy i najwygodniejszy sposób na wyciągnięcie powiązanych danych
SELECT 
    c.CustomerID,
    c.CustomerName,
    c.Country,
    COUNT(o.OrderID) AS TotalOrders,
    SUM(o.TotalAmount) AS TotalSpent
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderDate >= '2024-01-01'
GROUP BY c.CustomerID, c.CustomerName, c.Country
HAVING SUM(o.TotalAmount) > 1000
ORDER BY TotalSpent DESC;

-- Używam funkcji okna (OVER + PARTITION BY), bo można łatwo policzyć średnią bez zwijania całej tabeli
SELECT 
    OrderID,
    CustomerID,
    OrderDate,
    TotalAmount,
    AVG(TotalAmount) OVER(PARTITION BY CustomerID) AS AvgCustomerOrderValue,
    RANK() OVER(PARTITION BY CustomerID ORDER BY TotalAmount DESC) AS OrderRank
FROM Orders;
