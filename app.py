# app.py

import streamlit as st

# ----- Page Setup -----
st.set_page_config(page_title="Faceless Finance YouTube ROI Calculator", layout="centered")

st.title("💰 Faceless Finance YouTube ROI & Cost Calculator")
st.markdown("""
Estimate your monthly costs, revenue, ROI, and break-even views for a fully automated faceless finance channel.
""")

# ----- User Inputs -----
st.header("📊 Channel & Video Settings")
videos_per_month = st.slider("Videos per Month", 1, 50, 20)
views_per_video = st.slider("Average Views per Video", 1000, 100000, 5000)
cpm_usd = st.slider("CPM ($ per 1000 ad views)", 0.5, 20.0, 3.5)
affiliate_per_video = st.number_input("Affiliate Revenue per Video ($)", 0, 500, 20)

st.header("🛠️ Tool & Automation Costs")
gpt_cost_per_script = st.number_input("OpenAI GPT Cost per Script ($)", 0.01, 1.0, 0.02, 0.01)
tts_cost_per_script = st.number_input("AI Voiceover Cost per Script ($)", 0.1, 5.0, 0.95, 0.05)
video_tool_cost = st.number_input("Video Creation Tool ($/month)", 0, 200, 39, 1)
stock_footage_cost = st.number_input("Stock Footage / Assets ($/month)", 0, 100, 30, 1)
misc_cost = st.number_input("Misc Costs (Storage, Editing) ($/month)", 0, 50, 10, 1)

# ----- Calculations -----
def calculate_costs(videos_per_month, gpt_cost, tts_cost, video_tool, stock, misc):
    total_gpt = videos_per_month * gpt_cost
    total_tts = videos_per_month * tts_cost
    total = total_gpt + total_tts + video_tool + stock + misc
    return round(total, 2)

def calculate_revenue(views_per_video, videos_per_month, cpm, affiliate):
    ad_revenue = (views_per_video * videos_per_month / 1000) * cpm
    affiliate_revenue = videos_per_month * affiliate
    total = ad_revenue + affiliate_revenue
    return round(total, 2)

def calculate_roi(revenue, cost):
    roi = ((revenue - cost) / cost) * 100
    return round(roi, 2)

def break_even_views(cost, cpm, affiliate, videos_per_month):
    total_affiliate = videos_per_month * affiliate
    remaining_cost = cost - total_affiliate
    if remaining_cost <= 0:
        return 0
    views_needed = (remaining_cost / cpm) * 1000
    return int(views_needed)

monthly_cost = calculate_costs(videos_per_month, gpt_cost_per_script, tts_cost_per_script,
                               video_tool_cost, stock_footage_cost, misc_cost)

monthly_revenue = calculate_revenue(views_per_video, videos_per_month, cpm_usd, affiliate_per_video)

roi = calculate_roi(monthly_revenue, monthly_cost)

break_even = break_even_views(monthly_cost, cpm_usd, affiliate_per_video, videos_per_month)

# ----- Output -----
st.header("💵 Results")
st.metric("Monthly Cost ($)", monthly_cost)
st.metric("Estimated Monthly Revenue ($)", monthly_revenue)
st.metric("Estimated ROI (%)", roi)
st.metric("Break-even Views Needed (per month)", break_even)

st.markdown("""
---
**How to Use:**
- Increase videos per month to see scaling impact.
- Adjust views or CPM to simulate YouTube ad revenue.
- Adjust affiliate revenue to see combined income potential.
- Update tool costs if you upgrade AI tools or stock footage subscriptions.
""")
