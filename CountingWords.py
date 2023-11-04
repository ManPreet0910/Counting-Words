user_intro=(input("Enter your introduction"))
print(user_intro)

word_count=1
character_count=0
for chracter in user_intro:
    character_count = character_count + 1
    if (chracter==" "):
        word_count=word_count + 1

print(word_count)