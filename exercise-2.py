# Functioninator 8000
## Task

### Input --> Output 1
text = str(input("Enter the single word text 'Shrink': ", ))
text_length = len(text)
print("Text length:", text_length)
text_end = text[-1]
print("Text ends at:", text_end)
while text_end == "k":
    print(text + "inator" +(" ")+ str(len(text)) + "000")
    break

### Input --> Output 2
text = str(input("Enter the single word text 'Doom': ", ))
text_length = len(text)
print("Text length:", text_length)
text_end = text[-1]
print("Text ends at:", text_end)
while text_end == "m":
    print(text + "inator" +(" ")+ str(len(text)) + "000")
    break

### Input --> Output 3
text = str(input("Enter the single word text 'EvilClone': ", ))
text_length = len(text)
print("Text length:", text_length)
text_end = text[-1]
print("Text ends at:", text_end)
while text_end == "e":
    print(text + "-inator" +(" ")+ str(len(text)) + "000")
    break
