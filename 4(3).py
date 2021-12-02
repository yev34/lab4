text_example = "2 2 3 1 1 3 1 1 5 5 8 4 5 6 9 8 7 4 5 9 8 5 4 1 2 5 8 4 5 3"


def process_text(text: str, sequence_length: int):
    words = text.split()

    start = 0
    sequence_data = {}
    while True:
        sequence = words[start: start+sequence_length]
        sequence_key = ",".join(sequence)
        sequence_data[sequence_key] = sequence_data.get(sequence_key, 0) + 1

        start += 1

        if start + sequence_length > len(words):
            sequence_data_sorted_ten = {k: v for k, v in sorted(sequence_data.items(), key=lambda item: -item[1])}
            return {k: sequence_data_sorted_ten[k] for k in list(sequence_data_sorted_ten)[:10]}


print(process_text(text_example, 2))

