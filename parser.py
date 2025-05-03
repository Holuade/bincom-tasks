from bs4 import BeautifulSoup
import re

def extract_colors_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    rows = soup.find_all("tr")[1:]  # skip header
    all_colors = []

    for row in rows:
        colors_raw = row.find_all("td")[1].text.strip().upper().replace("BLEW", "BLUE")
        colors_clean = [color.strip() for color in re.split(r",\s*", colors_raw)]
        all_colors.extend(colors_clean)

    return all_colors
