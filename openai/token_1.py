import tiktoken

encoder = tiktoken.encoding_for_model('gpt-3.5-turbo')
print(encoder.name)

encoder = tiktoken.encoding_for_model('gpt-4')
print(encoder.name)

encoder = tiktoken.encoding_for_model('gpt-4o')
print(encoder.name)
