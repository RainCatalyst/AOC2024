print(sum([int(x.group(1))*int(x.group(2)) for x in __import__('re').finditer(r"mul\((\d{1,3}),(\d{1,3})\)", __import__('re').sub(r"don't\(\)([\S\s]*?)(?=do\(\)|\Z)", '', input()))]))
