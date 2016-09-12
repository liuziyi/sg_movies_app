//Dependencies
var express = require('express');
var router = express.Router();

var moviesJSON = require('../movies.json');

router.get('/:movie_title', function(req,res,next){
	var movie_title = req.params.movie_title;
	var movies = moviesJSON.movies;
	res.render('movieSingle', {
		movie_title: movie_title,
		movies: movies
	});
});

module.exports = router;