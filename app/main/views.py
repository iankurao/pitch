from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitches
from flask_login import login_required
from .forms import UpdateProfile,ReviewForm,WritePitch
from .. import db



@main.route("/")
def index():
    title="Pitch"
    message="Home of ideas, Where ideas are born"
    top=Pitches.query.all();
    pitch=Pitches.query.filter_by(categ="AI").all()
    pitch1=Pitches.query.filter_by(categ="R").all()
    pitch2=Pitches.query.filter_by(categ="D").all()
    pitch3=Pitches.query.filter_by(categ="IOT").all()
    top.reverse()
    top_pitch=top[0:4]
    return render_template("index.html",title=title,message=message,pitch=pitch,top_pitch=top_pitch,pitch1=pitch1,pitch2=pitch2,pitch3=pitch3)




@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

     
    pitch=Pitches.query.filter_by(author=uname).all()
    title=uname
    return render_template("profile/profile.html", user = user, pitch=pitch, title=title)


'''
new Pitch idea
'''

@main.route("/<uname>",methods=["GET","POST"])
@login_required
def new_pitch(uname):
    uname=uname
    user=User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form=WritePitch()
    if form.validate_on_submit():
        new_pitch=Pitches(pitch=form.pitch.data,title=form.title.data,author=uname,categ=form.categ.data)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for(".index"))


    title="new Pitch"
    return render_template("pitch.html",new_review=form,title=title)

'''
review
'''

@main.route("/pitch/new/review/<int:id>",methods=["GET","POST"])
@login_required
def review(id):
    pitch_id=id
    pitch=Pitches.query.all();
    title="Write a comment"
    form=ReviewForm()
    if form.validate_on_submit():
        title=form.title.data
        comments=form.comments.data

        #update this variables
        review=Comments(pitch_id=id,pitch_title=title,comments=comments,user=current_user)

        #save
        review.save_comment()
        return redirect(url_for('.review',id=pitch_id))

    '''
    query Comments database table
    '''
    all_comments=Comments.query.filter_by(pitch_id=id).all()

    return render_template("new_review.html",pitch=pitch,id=pitch_id,title=title,comment_form=form,all=all_comments)

