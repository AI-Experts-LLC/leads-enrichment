from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Hello World": "Welcome to the Leads Enrichment app"})


#make a request to get a list of target prospects given a target account
@app.route('/get-prospects-by-account', methods=['POST'])
def get_prospects_by_account():
    data = request.json
    target_account = data.get('target_account')
    return jsonify({"prospects": ["prospect1", "prospect2", "prospect3"]})

# Make a request to get a hospital's original opening year given a hospital name and address
@app.route('/get-hospital-year', methods=['POST'])
def get_hospital_year():
    data = request.json
    hospital_name = data.get('hospital_name')
    hospital_address = data.get('hospital_address')
    return jsonify({"hospital_year": "1900"})

# make a request to get a personalized message given a prospect's linkedin profile url
@app.route('/get-personalized-message-by-linkedin', methods=['POST'])
def get_personalized_message_by_linkedin():
    data = request.json
    prospect_linkedin_profile = data.get('prospect_linkedin_profile')
    return jsonify({"personalized_message": "Hello, I'm interested in your work at [company name]. I'm a [your role] at [your company name] and I'm looking for [specific need]. Would you be open to a quick call to discuss how we can help each other?"})

# make a request to get a personalized message given a prospect's name, title, and company
@app.route('/get-personalized-message-by-name', methods=['POST'])
def get_personalized_message_by_name():
    data = request.json
    prospect_name = data.get('prospect_name')
    prospect_title = data.get('prospect_title')
    prospect_company = data.get('prospect_company')
    return jsonify({"personalized_message": "Hello, I'm interested in your work at [company name]. I'm a [your role] at [your company name] and I'm looking for [specific need]. Would you be open to a quick call to discuss how we can help each other?"})



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
