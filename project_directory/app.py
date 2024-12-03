from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM

# Initialize Flask app
app = Flask(__name__)

# Initialize the tokenizer and model for Model 1 (GPT-2)
tokenizer_1 = AutoTokenizer.from_pretrained("gpt2")
model_1 = AutoModelForCausalLM.from_pretrained("gpt2").to('cpu')

# Initialize the tokenizer and model for Model 2 (GPT-2)
tokenizer_2 = AutoTokenizer.from_pretrained("gpt2")
model_2 = AutoModelForCausalLM.from_pretrained("gpt2").to('cpu')

# Function to generate text from a given model and prompt
def generate_response(model, tokenizer, prompt, max_tokens=50, temperature=0.9):
    inputs = tokenizer(prompt, return_tensors='pt').to(model.device)
    outputs = model.generate(
        inputs['input_ids'],
        max_new_tokens=max_tokens, 
        temperature=temperature, 
        do_sample=True,
        attention_mask=inputs['attention_mask'],
        pad_token_id=tokenizer.eos_token_id  
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

@app.route('/')
def index():
    return render_template('index.html')

# API route for generating a conversation between two models
@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json.get('prompt')
    max_length = request.json.get('max_length', 50)
    
    if not prompt:
        return jsonify({'error': 'Please provide a prompt'}), 400
    
    conversation = [f"User: {prompt}"]
    
    # Start the conversation with Model 1 (GPT-2)
    response_1 = generate_response(model_1, tokenizer_1, prompt, max_tokens=max_length)
    conversation.append(f"Model 1: {response_1}")
    
    # Now Model 2 (DistilGPT-2) responds to Model 1's output
    response_2 = generate_response(model_2, tokenizer_2, response_1, max_tokens=max_length)
    conversation.append(f"Model 2: {response_2}")
    
    # Return the conversation
    return jsonify({'conversation': conversation})

if __name__ == "__main__":
    app.run()