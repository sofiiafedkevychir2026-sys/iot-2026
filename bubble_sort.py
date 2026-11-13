def cipher(s, k):
    c = ""
    i = 0
    while len(s) > 0:
        i = (i + k - 1) % len(s)
        c += s[i]
        s = s[:i] + s[i + 1:]

    return c


input_str = input("Введіть довільний рядок: ")
key = int(input("Введіть ключ (цифру від 1 до 10): "))

print(f"Заданий рядок: {input_str}")
print(f"Ключ: {key}")
print(f"Шифр: {cipher(input_str, key)}")

print("hello")

