import urllib.request

def print_txt_from_url(url):
    with urllib.request.urlopen(url) as response:
        content = response.read().decode('utf-8')
        print(content)

if __name__ == '__main__':
    n = input().strip()
    url = f"https://raw.githubusercontent.com/your-id/your-repo/main/festival{n}.txt"
    print_txt_from_url(url)
