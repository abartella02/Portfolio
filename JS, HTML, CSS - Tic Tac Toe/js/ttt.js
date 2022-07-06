 console.log("Hi");
 let loginInfo = [["a", "b"]]; //need php to store login info

 const title = document.getElementById("title");
 const board = document.getElementById("board");
 const loginbox = document.getElementById("loginbox");

 let O_wins = 0;
 let X_wins = 0;

 function getInfo(){
     const user = document.getElementById("user").value;
     const pass = document.getElementById("pass").value;
     return [user, pass];
 }

 function login(){
    let loginCond = false;
    
    let user = getInfo()[0];
    let pass = getInfo()[1];

    for(let i = 0; i<loginInfo.length; i++){
        console.log(loginInfo[i][0]);
        console.log(loginInfo[i][1]);

        if(user === loginInfo[i][0]){
            if(pass === loginInfo[i][1]){
                loginCond = true;
                break;
            }
        }
    }
    console.log(loginCond);
    if(loginCond === true){
        loginbox.style.display = 'none';
        title.style.display = 'block';
        board.style.display = 'grid';
    }
    return;
 }

 const tiles = document.querySelectorAll(".tile");
 const PLAYER_X = "X";
 const PLAYER_O = "O";

 let turn = PLAYER_X;
 const boardstate = Array(tiles.length);
 boardstate.fill(null);

 //Elements
 const strike = document.getElementById("strike");
 const gameOverArea = document.getElementById("game-over-area");
 const gameOverText = document.getElementById("game-over-text");
 const playAgain = document.getElementById("play-again");
 playAgain.addEventListener("click", startNewGame);
 const loginButton = document.getElementById("loginButton");
 loginButton.addEventListener("click", login);
 const xscore = document.getElementById("xscore");
 const oscore = document.getElementById("oscore");

 tiles.forEach(tile=>addEventListener("click", tileclick));

function startNewGame(){
    strike.className = "strike";
    gameOverArea.className = "hidden";
    boardstate.fill(null);
    tiles.forEach((tile)=> (tile.innerText = ""));
    turn = PLAYER_X;
    setHoverText();
    xscore.style.fontWeight = 'normal';
    oscore.style.fontWeight = 'normal';
}

function setHoverText(){
    //remove current hover text
    tiles.forEach((tile)=>{
        tile.classList.remove("x-hover");
        tile.classList.remove("o-hover");
    });

    const hoverClass = `${turn.toLowerCase()}-hover`

    tiles.forEach(tile => {
        if(tile.innerText === ""){
            tile.classList.add(hoverClass);
        }
    });

}

setHoverText();

function tileclick(event){
    if(gameOverArea.classList.contains("visible")){
        return;
    }

    const tile = event.target;
    const tileNumber = tile.dataset.index;
    if(tile.innerText != ""){
        return;
    }

    if(turn === PLAYER_X){
        tile.innerText = PLAYER_X;
        boardstate[tileNumber-1] = PLAYER_X;
        turn = PLAYER_O;
    }else{
        tile.innerText = PLAYER_O;
        boardstate[tileNumber-1] = PLAYER_O;
        turn = PLAYER_X;
    }

    setHoverText();
    winnerCheck();
}

const winCond = [
    {combo:[1,2,3], strikeClass: "strike-row-1"},
    {combo:[4,5,6], strikeClass: "strike-row-2"},
    {combo:[7,8,9], strikeClass: "strike-row-3"},

    {combo:[1,4,7], strikeClass: "strike-col-1"},
    {combo:[2,5,8], strikeClass: "strike-col-2"},
    {combo:[3,6,9], strikeClass: "strike-col-3"},

    {combo:[1,5,9], strikeClass: "strike-diag-1"},
    {combo:[3,5,7], strikeClass: "strike-diag-2"},
];

function winnerCheck(){
    for(cond of winCond){
        const {combo, strikeClass} = cond;
        const tileValue1 = boardstate[combo[0]-1];
        const tileValue2 = boardstate[combo[1]-1];
        const tileValue3 = boardstate[combo[2]-1];

        if(tileValue1 != null && tileValue1 === tileValue2 && tileValue1 === tileValue3){
            strike.classList.add(strikeClass);
            gameOver(tileValue1);
            return;
        }
    }

    const allTilesFull = boardstate.every((tile)=>tile !== null);
    if(allTilesFull){
        gameOver(null);
    }
}

function gameOver(winnerText){
    let text = "Draw";
    if(winnerText != null){
        text = `Winner is ${winnerText}`;
    }

    if(winnerText === "X"){
        xscore.innerText = ++X_wins;
        xscore.style.fontWeight = 'bold';
    }
    if(winnerText === "O"){
        oscore.innerText = ++O_wins;
        oscore.style.fontWeight = 'bold';
    }

    gameOverArea.className = "visible";
    gameOverText.innerText = text;
}