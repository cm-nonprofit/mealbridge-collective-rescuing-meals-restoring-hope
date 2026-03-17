import os, json, urllib.request, urllib.parse, ssl, random

UNSPLASH_API_KEY = 'buhc7QncQ0ZMcCjMWpJhQ-NIiIjmoNeFYE4IyOiCbVA'
ASSETS = 'assets'

ssl_ctx = ssl.create_default_context()


def download_image(query, filename, orientation='landscape'):
    os.makedirs(ASSETS, exist_ok=True)
    try:
        params = urllib.parse.urlencode({'query': query, 'per_page': 10, 'orientation': orientation})
        url = f'https://api.unsplash.com/search/photos?{params}'
        req = urllib.request.Request(url, headers={'Authorization': f'Client-ID {UNSPLASH_API_KEY}'})
        with urllib.request.urlopen(req, context=ssl_ctx, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        if data.get('results'):
            pick = random.choice(data['results'])
            image_url = pick['urls']['regular']
            with urllib.request.urlopen(image_url, context=ssl_ctx, timeout=15) as img_resp:
                img_data = img_resp.read()
            path = os.path.join(ASSETS, filename)
            with open(path, 'wb') as f:
                f.write(img_data)
            print(f"Downloaded: {filename} (query: {query})")
            return True
    except Exception as e:
        print(f"Failed {filename} ({query}): {e}")
    return False


# Food insecurity / meal rescue nonprofit images
download_image('food donation volunteer community', 'hero-bg.jpg')
download_image('meal preparation kitchen cooking', 'program1.jpg')
download_image('fresh produce farm basket harvest', 'program2.jpg')
download_image('mobile app smartphone delivery', 'program3.jpg')
download_image('homeless shelter meal serving people', 'program4.jpg')
download_image('grocery store food surplus abundance', 'impact1.jpg')

print("Done.")
