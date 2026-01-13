import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters

# Allowed domain
ANIMEPAHE_DOMAINS = ["animepahe.si", "animepahe.com"]

def extract_pahe_links(url):
    """Extract download links, name, quality, and size from AnimePahe page."""
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except Exception:
        return []

    soup = BeautifulSoup(res.text, "html.parser")
    download_div = soup.find("div", id="pickDownload")
    if not download_div:
        return []

    result = []
    for a in download_div.find_all("a"):
        text = a.text.strip()  # e.g., Amazon · 360p (54MB)
        try:
            name, rest = text.split("·")
            quality, size = rest.strip().split("(")
            size = size.replace(")", "")
            result.append({
                "name": name.strip(),
                "quality": quality.strip(),
                "size": size.strip(),
                "url": a['href']
            })
        except Exception:
            continue
    return result

@Client.on_message(filters.command("p"))
async def pahe_links(client, message):
    """
    Command: /p <AnimePahe link>
    Only responds if link matches AnimePahe domains.
    """
    if len(message.command) < 2:
        return  # No link provided, ignore

    url = message.command[1].strip()

    # Only process AnimePahe domain links
    if not any(domain in url for domain in ANIMEPAHE_DOMAINS):
        return  # Ignore non-animepahe links

    links = extract_pahe_links(url)
    if not links:
        return await message.reply("❌ Could not find download links!")

    text = "📥 **Download Links:**\n\n"
    for l in links:
        text += f"**{l['name']} · {l['quality']} ({l['size']})**\n{l['url']}\n\n"

    await message.reply(text)
