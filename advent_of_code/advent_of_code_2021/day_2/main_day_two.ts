import { once } from 'events'
import * as fs from 'fs'
import * as readline from 'readline'

let coordinates:[number, number] = [0,0]
let coordinatesThree:[number, number, number] = [0,0,0]

const processLinePartOne = (line:string) => {
    let lineSplit = line.split(' ')
    let direction = lineSplit[0]
    let amount = Number(lineSplit[1])

    if (direction == 'forward') {
        coordinates[0] = coordinates[0] + amount
    }
    else if (direction == 'up') {
        coordinates[1] = coordinates[1] - amount
    }
    else {
        coordinates[1] = coordinates[1] + amount
    }
}

const processLinePartTwo = (line:string) => {
    let lineSplit = line.split(' ')
    let direction = lineSplit[0]
    let amount = Number(lineSplit[1])

    if (direction == 'forward') {
        coordinatesThree[0] = coordinatesThree[0] + amount
        coordinatesThree[1] = coordinatesThree[1] + coordinatesThree[2] * amount
    }
    else if (direction == 'up') {
        coordinatesThree[2] = coordinatesThree[2] - amount
    }
    else {
        coordinatesThree[2] = coordinatesThree[2] + amount
    }
}

async function processLineByLinePart(coordinates:[number, number, ...number[]], callback:any) {
    try {
        const fileStream = fs.createReadStream('day_2/input.txt')
        const rl = readline.createInterface({
            input:fileStream,
            crlfDelay:Infinity
        })
        rl.on('line', callback)
        await once(rl, 'close')
    }
    catch (err) {
        console.log(err)
    }
};

async function run() {
    await processLineByLinePart(coordinates, processLinePartOne)
    console.log(coordinates[0] * coordinates[1])
    await processLineByLinePart(coordinatesThree, processLinePartTwo)
    console.log(coordinatesThree[0] * coordinatesThree[1])
}

run()
