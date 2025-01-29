from transformers import GPT2Tokenizer, GPT2LMHeadModel

def summarize_text_with_gpt(input_text, model_name="gpt2", top_k=50, temperature=1.0):
    # Load pre-trained GPT model and tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Encode the input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    print("Input IDs:", input_ids)
    
    # Generate text using top-k sampling
    output_ids = model.generate(
        input_ids,
        max_length=150,
        top_k=top_k,
        temperature=temperature,
        do_sample=True,
        early_stopping=True
    )
    print("Output IDs:", output_ids)
    
    # Decode the generated output
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
    summary = summarize_text_with_gpt(input_text)
    print("Summary:", summary)
