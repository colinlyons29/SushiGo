var PythonShell = require('python-shell');
var options = {
    mode: 'text',
    pythonPath: '/usr/local/bin/python3',
    args: ['playersDB', 'selectedCardsDB']
};




PythonShell.run('endOfRound.py', options, function (err, results) {
    if (err) throw err;
    // results is an array consisting of messages collected during execution
    console.log(results);
});
