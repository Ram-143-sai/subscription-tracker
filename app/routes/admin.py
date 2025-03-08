from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models import User, Subscription

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        return "Unauthorized", 403

    user_count = User.query.count()
    subscription_count = Subscription.query.count()

    return render_template('admin.html',
                           user_count=user_count,
                           subscription_count=subscription_count
                           )