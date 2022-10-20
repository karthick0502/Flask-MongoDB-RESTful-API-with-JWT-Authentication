from spiceblue import app, db
from spiceblue.models import register_user, login_user, add_template, get_all_template, update_template, delete_template
from spiceblue.models import get_single_template, token_required


@app.route('/register', methods=['POST'])
def register():
    return register_user()


@app.route('/login', methods=['POST'])
def login():
    return login_user()


@app.route('/template', methods=['POST'])
@token_required
def add(token):
    return add_template(token)


@app.route('/template', methods=['GET'])
@token_required
def get_all(token):
    return get_all_template(token)


@app.route('/template/<template_id>', methods=['GET'])
@token_required
def get_one(token, template_id):
    return get_single_template(token, template_id)


@app.route('/template/<template_id>', methods=['PUT'])
@token_required
def update(token, template_id):
    return update_template(token, template_id)


@app.route('/template/<template_id>', methods=['DELETE'])
@token_required
def delete(token, template_id):
    return delete_template(token, template_id)