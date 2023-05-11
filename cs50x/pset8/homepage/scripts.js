document.addEventListener('DOMContentLoaded', function () {
    let idContatoBar = document.querySelector("#contato-bar");
    if (idContatoBar) {cafe()} else {document.removeEventListener('DOMContentLoaded', cafe)};
});

/*function cafe() {
    let text = document.querySelector("#teste");
    setInterval(function(){
        text.innerHTML = text.innerHTML == "Entre em contato conosco!" ? "Entre em contato conosco! Vamos tomar um café." : "Entre em contato conosco!";
    }, 1000);
}*/

function cafe() {
    let div = document.querySelector("#contato-bar");
    let text = " Vamos tomar um café!";
    text = text.split("").reverse();
    var typer = setInterval(function(){
        if (!text.length) {return clearInterval(typer), setTimeout(uncafe, 1000)};
        div.innerHTML += `${text.pop()}`;
    },100);
}

function uncafe() {
    let div = document.querySelector("#contato-bar");
    let text = div.innerHTML;
    text = text.split("");
    var typer = setInterval(function(){
        if (!text.length) {return clearInterval(typer), papo()};
        div.innerHTML = `${text.join("")}`;
        text.pop();
    },100);
}

function papo() {
    let div = document.querySelector("#contato-bar");
    let text = " Vamos bater um papo!";
    text = text.split("").reverse();
    var typer = setInterval(function(){
        if (!text.length) {return clearInterval(typer), setTimeout(unpapo, 1000)};
        div.innerHTML += `${text.pop()}`;
    },100);
}

function unpapo() {
    let div = document.querySelector("#contato-bar");
    let text = div.innerHTML;
    text = text.split("");
    var typer = setInterval(function(){
        if (!text.length) {return clearInterval(typer), solucao()};
        div.innerHTML = `${text.join("")}`;
        text.pop();
    },100);
}

function solucao() {
    let div = document.querySelector("#contato-bar");
    let text = " Sua solução está aqui!";
    text = text.split("").reverse();
    var typer = setInterval(function(){
        if (!text.length) {return clearInterval(typer), setTimeout(unsolucao, 1000)};
        div.innerHTML += `${text.pop()}`;
    },100);
}

function unsolucao() {
    let div = document.querySelector("#contato-bar");
    let text = div.innerHTML;
    text = text.split("");
    var typer = setInterval(function(){
        if (!text.length) {return clearInterval(typer), cafe()};
        div.innerHTML = `${text.join("")}`;
        text.pop();
    },100);
}

function joke() {
    document.querySelector("#joke-alert").hidden=false;
}

function joke_off() {
    document.querySelector("#joke-alert").hidden=true;
}

function hello() {
    let name = document.querySelector("#name").value;
    if (name)
    {
        let element = document.querySelector("#hello-alert");
        element.innerHTML = `<strong>Santo guacamole!</strong> ${name}, nada irá acontecer aqui, é só um teste!`;
        document.querySelector("#hello-alert").hidden=false;
        setTimeout(function () {
            document.querySelector("#hello-alert").hidden=true;
        }, 3000)
    }
    else
    {
        document.querySelector("#hello-alert").hidden=false;
        setTimeout(function () {
            document.querySelector("#hello-alert").hidden=true;
        }, 3000)
    }
}