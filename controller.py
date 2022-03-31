from flask import request, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, post
from geoalchemy2 import functions

def create_user():
    lat=request.args.get('lat')
    lon=request.args.get('lon')
    latlon1 = 'POINT('+lon+' '+lat+')'
    post1 = request.args.get('post')
    if post1 and lat and lon:
            new_post = post(
                latlon=latlon1,
                lat=lat,
                lon=lon,
                post=post1,
                created=dt.now(),
            )
    else:
        return '----------------Fail ------------\n Some Error may be input for api'
    db.session.add(new_post)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return make_response(f" successfully created!{type(latlon1)}")

def post_user():
        lat=request.args.get('lat')
        lon=request.args.get('lon')
        page=int(request.args.get('page'))
        if lat and lon and page:
            result = post.query.order_by(functions.ST_Distance(post.latlon, 'POINT('+lon+' '+ lat+')')).paginate(page, per_page=10).items
            results = [
                {
                    "post": post2.post,
                    "datetime": post2.created,
                    "latitude":post2.lat,
                    "longitude":post2.lon
                } for post2 in result]
        else:
            return "Check input"
        return {"count": len(results), "post": results}