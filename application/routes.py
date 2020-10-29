from flask import current_app as app
from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from .models import db, Details
import os
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


@app.route('/', methods=['GET', 'POST'])
def upload():
    
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

    # handle image upload from Dropszone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)
            
            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename    
            )

            # append image urls
            file_urls.append(photos.url(filename))
            
        session['file_urls'] = file_urls
        return "uploading..."
    # return dropzone template on GET request    
    return render_template('index.html')


@app.route('/data', methods=['GET','POST'])
def data():
    if request.method == 'POST':
        name = request.form["name"]
        tye = request.form["type"]
        images = session['file_urls']
        duration = request.form["duration"]
        dicription = request.form["discription"]
        prise = request.form["prise"]
        tags = request.form["tags"]
        slug = request.form["slug"]
        data = Details(name=name,type=tye,filename=str(images), duration=duration,dicription=dicription,prise=prise,tags=tags,slug=slug)
        db.session.add(data)
        db.session.commit()
        print(name,tye,dicription)
        return redirect(url_for('data'))
    return render_template('index.html')

@app.route('/result')
def results():
    
    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))

    data = Details.query.all()
    print(data)   
    
    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    print(file_urls)
    session.clear()
    
    return render_template('results.html', file_urls=file_urls)
