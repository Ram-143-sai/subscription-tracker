from ..forms import SubscriptionForm
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from ..models import Subscription
from .. import db
from datetime import datetime

main_bp = Blueprint('main', __name__)




@main_bp.route('/dashboard')
@login_required
def dashboard():
    # Create form instance
    form = SubscriptionForm()
    subscriptions = Subscription.query.filter_by(user_id=current_user.id).all()
    upcoming_trials = Subscription.query.filter(
        Subscription.user_id == current_user.id,
        Subscription.trial_end >= datetime.now()
    ).all()

    return render_template('dashboard.html',
                           subscriptions=subscriptions,
                           upcoming_trials=upcoming_trials,
                           form=form  # Pass form to template
                           )

@main_bp.route('/add_subscription', methods=['GET', 'POST'])
@login_required
def add_subscription():
    form = SubscriptionForm()
    if form.validate_on_submit():
        subscription = Subscription(
            name=form.name.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            price=form.price.data,
            trial_end=form.trial_end.data,
            cancellation_link=form.cancellation_link.data,
            user_id=current_user.id
        )
        db.session.add(subscription)
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    return render_template('add_subscription.html', form=form)