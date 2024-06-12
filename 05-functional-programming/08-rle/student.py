def rle_encode(data):
    data = iter(data)
    try:
        last_letter = next(data)
        count = 1
        for letter in data:
            if letter == last_letter:
                count += 1
                last_letter = letter
            else:
                yield (last_letter, count)
                last_letter = letter
                count = 1
        yield (last_letter, count)
    except StopIteration:
        pass
        
def rle_decode(data):
    data = iter(data)
    for letter, count in data:
        for _ in range(count):
            yield letter