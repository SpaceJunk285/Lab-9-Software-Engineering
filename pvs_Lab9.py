def encode(password):
    encoded = ""
    for i in str(password):
        encoded += str(int(i) + 1)
    return encoded

if __name__ == '__main__':
    print(encode(1112))