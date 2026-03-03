import oci  # Oracle SDK
import os
import requests  # for Netlify/Render APIs

def monitor_oracle_db(instance_id):
    config = oci.config.from_file()
    adb_client = oci.database.AutonomousDatabaseClient(config)
    db = adb_client.get_autonomous_database(instance_id)
    if db.data.cpu_core_count > 0.8 * db.data.cpu_core_count_limit:  # 80% threshold
        # Revenue check stub
        if get_revenue_balance() > 100:  # R100 threshold
            adb_client.update_autonomous_database(instance_id, update_autonomous_database_details=oci.database.models.UpdateAutonomousDatabaseDetails(cpu_core_count=2))  # Upgrade to paid
    return "Scaled"

def monitor_netlify(site_id, token):
    r = requests.get(f"https://api.netlify.com/api/v1/sites/{site_id}", headers={"Authorization": f"Bearer {token}"})
    bandwidth_used = r.json()["bandwidth_used"]
    if bandwidth_used > 70:  # 70 GB threshold
        if get_revenue_balance() > 350:  # R350 for Pro
            # API upgrade stub – manual for now, AI notifies
            print("Upgrade to Pro recommended")

# Call in cron
