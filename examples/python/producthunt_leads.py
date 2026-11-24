import os
from apify_client import ApifyClient

token = os.environ.get("APIFY_TOKEN")
if not token:
    raise RuntimeError("Set APIFY_TOKEN environment variable before running.")

client = ApifyClient(token)

run = client.actor("ajengayu89/producthunt-intelligence-scraper").call(
    run_input={
        "mode": "leaderboard",
        "period": "daily",
        "maxItems": 20,
        "enrichStartupContacts": True,
        "incrementalMode": False,
        "proxyConfiguration": {"useApifyProxy": True},
    }
)

items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
outreach_leads = [item for item in items if item.get("outreachReady") is True]

print(f"Fetched {len(items)} launches; {len(outreach_leads)} outreach-ready leads:")
for lead in outreach_leads:
    print(
        f"#{lead.get('dailyRank') or lead.get('rank')} {lead.get('name')} | "
        f"Traction: {lead.get('tractionScore')} | "
        f"Website: {lead.get('websiteUrl')} | "
        f"Emails: {lead.get('emails')}"
    )
