const generateBtn = document.getElementById('generateBtn');
const promptInput = document.getElementById('prompt');
const maxLengthInput = document.getElementById('maxLength');
const generatedTextDiv = document.getElementById('generatedText');

generateBtn.addEventListener('click', async () => {
    const prompt = promptInput.value;
    const maxLength = parseInt(maxLengthInput.value, 10);

    if (prompt.trim() === '') {
        generatedTextDiv.innerText = 'Please enter a valid prompt.';
        return;
    }

    if (isNaN(maxLength) || maxLength < 1 || maxLength > 10000) {
        generatedTextDiv.innerText = 'Please enter a valid max length (between 1 and 10000).';
        return;
    }

    try {
        // Send the prompt and max_length to the Flask backend API
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: prompt, max_length: maxLength })
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const data = await response.json();

        // Display the generated text or handle errors
        if (data.conversation) {
            generatedTextDiv.innerText = data.conversation.join('\n\n');
        } else {
            generatedTextDiv.innerText = 'No text generated. Please try again.';
        }

    } catch (error) {
        console.error('Error generating text:', error);
        generatedTextDiv.innerText = 'An error occurred while generating text.';
    }
});
