known_words = set([input().lower() for _ in range(int(input()))])
text_words = set()
[text_words.update(input().lower().split()) for _ in range(int(input()))]

[print(s) for s in text_words-known_words]