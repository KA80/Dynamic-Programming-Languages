var canvas, ctx, figures, idTimer;
var speed = 0;
var N = 200;


class Figure{
    constructor(pX, pY){
        this.posX = pX;
        this.posY = pY;
        this.color1 = 'rgb(' + Math.floor(Math.random() * 256) + ','
            + Math.floor(Math.random() * 256) + ',' + Math.floor(Math.random() * 256) + ')';
        this.color2 = 'rgb(' + Math.floor(Math.random() * 256) + ','
            + Math.floor(Math.random() * 256) + ',' + Math.floor(Math.random() * 256) + ')';
        this.path = Math.floor(Math.random() * 4);
    }

}

class Ball extends Figure{
    constructor(pX, pY){
        super(pX, pY);
        this.rBall = 5 + Math.random() * 100;
    }

    
    draw(ctx){
        ctx.fillStyle = this.colorBall(ctx);
        ctx.beginPath();
        ctx.arc(this.posX, this.posY, this.rBall, 0, 2 * Math.PI, false);
        ctx.closePath();
        ctx.fill();
    }

    colorBall(ctx){
        this.gradient = ctx.createRadialGradient(this.posX + this.rBall / 4,
            this.posY - this.rBall / 6, this.rBall / 8, this.posX, this.posY, this.rBall);
        this.gradient.addColorStop(0, this.color2);
        this.gradient.addColorStop(0.85, this.color1);
        return this.gradient;
    }

    is_TouchWithCanvas(){
        if ((this.posX + this.rBall > canvas.width) || (this.posX - this.rBall < 0)
            || (this.posY - this.rBall < 0) || (this.posY + this.rBall > canvas.height))
            return true;
        return false
    }

    increase(ctx){
        ctx.fillStyle = this.gradient;
        ctx.beginPath();
        this.rBall++;
        ctx.arc(this.posX, this.posY, this.rBall, 0, 2 * Math.PI, false);
        ctx.closePath();
        ctx.fill();
    }

    is_maxSize(){
        if (this.rBall >= N)
            return true;
        return false;
    }

}


class Rectangle extends Figure{
    constructor(pX, pY){
        super(pX, pY);
        this.rHeight = 5 + Math.random() * 100;
        this.rWidth = 5 + Math.random() * 100;
    }

    draw(ctx){
        ctx.beginPath();
        ctx.moveTo(this.posX - this.rWidth, this.posY + this.rHeight);
        ctx.lineTo(this.posX + this.rWidth, this.posY + this.rHeight);
        ctx.lineTo(this.posX + this.rWidth, this.posY - this.rHeight);
        ctx.lineTo(this.posX - this.rWidth, this.posY - this.rHeight);
        ctx.lineTo(this.posX - this.rWidth, this.posY + this.rHeight);
        ctx.closePath();
        ctx.fillStyle = this.colorRectangle(ctx);
        ctx.fill();
    }

    colorRectangle(ctx){
        this.gradient = ctx.createLinearGradient(this.posX + this.rWidth, this.posY - this.rHeight, this.posX - this.rWidth, this.posY + this.rHeight);
        this.gradient.addColorStop(0, this.color2);
        this.gradient.addColorStop(0.85, this.color1);
        return this.gradient;
    }

    is_TouchWithCanvas() {
        if ((this.posX + this.rWidth > canvas.width) || (this.posX - this.rWidth < 0)
            || (this.posY - this.rHeight < 0) || (this.posY + this.rHeight > canvas.height))
            return true;
        return false
    }

    increase(ctx){
        ctx.beginPath();
        this.rHeight++;
        this.rWidth++;
        ctx.moveTo(this.posX - this.rWidth, this.posY + this.rHeight);
        ctx.lineTo(this.posX + this.rWidth, this.posY + this.rHeight);
        ctx.lineTo(this.posX + this.rWidth, this.posY - this.rHeight);
        ctx.lineTo(this.posX - this.rWidth, this.posY - this.rHeight);
        ctx.lineTo(this.posX - this.rWidth, this.posY + this.rHeight);
        ctx.closePath();
        ctx.fillStyle = this.gradient;
        ctx.fill();
    }

    is_maxSize() {
        if (this.rHeight >= N || this.rWidth >= N)
            return true;
        return false;
    }

}


class Triangle extends Figure{
    constructor(pX, pY){
        super(pX, pY);
        this.rHeight = 5 + Math.random() * 200;
        this.rSide = 5 +  Math.random() * 200;
    }

    draw(ctx){
        ctx.beginPath();
        ctx.moveTo(this.posX - this.rSide / 2, this.posY + this.rHeight / 2);
        ctx.lineTo(this.posX + this.rSide / 2, this.posY + this.rHeight / 2);
        ctx.lineTo(this.posX, this.posY - this.rHeight / 2);
        ctx.lineTo(this.posX - this.rSide / 2, this.posY + this.rHeight / 2);
        ctx.closePath();
        ctx.fillStyle = this.colorTriangle(ctx);
        ctx.fill()
    }

