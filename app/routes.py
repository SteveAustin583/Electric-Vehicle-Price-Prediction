from flask import render_template, request, jsonify
# , Environment, PackageLoader, select_autoescape
from app import app
from app.model import predict_price
from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def index():
    env = Environment(
        loader=PackageLoader("app"),
        autoescape=select_autoescape()
    )
    template = env.get_template("index.html")
    return render_template(template)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    
    # Convert the form data into the correct format for prediction
    features = [
        data['county'],
        data['city'],
        data['zip_code'],
        data['model_year'],
        data['make'],
        data['model'],
        data['ev_type'],
        data['cafv_eligibility'],
        data['legislative_district']
    ]
    
    # Get the prediction result
    price = predict_price(features)
    
    return jsonify({'predicted_price': price})

