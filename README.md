
import pyshorteners

def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(url)
        return shortened_url
    except Exception as e:
        print("Error: ", e)
        return None

if __name__ == "__main__":
    long_url = input("Enter the URL to shorten: ")
    shortened_url = shorten_url(long_url)
    if shortened_url:
        print("Shortened URL:", shortened_url)
