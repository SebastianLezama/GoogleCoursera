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

// collections like json,

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
