// Python Shell is initialized
// Arguments declared as the path of python, the arguments for the execution of the shell, and the mode of the argument, which is text by default
// The shell is run on the declared file, with the arguments
// A function for catching any errors and displaying the results of execution is present

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
