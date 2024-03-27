from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"student_number": "200559680"})

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming JSON request
    req = request.get_json(force=True)

    # Extract the intent name from the request
    intent_name = req.get("queryResult", {}).get("intent", {}).get("displayName", "")

    # Initialize a response dictionary
    response = {"fulfillmentMessages": []}

    # Handle the chocolateBrands intent
    if intent_name == "chocolate_brands":
        # List of chocolate brands
        chocolate_brands = ["Cadbury", "Lindt", "Kitkat", "Mars", "Snickers"]  # Capitalize Snickers
        # Building the response text
        response_text = "List of chocolate brands available in the market are: \n" + "\n".join([f"{i+1} - {item}" for i, item in enumerate(chocolate_brands)])  # Corrected variable name

        # Set the response in the fulfillmentMessages format
        response["fulfillmentMessages"].append({
            "text": {"text": [response_text]}
        })

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
