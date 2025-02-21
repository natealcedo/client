from flask import Flask, render_template
import ssl

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("cert.pem", "key.pem")  # Load SSL certificate and key
    app.run(host="0.0.0.0", port=443, ssl_context=context)
