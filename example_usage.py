from client import B2bNewMediaCreatorBrandGrowthAutomatorClient

def main():
    client = B2bNewMediaCreatorBrandGrowthAutomatorClient()
    brand = {"name": "Flowmatic SaaS", "category": "AI Workflow Automation", "target_cac_usd": 50}
    res = client.run_growth_campaign(brand, "B2B SaaS Founders & Growth Leads")
    proj = res["projected_reach"]
    print(f"Projected Reach: {proj['total_impressions']:,} impressions | {proj['estimated_new_signups']:,} est. signups | CAC ${proj['cac_estimate_usd']}")
    print("Matched Creators:")
    for c in res["matched_creators"]:
        print(f"  {c['creator']} — Brand Fit: {c['brand_fit_score']}/100")

if __name__ == "__main__":
    main()
