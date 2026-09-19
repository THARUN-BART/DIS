data = [
("Credentials","SQL Injection","High","High","Parameterized queries"),
("Sensitive Data","Data Theft","Medium","High","RBAC"),
("Server","DoS Attack","Low","Medium","Firewall")
]

risk = {
("High","High"):"Critical",
("High","Medium"):"High",
("Medium","High"):"High",
("Medium","Medium"):"Moderate",
("Low","Medium"):"Low"
}

for a,t,l,i,m in data:
    print(a, t, risk[(l,i)], m)