import re
sample_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. ,
varsha@example.com, varsha.doe@email.co.uk, var_sha[at]example.com
"""
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(pattern, sample_text)
print("Extracted emails:")
for email in emails:
    print(email)
print("\nValidation:")
for email in emails:
    if re.fullmatch(pattern, email):  
        print(f"{email}: Valid")
    else:
        print(f"{email}: Invalid")
