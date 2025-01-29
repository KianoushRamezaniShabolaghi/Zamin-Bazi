from transformers import T5Tokenizer, T5ForConditionalGeneration

def encode_decode(input_text, model_name="T5-3B"):
    # Load pre-trained model and tokenizer
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Encoding the input text
    input_ids = tokenizer.encode("translate English to French: " + input_text, return_tensors="pt")

    # Generating the output (decoding)
    output_ids = model.generate(input_ids, max_length=50, num_beams=4, early_stopping=True)
    decoded_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return decoded_text

# Example usage
if __name__ == "__main__":
    input_text = "I love programming."
    output_text = encode_decode(input_text)
    print("Input:", input_text)
    print("Output:", output_text)
