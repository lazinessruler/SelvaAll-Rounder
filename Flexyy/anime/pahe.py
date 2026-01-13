import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters

ANIMEPAHE_DOMAINS = (
    "animepahe.si",
    "animepahe.com",
    "animepahe.org"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://animepahe.si/",
}

def extract_pahe_links(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
    except Exception:
        return []

    soup = BeautifulSoup(r.text, "lxml")

    download_div = soup.find("div", id="pickDownload")
    if not download_div:
        return []

    results = []
    for a in download_div.find_all("a", href=True):
        text = a.get_text(strip=True)
        href = a["href"]

        # Example text: Amazon · 360p (54MB)
        try:
            name, rest = text.split("·")
            quality, size = rest.strip().split("(")
            size = size.replace(")", "").strip()
        except Exception:
            continue

        results.append({
            "name": name.strip(),
            "quality": quality.strip(),
            "size": size,
            "url": href
        })

    return results


@Client.on_message(filters.command("p"))
async def pahe_handler(client, message):
    if len(message.command) < 2:
        return

    url = message.command[1].strip()

    if not any(d in url for d in ANIMEPAHE_DOMAINS):
        return  # ignore non-animepahe links

    links = extract_pahe_links(url)
    if not links:
        return await message.reply("❌ Download links not found.")

    text = "📥 **AnimePahe Download Links**\n\n"
    for i, l in enumerate(links, 1):
        text += (
            f"**{i}. {l['name']} · {l['quality']} ({l['size']})**\n"
            f"{l['url']}\n\n"
        )

    await message.reply(text, disable_web_page_preview=True)
