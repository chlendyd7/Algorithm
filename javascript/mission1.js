console.log('hello');

const numArray = [[10], [30], [50], [80]];
const player = { "A": 0, "B": 0, "C": 0 };


/**
 * 
 * @param {[]} parm0 
 */
function play(parm0) {

    for (let i = 0; i < parm0.length; i += 3) {
        console.log(parm0.slice(i, i + 3));
        turnOrder = normalize(parm0.slice(i, i + 3));
        for (const { val: card, i: player } of turnOrder) {
            processTurn(card, player);
        }
    }
}

function processTurn(card, player) {
    const array = selectArray(card);
}

function selectArray(card) {
    let minDiff = 1000000;
    let selected = [];
    let lastOfSelected;

    
}

function normalize(array) {
    cards = array.map((val, i) => ({
        val, i
    }))
    .sort((a, b) => a.val - b.val);
    console.log(cards);
}

console.log(play([21, 9, 4]));
// Map([["A", '0'], ["B", '2'], ["C", '0']])