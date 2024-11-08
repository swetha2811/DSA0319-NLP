import wikipediaapi
user_agent = "My Wikipedia Scraper/1.0"
wiki_wiki = wikipediaapi.Wikipedia('en', user_agent=user_agent)
sentences = [
    "apple is a leading tech company.",
    "i love apples as a fruit.",
    "python is a popular programming language.",
    "the python is a non-venomous snake"
]
wiki_wiki = wikipediaapi.Wikipedia('en')
for sentence in sentences:
    words = sentence.split()
    for word in words:
        if word[0].isupper():
            page = wiki_wiki.page(word)
            if page.exists():
                print(f"Entity mention '{word}' corresponds to Wikipedia page: {page.fullurl}")
            else:
                print(f"No Wikipedia page found for entity mention '{word}'")
