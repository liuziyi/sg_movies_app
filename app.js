//Dependencies
var express = require('express');
var path = require('path');

var app = express();

app.set('view engine', 'ejs');

app.use(express.static(path.join(__dirname, 'public')));


//Routes
var indexRoute = require('./routes/index');
var movieSingleRoute = require('./routes/movieSingle');
var notFoundRoute = require('./routes/notFound');

app.use('/movies', movieSingleRoute);
app.use('/', indexRoute);
app.use('*', notFoundRoute);


app.listen(process.env.PORT || 3000);

// app.listen(3000);
// console.log('Listening on port 3000');