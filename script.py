import pandas as pd
import numpy as np

print("SHADOWED REALMS RPG - REALISTIC ASSET VALUATION ANALYSIS")
print("Based on actual marketplace data from Unity Asset Store, Unreal Marketplace, etc.")
print("=" * 80)

# Real marketplace data from research
# Unity Asset Store: $50 asset = $2000-3000 over few years [web:120]
# Successful seller: $524,900 gross revenue ($367,000 after 30% Unity cut) [web:123]
# First year seller: $542 gross = $379 net [web:125]
# Average hourly: $20-60 depending on success [web:120]

# MONTH-BY-MONTH REALISTIC ASSET CREATION AND VALUES

asset_breakdown = {
    'Month': [1, 2, 3, 4, 5, 6],
    'Month Focus': [
        'Foundation & Setup',
        'Characters & Animation', 
        'Environments & Rendering',
        'Web & Community',
        'Polish & Integration',
        'Launch & Marketing'
    ],
    'Assets Created': [15, 25, 30, 20, 25, 35],  # More realistic numbers
    'High-Value Items': [2, 4, 5, 3, 4, 6],     # Premium assets per month
    'Medium-Value Items': [8, 12, 15, 10, 12, 18], # Mid-tier assets
    'Low-Value Items': [5, 9, 10, 7, 9, 11],    # Basic assets/tools
}

monthly_df = pd.DataFrame(asset_breakdown)

print("\nMONTHLY ASSET CREATION BREAKDOWN:")
print("-" * 50)
print(monthly_df.to_string(index=False))

# REALISTIC PRICING BASED ON RESEARCH
pricing_strategy = {
    'Asset Category': [
        'Character Models (rigged)',
        'Animation Packs', 
        'Environment Packs',
        'Shader/Material Packs',
        'Tool Scripts/Extensions',
        'UI/Interface Packs',
        'Audio/Music Packs',
        'Complete Game Kits',
        'Tutorial/Educational',
        'VFX/Particle Systems'
    ],
    'Unity Store Price': [45, 35, 55, 25, 40, 30, 20, 150, 75, 35],
    'Unreal Price': [50, 40, 60, 30, 45, 35, 25, 175, 85, 40],
    'GameDev Market': [40, 30, 50, 20, 35, 25, 15, 125, 65, 30],
    'Monthly Sales Est': [3, 5, 4, 8, 6, 4, 10, 1, 2, 3],
    'Revenue Per Month': [135, 175, 220, 200, 240, 120, 200, 150, 150, 105]
}

pricing_df = pd.DataFrame(pricing_strategy)
print(f"\n\nREALISTIC ASSET PRICING & REVENUE:")
print("-" * 50)
print(pricing_df.to_string(index=False))

total_monthly_revenue = pricing_df['Revenue Per Month'].sum()
print(f"\nTotal Monthly Revenue Potential: ${total_monthly_revenue}")

# ACTUAL ASSET PRODUCTION PLAN
specific_assets = {
    'Asset Name': [
        # Month 1 Foundation (15 assets)
        'Maya-Unity Pipeline Tools', 'Character Rig Templates', 'Basic Anime Shaders',
        'Project Setup Scripts', 'Git Workflow Templates',
        
        # Month 2 Characters (25 assets) 
        'Anime Character Pack (5 models)', 'Facial Animation System', 'Hair Dynamics Kit',
        'Combat Animation Set', 'Dialogue Gesture Pack', 'Expression Library',
        
        # Month 3 Environments (30 assets)
        'Modular Village Kit', 'Japanese Architecture Pack', 'Fantasy Forest Bundle', 
        'Lighting Preset Collection', 'Atmospheric Effects', 'Procedural Terrain Tools',
        
        # Month 4 Web/Community (20 assets)
        'Game Website Template', 'Community Dashboard', 'Analytics Integration',
        'Social Media Automation', 'Tutorial Template Pack',
        
        # Month 5 Polish (25 assets)
        'Advanced Shader Library', 'Performance Optimization Tools', 'Quality Assurance Suite',
        'Cross-Platform Porting Kit', 'Advanced Animation Controllers',
        
        # Month 6 Launch (35 assets)  
        'Complete RPG Game Template', 'Marketing Asset Pack', 'Steam Integration Kit',
        'Community Management Tools', 'Educational Course Bundle'
    ],
    'Month Created': [1,1,1,1,1, 2,2,2,2,2,2, 3,3,3,3,3,3, 4,4,4,4,4, 5,5,5,5,5, 6,6,6,6,6],
    'Asset Type': [
        'Tool','Template','Shader','Script','Template',
        'Character','Animation','VFX','Animation','Animation','Animation', 
        'Environment','Environment','Environment','Lighting','VFX','Tool',
        'Web','Web','Script','Script','Educational',
        'Shader','Tool','Tool','Tool','Animation',
        'Game Kit','Marketing','Tool','Tool','Educational'
    ],
    'Realistic Price': [25,15,20,15,10, 120,65,45,85,55,35, 95,85,75,40,50,35, 45,55,30,25,65, 75,45,35,40,55, 250,95,65,45,150],
    'Platform Strategy': [
        'Unity','Unity','Multiple','Unity','GitHub',
        'Multiple','Unity','Multiple','Unity','Unity','Unity',
        'Multiple','Multiple','Multiple','Unity','Multiple','Unity', 
        'Web','Gumroad','Unity','Unity','Gumroad',
        'Multiple','Unity','Unity','Unity','Unity',
        'Steam','Multiple','Unity','Unity','Gumroad'
    ],
    'Monthly Sales Est': [2,1,3,2,1, 3,2,2,2,2,1, 2,2,2,3,2,2, 1,1,2,2,1, 2,2,2,2,2, 1,1,2,2,1]
}

