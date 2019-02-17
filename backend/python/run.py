from flask import Flask, render_template, jsonify, request


from vueflask.core.aws.s3 import S3Client


app = Flask(__name__,
            static_folder="../../frontend/dist/static",
            template_folder="../../frontend/dist")


@app.route('/api/list')
def list():
    s3 = S3Client(profile = 'vueflasksample', bucket = 'vueflasksample')
    prefix = request.args.get('prefix')
    response = {
        'files': s3.getList(prefix = prefix)
    }
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
