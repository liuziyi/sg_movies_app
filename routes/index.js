//Dependencies
var express = require('express');
var router = express.Router();

var moviesJSON = require('../movies.json');

router.get('/', function(req,res,next){
	var movies = moviesJSON.movies;
	res.render('home', {title: 'NOW SHOWING' ,movies:movies});
});

module.exports = router;