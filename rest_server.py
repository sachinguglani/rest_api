import connexion
from flask import (
    Flask,
    render_template
)


app = connexion.App(__name__, specification_dir='./')

# swagger.yml  -> configure the endpoints
app.add_api('swagger.yml')


@app.route('/')
def home():

    return render_template('scratch.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)