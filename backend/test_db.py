from app.database.session import SessionLocal

db = SessionLocal()

try:
    print("Database Connected")
finally:
    db.close()