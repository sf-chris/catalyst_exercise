from flask import Flask, jsonify, abort, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restless import APIManager

"""
instantiates the app, loads config and creates database"""
app = Flask(__name__) 
app.config.from_pyfile('config.py') 
db = SQLAlchemy(app) 


"""
Classes for the database"""
class People(db.Model):
       
    __tablename__ = 'people' 
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def __repr__(self):        
        return '<People %r>' % (self.name)
    

class Movie(db.Model):
    
    __tablename__ = 'movies'
    
    id = db.Columns(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    length = db.Column(db.Integer)
    
    def __init__(self, id, title, length):
        self.id = id
        self.title = title
        self.length = length
    
    def __repr__(self):
        return '<Title %r>' % self.title
 
    
class Votes(db.Model):
    
    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    #TODO The constraint on people voting on only one movie once 
    #TODO figure out how to do init for a vote
    
   
db.createAll()


"""
Handles requests for GET"""
@app.route('/movies', methods = ['GET'])
def get_movies():
    return jsonify({'movies': Movie.query.all()})
    
@app.route('/people', methods = ['GET'])
def get_people():
    return jsonify({'people': People.query.all()})

@app.route('/votes', methods = ['GET'])
def get_votes():
    return jsonify({'votes': Votes.query.all()})

"""
Handles requests for POST"""

    
    