    colorTriangle(ctx){
        this.gradient = ctx.createLinearGradient(this.posX + this.rSide / 2, this.posY - this.rHeight / 2, this.posX - this.rSide / 2, this.posY + this.rHeight / 2);
        this.gradient.addColorStop(0, this.color2);
        this.gradient.addColorStop(0.75, this.color1);
        return this.gradient;
    }

    is_TouchWithCanvas() {
        if ((this.posX + this.rSide / 2 > canvas.width) || (this.posX - this.rSide / 2 < 0)
            || (this.posY - this.rHeight / 2 < 0) || (this.posY + this.rHeight / 2 > canvas.height))
            return true;
        return false
    }

    increase(ctx){
        ctx.beginPath();
        this.rHeight++;
        this.rSide++;
        ctx.moveTo(this.posX - this.rSide / 2, this.posY + this.rHeight / 2);
        ctx.lineTo(this.posX + this.rSide / 2, this.posY + this.rHeight / 2);
        ctx.lineTo(this.posX, this.posY - this.rHeight / 2);
        ctx.lineTo(this.posX - this.rSide / 2, this.posY + this.rHeight / 2);
        ctx.closePath();
        ctx.fillStyle = this.gradient;
        ctx.fill()
    }

    is_maxSize() {
        if (this.rHeight >= N || this.rSide >= N)
            return true;
        return false;
    }

}




function drawBack(ctx, col1, col2, w, h) {
    // закрашиваем канвас градиентным фоном
    ctx.save();
    var g = ctx.createLinearGradient(0, 0, 0, h);
    g.addColorStop(1, col1);
    g.addColorStop(0, col2);
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, w, h);
    ctx.restore();
}


// инициализация работы
function init() {
    canvas = document.getElementById('canvas');
    if (canvas.getContext) {
        ctx = canvas.getContext('2d');
        //рисуем фон
        drawBack(ctx, '#f702ff', '#aaa', canvas.width, canvas.height);
        //создаем 10 шариков, заноси их в массив и выводим на canvas
        path_rand = [];
        figures = [];
        for (var i = 1; i <= 20; i++) {
            var cur_figure = Math.floor(Math.random() * 3);
            var item;
            switch (cur_figure){
                case 0:
                    do {
                        var x = 10 + Math.random() * (canvas.width - 30);
                        var y = 10 + Math.random() * (canvas.height - 30);
                        item = new Ball(x, y);
                    } while (item.is_TouchWithCanvas())
                    break;
                case 1:
                    do{
                        var x = 10 + Math.random() * (canvas.width - 30);
                        var y = 10 + Math.random() * (canvas.height - 30);
                        item = new Rectangle(x, y);
                    } while (item.is_TouchWithCanvas())
                    break;
                case 2:
                    do{
                        var x = 10 + Math.random() * (canvas.width - 30);
                        var y = 10 + Math.random() * (canvas.height - 30);
                        item = new Triangle(x, y);
                    } while (item.is_TouchWithCanvas())
                    break;
            }
            item.draw(ctx);
            figures.push(item);
        }
    }
}


// создаем новый шарик по щелчку мыши, добавляем его в массив шариков и рисуем его
function goInput(event) {
    var x = event.clientX;
    var y = event.clientY;
    var cur_figure = Math.floor(Math.random() * 3);
    var item;
    switch (cur_figure){
        case 0:
            item = new Ball(x, y);
            if (!item.is_TouchWithCanvas()) {
                item.draw(ctx);
                figures.push(item);
            }
            break;
        case 1:
            item = new Rectangle(x, y);
            if (!item.is_TouchWithCanvas()) {
                item.draw(ctx);
                figures.push(item);
            }
            break;
        case 2:
            item = new Triangle(x, y);
            if (!item.is_TouchWithCanvas()) {
                item.draw(ctx);
                figures.push(item);
            }
            break;
    }  
}


function moveFigure_up() {
    //реализация движения шариков, находящихся в массиве balls вверх
    drawBack(ctx, '#f702ff', '#aaa', canvas.width, canvas.height);
    for (var i = 0; i < figures.length; i) {
        figures[i].posX = figures[i].posX + (Math.random() * 4 - 2);
        figures[i].posY = figures[i].posY + (Math.random() * 2 - 4 - speed);
        figures[i].draw(ctx);
        if (figures[i].is_TouchWithCanvas()){
            figures.splice(i, 1);
        }
        else
            i++;
    }
}

function moveBall_left() {
    //реализация движения шариков, находящихся в массиве balls влево
    drawBack(ctx, '#f702ff', '#aaa', canvas.width, canvas.height);
    for (var i = 0; i < figures.length; i) {
        figures[i].posX = figures[i].posX + (Math.random() * 2 - 4 - speed);
        figures[i].posY = figures[i].posY + (Math.random() * 4 - 2);
        figures[i].draw(ctx);
        if (figures[i].is_TouchWithCanvas())
            figures.splice(i, 1);
        else
            i++;
    }
}

