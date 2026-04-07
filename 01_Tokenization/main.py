import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey Bedu Kyaa haal hai ?"
token = enc.encode(text)

print("Encode Token :", token)

decode = enc.decode(token)
print("Decode Token :", decode)