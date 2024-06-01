import tiktoken

def encode(encoder, text):
    tokens = encoder.encode(text)
    print(tokens)
    print(encoder.decode(tokens))
    print('-' * 10)

encoder = tiktoken.encoding_for_model('gpt-3.5-turbo')
print(encoder.name)

encode(encoder, "你好")

encoder = tiktoken.encoding_for_model('gpt-4')
print(encoder.name)

encode(encoder, "你好")


encoder = tiktoken.encoding_for_model('gpt-4o')
print(encoder.name)

encode(encoder, "你好")
