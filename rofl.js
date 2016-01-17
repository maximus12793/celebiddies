var mysql = require('mysql');
new mysql.createConnection({
    host: 'myinstance.crvhxo7lbemw.us-west-2.rds.amazonaws.com',
    user: 'root',
    password: 'swaglords',
    database: 'mysql',
    port: 3306
}).connect(function(error) {
    if (error) {
        return console.log('CONNECTION error: ' + error);
    }
    this.query().
        insert('MainUserDatabase',
            ['email', 'password', 'first_name', 'last_name'],
            ['xyzh@gmail.com', 'password', 'Oeem', 'Stosh']
        ).
        execute(function(error, result) {
                if (error) {
                        console.log('ERROR: ' + error);
                        return;
                }
                console.log('GENERATED id: ' + result.id);
        });
});