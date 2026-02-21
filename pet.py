import requests
import os

# CONFIGURATION
USERNAME = "kabishanan" 

def get_commit_count():
    try:
        url = f"https://api.github.com/users/{USERNAME}/events"
        response = requests.get(url).json()
        # Filters for PushEvents (actual code updates)
        commits = [e for e in response if e['type'] == 'PushEvent']
        return len(commits)
    except:
        return 0

def generate_svg(commit_count):
    # Logic: More commits = happier pet!
    if commit_count > 5:
        color, eyes, status = "#FFD700", "O O", "GOD MODE"
    elif commit_count > 0:
        color, eyes, status = "#7ed321", "^ ^", "Happy & Productive"
    else:
        color, eyes, status = "#9b9b9b", "- -", "Sleeping..."

    svg_template = f"""
    <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
      <circle cx="100" cy="100" r="80" fill="{color}" stroke="black" stroke-width="3"/>
      <text x="100" y="95" font-family="Arial" font-size="25" text-anchor="middle">{eyes}</text>
      <text x="100" y="130" font-family="Arial" font-size="14" text-anchor="middle" font-weight="bold">{status}</text>
      <text x="100" y="155" font-family="Arial" font-size="12" text-anchor="middle">Commits today: {commit_count}</text>
    </svg>
    """
    with open("pet.svg", "w") as f:
        f.write(svg_template)

if __name__ == "__main__":
    count = get_commit_count()
    generate_svg(count)
