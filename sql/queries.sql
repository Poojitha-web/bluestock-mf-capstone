-- Top 5 Funds by AUM
SELECT *
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV per Month
SELECT
strftime('%Y-%m',date) month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- SIP YoY Growth
SELECT *
FROM monthly_sip_inflows;

-- Transactions by State
SELECT
state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Funds with Expense Ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;