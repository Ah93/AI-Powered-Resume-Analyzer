import google.generativeai as genai

# Configure Gemini with your API key
genai.configure(api_key="AIzaSyAUgrPIOR1Kokk1f29rvxhkIZom9mToA_o")

# Initialize the model (use correct model name)
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# Call the model with a prompt
response = model.generate_content("in short, write ahmed.")

# Print the response
print(response.text)
