from flask import Flask, request, jsonify, render_template
import numpy as np
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        print("data is below = ",data)
        print("type of data = ",type(data))
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        user_id = data.get("userId")
        user_type = data.get("userType")
        user_age = data.get("userAge")

        user_key = "u_"
        if user_type == "new":
            user_key += "n_"
        else:
            user_key += "r_"
        
        if user_age < 20:
            user_key += "a1"
        elif ((user_age >= 20) and (user_age <= 40)):
            user_key += "a2"
        else:
            user_key += "a3"
        
        print("fetching user key = ",user_key)
        # add logging to .log file
        fetch_redis_key = redis_client.get(user_key)
        if fetch_redis_key:
            fetch_redis_value = fetch_redis_key.decode('utf-8')
        print("redis value fetched = ",fetch_redis_value)
        
        return jsonify({'print id': user_id, 'print type': user_type, 'print age' : user_age}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

# gunicorn -w 4 -b 0.0.0.0:8000 runapp:app
# SET "u_r_a1" '{"p1" : [1, 1], "p2" : [1, 1]}' (_n_a1)
# curl -X POST http://localhost:8000 -H "Content-Type: application/json" -d '{"userType": "new", "userId" : 232421, "userAge" : 43}'
# this