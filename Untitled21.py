#!/usr/bin/env python
# coding: utf-8

# In[5]:


import hashlib
import sqlite3

# Initialize SQLite database
conn = sqlite3.connect('url_shortener.db')
c = conn.cursor()

# Create the 'urls' table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, long_url TEXT, short_code TEXT)''')
conn.commit()

def shorten_url(long_url):
    # Generate a unique hash code for the long URL
    short_code = hashlib.md5(long_url.encode()).hexdigest()[:8]

    # Save the URL mapping to the database
    c.execute('''INSERT INTO urls (long_url, short_code) VALUES (?, ?)''', (long_url, short_code))
    conn.commit()

    # Return the short URL
    return f"http://your-domain.com/{short_code}"  # Replace 'your-domain.com' with your actual domain

def get_long_url(short_code):
    # Retrieve the original long URL from the database
    c.execute('''SELECT long_url FROM urls WHERE short_code = ?''', (short_code,))
    result = c.fetchone()
    if result:
        return result[0]
    else:
        return None

# Example usage:
if __name__ == "__main__":
    long_url = "https://www.example.com/very/long/url/to/be/shortened"
    short_url = shorten_url(long_url)
    print("Shortened URL:", short_url)

    # Simulate redirecting from short URL to long URL
    short_code = short_url.split("/")[-1]
    long_url_from_db = get_long_url(short_code)
    if long_url_from_db:
        print("Redirecting to:", long_url_from_db)
    else:
        print("Short URL not found.")


# In[ ]:




