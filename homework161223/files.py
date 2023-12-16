# with open("ishodnik.txt", "r") as input_file:
# with open("noviyfile.txt", "w") as output_file:
# for line in input_file:
# words = line.split()
# long_words = [word for word in words if len(word) >= 7]
# output_file.write(" ".join(long_words) + "\n")

# import re
#
# with open('text.txt', 'r') as f_text, open('words.txt', 'r') as f_words, open('results.txt', 'w') as f_results:
#     f_results.write(re.sub(re.sub(r"(?m)\s+", "|", f_words.read()), '', f_text.read()))

# with open('zadacha3.txt', 'w+', encoding='UTF-8') as f:
#     a = ' '.join(i for i in iter(input, 'quit'))
#     f.write(a + '\n')

# flag = False
# for a in iter(input, "quit"):
#     a = a if a.endswith('.txt') else a + '.txt'
#     with open(a, 'r') as f:
#         if flag:
#             s &= set(f.read())
#         else:
#             s = set(f.read())
#             flag = True
# print(s)

# names = []
# texts = []
#
# while (a := input()) != 'quit':
#     names.append(a)
#
# for i in names:
#     with open(f'{i}.txt', 'r') as f:
#         texts.append(set(f.read()))
# s = set(texts[0])
# for i in range(1, len(texts)):
#     s = s.intersection(texts[i])
# print(s)