const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const db = new sqlite3.Database('./todo.db');

const app = express();

const port = 3000;

app.use(express.urlencoded({extended: true}));
app.use(express.json());

app.set('view engine', 'pug');

app.get('/', (req, res) => {
//    res.send("Hello, CS50!") //para enviar um texto para a URL;
    let todolist = [];
    db.each('SELECT name FROM todos', (err, row) => {
        if (err) {
            console.log(err);
        }
        else {
            console.log(row);
            todolist.push(row.name);
        }
    }, (err) => {
        res.render('index', {title: 'CS50', message: 'This is my to-do app', todolist: todolist});
    });
});

app.post('/', (req, res) => {
    //console.log(req.body); //só para vermos que está funcionando, com log do body.
    let todo = req.body.todo;
    console.log(todo); //para garantir que está tudo certo
    db.run('INSERT INTO todos(name) VALUES(?)', todo);
    res.redirect("/"); //Não queremos o site num loop eterno, por isso recarregamos a homepage;
});

app.listen(port, () => {
    console.log('listening on port 3000');
});

console.log("Hello, CS50!")