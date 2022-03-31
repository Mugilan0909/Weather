from flask import request,Blueprint
from .controller import create_user,post_user


post_bp1=Blueprint('post_bp1',__name__)


@post_bp1.route('/post', methods=['GET','POST'])
def post_records():
    """Create a user via query string parameters."""
    if request.method == 'POST':

        return create_user()
    if request.method=='GET':

        return post_user()