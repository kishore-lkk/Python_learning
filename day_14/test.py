test_cases = [
    {},                          # Case 1: SameSite key missing entirely
    {"SameSite": "None"},        # Case 2: explicitly SameSite=None (insecure)
    {"SameSite": "Lax"},         # Case 3: SameSite=Lax
    {"SameSite": "Strict"},      # Case 4: SameSite=Strict
]

for rest in test_cases:
    value = rest.get("SameSite")
    result = "present" if value != "None" and value != None else "missing"
    print(f"rest={rest} -> get()={value!r} -> your_code_says={result}")