from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///db/bluestock_mf.db")

# Open a connection
conn = engine.connect()

print("Database created successfully!")

conn.close()