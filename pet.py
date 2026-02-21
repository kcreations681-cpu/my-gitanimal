import requests
import os

# CONFIGURATION
USERNAME = "kcreations681-cpu" 

def get_commit_count():
    try:
        url = f"https://api.github.com/users/{USERNAME}/events"
        response = requests.get(url).json()
        commits = [e for e in response if e['type'] == 'PushEvent']
        return len(commits)
    except:
        return 0

def generate_svg(commit_count):
    # Mood Logic: Colors change based on work!
    if commit_count > 5:
        box_color, face = "#ff9a9e", "◕ ‿ ◕" # Pink box
    elif commit_count > 0:
        box_color, face = "#f6d365", "◕ ◡ ◕" # Yellow box
    else:
        box_color, face = "#cfd9df", "◡ _ ◡" # Grey box

    svg_template = f"""
    <svg width="400" height="250" xmlns="http://www.w3.org/2000/svg">
      <style>
        @keyframes wave {{
          0%, 100% {{ transform: rotate(0deg); }}
          50% {{ transform: rotate(-20deg); }}
        }}
        @keyframes bounce {{
          0%, 100% {{ transform: translateY(0); }}
          50% {{ transform: translateY(-5px); }}
        }}
        .arm {{ animation: wave 1.5s infinite ease-in-out; transform-origin: 130px 110px; }}
        .cat-head {{ animation: bounce 2s infinite ease-in-out; }}
        .text {{ font-family: 'Comic Sans MS', cursive, sans-serif; fill: #ff4757; font-weight: bold; }}
      </style>

      <text x="130" y="40" class="text" font-size="24">Hello Everyone! ✨</text>

      <g class="cat-head">
        <path d="M80,120 Q80,60 140,60 Q200,60 200,120" fill="white" stroke="#5d4037" stroke-width="3"/>
        <path d="M80,80 L60,40 L110,65 Z" fill="white" stroke="#5d4037" stroke-width="3"/> <path d="M200,80 L220,40 L170,65 Z" fill="white" stroke="#5d4037" stroke-width="3"/> <text x="140" y="105" font-size="25" text-anchor="middle">{face}</text> </g>

      <path class="arm" d="M85,110 Q60,90 50,110 T75,130" fill="white" stroke="#5d4037" stroke-width="3"/>

      <rect x="60" y="120" width="160" height="100" fill="{box_color}" stroke="#5d4037" stroke-width="4" rx="10"/>
      <path d="M60,120 L30,90 M220,120 L250,90" stroke="#5d4037" stroke-width="4"/> <rect x="240" y="140" width="140" height="40" rx="10" fill="#f1f2f6"/>
      <text x="310" y="165" font-family="Arial" font-size="12" text-anchor="middle" fill="#2f3542">Commits Today: {commit_count}</text>
    </svg>
    """
    with open("pet.svg", "w", encoding="utf-8") as f:
        f.write(svg_template)

if __name__ == "__main__":
    count = get_commit_count()
    generate_svg(count)
