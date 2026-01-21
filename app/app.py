from flask import flask
app = flask(__name__)

@app.route("/")
def home():
    return "Pulumi + Github Actions + Trivy + k8s"
app.run(host="0.0.0.0", port=5000)