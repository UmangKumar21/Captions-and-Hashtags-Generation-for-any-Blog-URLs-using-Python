pip install nltk
import requests
from bs4 import BeautifulSoup
import re
def fetch_blog_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        blog_text = ' '.join([re.sub(r'<.+?>', '', str(para)) for para in paragraphs])
        return blog_text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the blog content: {e}")
        return None
def generate_captions(blog_text, max_chars_per_caption=100):
    words = blog_text.split()
    captions = []
    current_caption = ""

    for word in words:
        if len(current_caption) + len(word) + 1 <= max_chars_per_caption:
            current_caption += " " + word
        else:
            captions.append(current_caption.strip())
            current_caption = word

    if current_caption:
        captions.append(current_caption.strip())

    return captions
def generate_hashtags(blog_text, max_hashtags=20):
    import nltk
    from nltk.tokenize import word_tokenize
    from nltk.corpus import stopwords
    from nltk.probability import FreqDist

    nltk.download("punkt")
    nltk.download("stopwords")
    words = word_tokenize(blog_text)
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords.words("english")]
hashtags = [word.strip("#.,!?") for word in words if word.startswith("#")]
additional_hashtags = [word for word in words if word not in hashtags and not word.startswith("#")]
hashtags.extend(additional_hashtags)
fdist = FreqDist(filtered_words)
common_words = fdist.most_common(max_hashtags)
hashtags = [word for word, _ in common_words]
return hashtags
blog_url = "https://nec.edu.in/blog/"
blog_content = fetch_blog_content(blog_url)

if blog_content:
    captions = generate_captions(blog_content)
    print("Captions:")
    for i, caption in enumerate(captions):
        print(f"Caption {i+1}: {caption}")

    hashtags = generate_hashtags(blog_content)
    print("\nHashtags:")
    for tag in hashtags:
        print(f"#{tag}")
else:
    print("Failed to fetch blog content.")