function moveBall_right() {
    //реализация движения шариков, находящихся в массиве balls вправо
    drawBack(ctx, '#f702ff', '#aaa', canvas.width, canvas.height);
    for (var i = 0; i < figures.length; i) {
        figures[i].posX = figures[i].posX + (Math.random() * 2 + 2 + speed);
        figures[i].posY = figures[i].posY + (Math.random() * 4 - 2);
        figures[i].draw(ctx);
        if (figures[i].is_TouchWithCanvas())
            figures.splice(i, 1);
        else
            i++;
    }
}

function moveBall_down() {
    //реализация движения шариков, находящихся в массиве balls вправо
    drawBack(ctx, '#f702ff', '#aaa', canvas.width, canvas.height);
    for (var i = 0; i < figures.length; i) {
        figures[i].posX = figures[i].posX + (Math.random() * 4 - 2);
        figures[i].posY = figures[i].posY + (Math.random() * 2 + 2 + speed);
        figures[i].draw(ctx);
        if (figures[i].is_TouchWithCanvas())
            figures.splice(i, 1);
        else
            i++;
    }
}

function moveBall_rand() {
    //реализация движения шариков, находящихся в массиве balls вправо
    drawBack(ctx, '#f702ff', '#aaa', canvas.width, canvas.height);
    for (var i = 0; i < figures.length; i) {
        switch (figures[i].path) {
            case 0:
                figures[i].posX = figures[i].posX + (Math.random() * 4 - 2);
                figures[i].posY = figures[i].posY + (Math.random() * 2 - 4 - speed);
                break;
            case 1:
                figures[i].posX = figures[i].posX + (Math.random() * 2 - 4 - speed);
                figures[i].posY = figures[i].posY + (Math.random() * 4 - 2);
                break;
            case 2:
                figures[i].posX = figures[i].posX + (Math.random() * 2 + 2 + speed);
                figures[i].posY = figures[i].posY + (Math.random() * 4 - 2);
                break;
            case 3:
                figures[i].posX = figures[i].posX + (Math.random() * 4 - 2);
                figures[i].posY = figures[i].posY + (Math.random() * 2 + 2 + speed);
                break;
        }
        figures[i].draw(ctx);
        if (figures[i].is_TouchWithCanvas())
            figures.splice(i, 1);
        else
            i++;
    }
}

function moveBall_chaos() {
    //реализация движения шариков, находящихся в массиве balls вправо
    drawBack(ctx, '#f702ff', '#aaa', canvas.width, canvas.height);
    for (var i = 0; i < figures.length; i) {
        tmp = Math.floor(Math.random() * 4);
        switch (tmp) {
            case 0:
                figures[i].posX = figures[i].posX + (Math.random() * 4 - 2 );
                figures[i].posY = figures[i].posY + (Math.random() * 2 - 4 - speed);
                break;
            case 1:
                figures[i].posX = figures[i].posX + (Math.random() * 2 - 4 - speed);
                figures[i].posY = figures[i].posY + (Math.random() * 4 - 2);
                break;
            case 2:
                figures[i].posX = figures[i].posX + (Math.random() * 2 + 2 + speed);
                figures[i].posY = figures[i].posY + (Math.random() * 4 - 2);
                break;
            case 3:
                figures[i].posX = figures[i].posX + (Math.random() * 4 - 2);
                figures[i].posY = figures[i].posY + (Math.random() * 2 + 2 + speed);
                break;
        }
        figures[i].draw(ctx);
        if (figures[i].is_TouchWithCanvas()){
            figures.splice(i, 1);
        }
            
        else
            i++;
    }
}

function increaseSize(){
    drawBack(ctx, '#f702ff', '#aaa', canvas.width, canvas.height);
    for (var i = 0; i < figures.length; i){
        if (!figures[i].is_TouchWithCanvas(ctx) && !figures[i].is_maxSize()){
            figures[i].increase(ctx);
            i++;
        }
        else{
            figures.splice(i, 1);
        }
        
    }
}






function speed_up(){
    speed++;
}

function speed_down(){
    
    if (speed >= -2)
        speed--;
    else
        speed++;
}

function increase(){
    stop();
    idTimer = setInterval('increaseSize();', 50);
}

function move_up() {
    stop();
    idTimer = setInterval('moveFigure_up();', 50);
}

function move_left() {
    stop();
    idTimer = setInterval('moveBall_left();', 50);
}

function move_right() {
    stop();
    idTimer = setInterval('moveBall_right();', 50);
}

function move_down() {
    stop();
    idTimer = setInterval('moveBall_down();', 50);
}

function move_rand() {
    stop();
    idTimer = setInterval('moveBall_rand();', 50);
}

function move_chaos() {
    stop();
    idTimer = setInterval('moveBall_chaos();', 50);
}

function stop(){
    clearInterval(idTimer);
    speed = 0;
}