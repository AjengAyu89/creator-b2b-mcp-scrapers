import os
from apify_client import ApifyClient

token = os.environ.get("APIFY_TOKEN")
if not token:
    raise RuntimeError("Set APIFY_TOKEN environment variable before running.")

client = ApifyClient(token)

# 1. Skool communities & owner B2B contacts
skool_run = client.actor("ajengayu89/skool-intelligence-scraper").call(
    run_input={
        "targets": ["https://www.skool.com/makerschool", "AI automation"],
        "mode": "communities",
        "maxItems": 10,
        "enrichWebsiteContacts": True,
    }
)
print("=== Skool Communities ===")
for item in client.dataset(skool_run["defaultDatasetId"]).iterate_items():
    print(
        item.get("displayName"),
        "| MRR min:", item.get("estimatedMrrMin"),
        "| Emails:", item.get("emails"),
    )

# 2. Patreon creators & estimated monthly revenue
patreon_run = client.actor("ajengayu89/patreon-intelligence-scraper").call(
    run_input={
        "mode": "creators",
        "searchQueries": ["podcast"],
        "maxItems": 10,
        "enrichContacts": True,
    }
)
print("\n=== Patreon Creators ===")
for item in client.dataset(patreon_run["defaultDatasetId"]).iterate_items():
    print(
        item.get("creatorName"),
        "| Est. Monthly Rev USD:", item.get("estimatedMonthlyRevenueUsd"),
        "| Paid Conv %:", item.get("paidConversionRate"),
    )
