from transformers import T5Tokenizer, T5ForConditionalGeneration

def summarize_text(input_text, model_name="t5-small"):
    # Load pre-trained model and tokenizer
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    # Prepare the input text for summarization
    input_ids = tokenizer.encode("summarize: " + input_text, return_tensors="pt", max_length=512, truncation=True, legacy=True)
    print(input_ids)
    # Generate the summary
    output_ids = model.generate(input_ids, max_length=150, num_beams=4, early_stopping=True)
    print(output_ids)
    summary = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return summary

# Example usage
if __name__ == "__main__":
    input_text = (
        "Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed "
        "to think like humans and mimic their actions. The term may also be applied to any machine that exhibits "
        "traits associated with a human mind such as learning and problem-solving. The ideal characteristic of "
        "artificial intelligence is its ability to rationalize and take actions that have the best chance of achieving "
        "a specific goal."
    )
    summary = summarize_text(input_text)
    #print("Input Text:", input_text)
    print("Summary:", summary)
    