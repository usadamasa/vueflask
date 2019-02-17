from flask import Flask, render_template, jsonify
from random import randint


from vueflask.core.aws.s3 import S3Client


app = Flask(__name__,
            static_folder="../../frontend/dist/static",
            template_folder="../../frontend/dist")


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

@app.route('/api/list')
def list():
    s3 = S3Client(profile = 'vueflasksample', bucket = 'vueflasksample')
    response = {
        'lastModified': s3.getList('hoge')
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
