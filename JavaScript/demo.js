console.log('Hello world!');

// use camel case

// variables 

let firstName = 'Sebastian';
let age = 31;
const species = 'Human';

// objects
let person = {
    name: 'Ro',
    age: 31
};

person.sex = "female";
console.log(person.name);
console.log(person['sex']);
delete person.sex

function checkObj(obj, property) {
    if (obj.hasOwnProperty(property)) {
        return obj[property];
    } else {
        return "Not found"
    }
}

// arrays
// declared arrays with const can be mutated with []
// use Object.freeze() to avoid mutation

let sampleColors = ['red', 'blue'];
console.log(sampleColors[0]);
sampleColors.push("green")
let green = sampleColors.pop()
let color_red = sampleColors.shift()
sampleColors.unshift(color_red)

function nextInLine(arr, item) {
    arr.push(item);
    return arr.shift();
}

let testArr = [1,2,3,4,5];

console.log("Before: " + JSON.stringify(testArr));
console.log(nextInLine(testArr, 6))
console.log("After: " + JSON.stringify(testArr));

// functions

function greet(name, lastName) {
    console.log('Hello ' + name + ' ' + lastName)
}

let num = 1;
num++;
num--

// if statements
// && and operator
// || or operator
let num_value = 8

function trueOrFalse(val) {
    if (val == 8) {
        return "Something";
    }
    return "Not something";
}
function strictTrueOrFalse(val){
    if (val === '8') {
        return "Something";
    }
    return "Not something";
}

function testLessThan(val) {
    if (val < 25) {
        return "Under 25";
    }

    if (val < 55) {
        return "Under 55";
    }

    return "55 or over";
}

function testLargerThan(val) {
    if (val >= 50) {
        return "Greater or equal than 50"
    } else if (val >= 25) {
        return "Greater or equal than 25"
    } else {
        return "Greater or equal than 0"
    }
}

// switch

function caseInSwitch(val) {
    let answer = '';
    switch(val) {
        case 1:
            answer = "alpha";
            break;
        case 2:
            answer = "beta";
            break;
        case 3:
            answer = "gamma";
            break;
        case 4:
            answer = "delta";
            break;
        default:
            answer = "stuff";
            break;

    }
    return answer
}

// collections like json, objects

let templateCollection = {
    "java": {
        "style": "powerline",
        "powerline_symbol": "\uE0B0",
        "foreground": "#ffffff",
        "background": "#d8406b",
        "test": [],
        "template": " \uE738 {{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }}"
    },
    "node": {
        "background": "#5aa6af",
        "foreground": "#ffffff",
        "powerline_symbol": "\ue0b0",
        "style": "powerline",
        "template": " \ue718 {{ if .PackageManagerIcon }}{{ .PackageManagerIcon }} {{ end }}{{ .Full }} ",
    },
    "python": {
        "style": "powerline",
        "powerline_symbol": "\uE0B0",
        "properties": {
            "home_enabled": true,
            "display_mode": "files"
        },
        "test": ["1990", "1984"],
        "foreground": "#ffffff",
        "background": "#5a84af",
        "template": " \uE235 {{ if .Error }}{{ .Error }}{{ else }}{{ if .Venv }}{{ .Venv }} {{ end }}{{ .Full }}{{ end }} "
    }
}

let templateCopy = JSON.parse(JSON.stringify(templateCollection));

function updateTemplate(arr, id, prop, value) {
    if (value === "") {
        delete arr[id][prop];
    } else if (prop === "test") {
        arr[id][prop] = arr[id][prop] || [];
        arr[id][prop].push(value);
    } else {
        arr[id][prop] = value;
    }
    return arr;
}

// console.log(templateCopy)
// console.log(updateTemplate(templateCollection, "python", "test", "2022"))

// while loops

let x = 0
let myArray = []

while (x < 5) {
    myArray.push(x);
    x++;
}
do {
    myArray.push(x)
    x++;
} while (x < 10)
console.log(myArray)

// for loops

let ourArray = []

for (let i = 1; i < 6; i++) {
    ourArray.push(i);
}

for (let i = 10; i >= 6; i--) {
    ourArray.push(i);
}
console.log(ourArray)
// iteration with clear sintax
let total = 0
for (const element of myArray) {
    total += element;
}
console.log(total)

function multiplyAll(arr) {
    let product = 1;

    for (const i of arr) {
        for (const j of i) {
            product *= j;
        }
    }
    return product
}

console.log(multiplyAll([[1,2],[3,4],[5,6,7]]));

// array lookup

let templateArray = [
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "49824238",
        "likes": ["JS", "Gaming"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "31200389",
        "likes": ["Python", "CSGO"]
    }
];

function lookUp(name, prop) {
    for (const i of templateArray) {
        if (i["firstName"] === name) {
            return i[prop] || "no such property";
        }
    }
    return "no such name";
}

console.log(lookUp("Sherlock", "lastName"))

// random numbers

let wholeNumber = Math.floor(Math.random() * 10);
let decimalNumber = Math.random();

console.log(decimalNumber)

// random range

function randomRange(min, max) {
    return Math.floor(Math.random() * (max - min +1)) + min;
}

console.log(randomRange(1, 4))

// convert string to integer with parseInt

let stringNumber = "56"
let stringBinary = "10011"

console.log(parseInt(stringBinary, 2))

// ternary: condition ? if true : if false
// if nested, start with if statement
function checkSign(number) {
    if (number > 0) {
        return "positive";
    }
    return number < 0 ? "negative" : "zero";
}

console.log(checkSign(6))

// arrow functions

const myConcat = (arr1, arr2) => arr1.concat(arr2);

// rest operator ...

const sum = (function() {
    return function sum(...args) {
        return args.reduce((a,b) => a + b, 0);
    };
})();
console.log(sum(3,5,4,8))

// spread operator [...args]
// to copy an array
// arr2 = [...arr1]

// destructuring assignment: const { a : b } = of object
// destructuring nested: const { a : {a2 : b}} = of object
// destrcuturing to remove items: const [ , , ...arr] = list;
// destructuring to get prop from object:
//  function half({ max, min }) { return (max + min) / 2;}

let voxel = {x: 3.6, y: 7.5, z: 6.5};

const { x : a, y : b, z : c } = voxel;
console.log(a)

// template literals

const greeting = `Hello, my name is ${person.name}!
I am ${person.age} years old.`;

console.log(greeting);

// iterating to template literals

function makeList(arr) {
    const result = []
    for (const i of arr) { 
        result.push(`<li class="text-warning">${i["firstName"]}</li>`)
    }
    return result
    }

console.log(makeList(templateArray))

// object literals
// to create an object and asign properties
const createPerson = (name, age, gender) => ( { name, age, gender});

// class syntax

class SpaceShuttle {
    constructor(targetPlanet) {
    this.targetPlanet = targetPlanet;
    }
}
let zeus = new SpaceShuttle('Jupiter');
console.log(zeus.targetPlanet)

function makeClass() {
    class Thermostat {
        constructor(temp) {
            this._temp = 5/9 * (temp - 32);
        }
        get temperature() {
            return this._temp;
        }
        set temperature(updatedTemp) {
            this._temp = updatedTemp;
        }
    }
    return Thermostat
}

const Thermostat = makeClass();
const thermos = new Thermostat(76);
let temp = thermos.temperature;
console.log(temp)
thermos.temperature = 10;
temp = thermos.temperature;
console.log(temp)

// import statement: import { function } from "./filename(.js)"
// declare export function and variables
// also: import * as newObjectName from "./filename(.js)"
// export default
// import function from "./filename(.js)"
