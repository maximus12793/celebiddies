var mysql = require('mysql');

console.log("HERE I AM RUNNING \n\n\n")
var connection = mysql.createConnection({
    host: 'myinstance.crvhxo7lbemw.us-west-2.rds.amazonaws.com',
    user: 'root',
    password: 'swaglords',
    database: 'mysql',
    port: 3306
});

connection.connect();

console.log("connection works!!!");

var query = connection.query(
    'show databases;', function(err, result, fields){
        console.log('result: ', result);
        if(err) throw err;

    });
connection.end();

console.log("finito");
