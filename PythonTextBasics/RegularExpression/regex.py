import re

# pattern = "fool"
# text = "piyas is the foolest person in the world"
# result = re.search(pattern,text)
# print(result)
# result.span()

# text = "piyas is the foolest person in the world fool the most fool ever existed"
# result = re.findall(pattern,text)
# print(result)
# result.span()#span does not work with findall

text1 = "Mike's new contact is 999-4321-87654, but he rarely picks up."
text2 = "Reach out to Emma at emma.work@mail.com or 222-6789-54321 for details."
text3 = "Order ID: ABC-1234, Customer Support: 777-5555-88888."
text4 = "Liam lives at 45B Baker Street, call 555-3333-22222 to reach him."
text5 = "John said, 'Dial 444-7777-99999 if it's urgent,' before leaving."

# pattern = r'\d\d\d-\d\d\d\d-\d\d\d\d\d'

# result = re.search(pattern, text1)
# if result:
# 	print(result.group())
# else:
# 	print("No match found")
	
# pattern = r'\d{3}-\d{4}-\d{5}' 

# result = re.search(pattern, text2)
# if result:
# 	print(result.group())
# else:
# 	print("No match found")

# pattern = r"(\d{3})-(\d{4})-(\d{5})"

# result = re.search(pattern, text3)
# if result:
# 	print(result.group(1))
# 	print(result.group(2))
# else:
# 	print("No match found")

output1 = re.search(r"man|woman","this is a man")
print(output1.group())
output2 = re.findall(r".at","the cat in the hat sat there")
print(output2)
output3 = re.findall(r"\d$","this ends with a number 2")
print(output3)
output4 = re.findall(r"^\d","1 is the loneliest number")
oitput5 = re.findall(r"[^\d]","there are umbers 34 inside 5 this sentence")
print(oitput5)
output6 = re.findall(r"[^\d]+","there are umbers 34 inside 5 this sentence")
print(output6)

test_phrase = "This is a string! But it has punctuation. How can we remove it?"
output7 = re.findall(r"[^!.? ]+",test_phrase)
print(output7)
print(''.join(output7))
text_hyphen = "The hyper-active cat scattered the food all-0ver the rom."
output8 = re.findall(r'[\w]+-[\w]+',text_hyphen)
print(output8)

