from flask import Flask, request, jsonify

app = Flask(__name__)


# Sample recommendation rules
recommendation_data = {
    "Burger": ["Coffee", "Sandwich", "Wrap"],
    "Biryani": ["Sandwich", "Sushi", "Salad"],
    "Pizza": ["Salad", "Sushi", "Sandwich"],
    "Sushi": ["Sandwich", "Biryani", "Taco"]
}


@app.route("/")
def home():
    return jsonify({
        "message": "Food Recommendation API is running"
    })


@app.route("/recommend", methods=["GET"])
def recommend_food():
    food_item = request.args.get("food_item")

    if not food_item:
        return jsonify({
            "error": "Please provide a food_item"
        }), 400

    recommendations = recommendation_data.get(food_item)

    if recommendations is None:
        return jsonify({
            "food_item": food_item,
            "recommendations": []
        })

    return jsonify({
        "food_item": food_item,
        "recommendations": recommendations
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)