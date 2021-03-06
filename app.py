import os
import yaml
import joblib
import numpy as np
from prediction_service import prediction
from flask import Flask, render_template, request, jsonify

webapp_path = "webapp"
static_dir = os.path.join(webapp_path, "static")
template_dir = os.path.join(webapp_path, "templates")

app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data_req = dict(request.form)
                data_req = {col: float(val) for col, val in data_req.items()}
                response = prediction.form_response(data_req)
                return render_template("index.html", response=response)
            elif request.json:
                response = prediction.api_response(request.json)
                return jsonify(response)
        except Exception as e:
            error = {"error": e}
            # error = {"error": "Something went wrong!! Try again!!"}
            return render_template("404.html", error=error)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