assets_df = pd.DataFrame(specific_assets)

print(f"\n\nFULL ASSET PRODUCTION SCHEDULE (Sample - showing key assets):")
print("-" * 70)
print(assets_df.head(15).to_string(index=False))  # Show first 15 for space

# Calculate realistic totals
total_asset_value = sum(assets_df['Realistic Price'])
monthly_revenue_est = sum(price * sales for price, sales in zip(assets_df['Realistic Price'], assets_df['Monthly Sales Est']))

print(f"\n\nREALISTIC PROJECT TOTALS:")
print("-" * 40)
print(f"Total Individual Asset Values: ${total_asset_value:,}")
print(f"Number of Sellable Assets: {len(assets_df)}")
print(f"Monthly Revenue Potential: ${monthly_revenue_est}")
print(f"Annual Revenue Potential: ${monthly_revenue_est * 12:,}")

# REALITY CHECK based on research data
print(f"\n\nREALITY CHECK (Based on Marketplace Research):")
print("-" * 50)
print("• Unity Asset Store seller with $50 asset: $2000-3000 over few years")
print("• First-year seller: $542 gross revenue ($379 after Unity's 30% cut)")
print("• Successful seller: $525K gross over multiple years ($367K net)")
print("• Average working hourly rate: $20-60 depending on asset success")
print("• Key insight: Quality matters more than quantity")

# Conservative projections
conservative_multiplier = 0.3  # Based on research showing many assets don't sell well
realistic_multiplier = 0.6    # Based on decent success examples  
optimistic_multiplier = 1.0   # Full potential if everything works

print(f"\n\nPROJECTED REVENUE SCENARIOS:")
print("-" * 40)
print(f"Conservative (30% of estimates): ${int(monthly_revenue_est * conservative_multiplier)}/month")
print(f"Realistic (60% of estimates): ${int(monthly_revenue_est * realistic_multiplier)}/month")
print(f"Optimistic (100% of estimates): ${monthly_revenue_est}/month")

# Investment requirements
investment_breakdown = {
    'Investment Category': [
        'Software Licenses (6 months)',
        'Hardware Upgrades',
        'Marketing/Advertising', 
        'Educational Resources',
        'Hosting/Server Costs',
        'Legal/Business Setup'
    ],
    'Cost': [3900, 2000, 1500, 500, 300, 800],
    'Description': [
        'Unity Pro, Maya, Substance, etc.',
        'High-end GPU, RAM upgrades',
        'Asset store promotion, ads',
        'Tutorials, courses, books',
        'Website, analytics, storage',
        'Business registration, contracts'
    ]
}

investment_df = pd.DataFrame(investment_breakdown)
print(f"\n\nINVESTMENT REQUIREMENTS:")
print("-" * 40)
print(investment_df.to_string(index=False))

total_investment = investment_df['Cost'].sum()
realistic_annual_revenue = monthly_revenue_est * realistic_multiplier * 12
roi_ratio = realistic_annual_revenue / total_investment

print(f"\nTotal Investment Required: ${total_investment:,}")
print(f"Realistic Annual Revenue: ${realistic_annual_revenue:,}")  
print(f"ROI Ratio: {roi_ratio:.1f}x return on investment")

print(f"\n\nKEY SUCCESS FACTORS (From Research):")
print("-" * 50)
print("1. QUALITY over quantity - professional presentation crucial")
print("2. NICHE FOCUS - anime/RPG market has demand but less competition")  
print("3. MARKETING - Unity store promotion and sales participation essential")
print("4. CONSISTENCY - regular releases build audience and search ranking")
print("5. SUPPORT - responsive customer service increases ratings/reviews")
print("6. CROSS-PLATFORM - Unity + Unreal + direct sales maximizes reach")

# Save analysis
assets_df.to_csv('shadowed_realms_asset_breakdown.csv', index=False)
pricing_df.to_csv('realistic_asset_pricing_strategy.csv', index=False)
investment_df.to_csv('project_investment_requirements.csv', index=False)

print(f"\n📁 Analysis files saved:")
print("- shadowed_realms_asset_breakdown.csv") 
print("- realistic_asset_pricing_strategy.csv")
print("- project_investment_requirements.csv")