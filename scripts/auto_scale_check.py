from backend.services.auto_scaling import monitor_oracle_db

print("Checking scaling...")
monitor_oracle_db("your-instance-ocid")
