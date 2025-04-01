from flask import *
from database import *
app = Flask(__name__)
app.config['SECRET_KEY'] = "secretKey"


@app.route("/", methods=["GET"])
def get_cafes():
    try:
        cafes = get_all_cafes()
        if not cafes:
            return jsonify({"message": "No cafes found"}), 404
        return jsonify(cafes), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    

@app.route("/add" , methods=['POST'])
def add_cafes():
    try:
        data = request.json
        required_fields = ["name", "map_url", "img_url", "location", "has_sockets", "has_toilet", "has_wifi", "can_take_calls", "seats", "coffee_price"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        name = data["name"]
        map_url = data["map_url"]
        img_url = data["img_url"]
        location = data["location"]
        has_sockets = data["has_sockets"]
        has_toilet = data["has_toilet"]
        has_wifi = data["has_wifi"]
        can_take_calls = data["can_take_calls"]
        seats = data["seats"]
        coffee_price = data["coffee_price"]
        
        result = add_cafe(name, map_url, img_url, location, has_sockets, has_toilet, has_wifi, can_take_calls, seats, coffee_price)

        return jsonify({"message": "Cafe added successfully!"}), 201
    except Exception as e :
        return jsonify({"error":f"Error occurred while adding the data{str(e)}"}), 400
    
    
    
@app.route("/delete",methods=["POST"])
def delete_cafes():
    data = request.json #its  property not function
    
    try:
        required_fields = ["cafe_id"]
        for field  in required_fields:
            if field not in data:
                return jsonify({
                    "error":"Missing the required field named cafe_id "
                })
        cafe_id = data["cafe_id"]
        result = delete_cafe(cafe_id)
        return jsonify(result),200
    except Exception as e :
        return jsonify({
            "error":f"an error occurred {str(e)}"
        }) , 400

        
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8000')