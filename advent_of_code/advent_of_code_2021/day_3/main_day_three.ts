import {once} from 'events'
import * as fs from 'fs'
import * as readline from 'readline'

let positionValues = new Array<number>(12)
let finalBinary = new Array<string>(12)
positionValues = [0,0,0,0,0,0,0,0,0,0,0,0]


const processLine = (line:string) => {
    let numArray = line.split('').map(Number)
    numArray.forEach((value, index) => {
        if (value == 1) {
            positionValues[index] += 1
        }
    })
}

function calculateBinary(positionValues:number[]) {
    positionValues.forEach((value, index) => {
        if (value > 500) {
            finalBinary[index] = '1'
        }
        else {
            finalBinary[index] = '0'
        }
    })
    let decimalNumber = parseInt(finalBinary.join(''), 2)
    return decimalNumber
}

async function processLineByLine(callback:any) {
    try {
        const fileStream = fs.createReadStream('day_3/input.txt')
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
}

async function runPartOne() {
    await processLineByLine(processLine)
    console.log(positionValues)
    let gamma = calculateBinary(positionValues)
    let epsilon = parseInt('010001011010', 2)
    console.log(gamma * epsilon)
}

// when equal lengths, returns the LAST occurring element
function mode(arr:Array<number>){
    return arr.sort((a,b) =>
          arr.filter(v => v===a).length
        - arr.filter(v => v===b).length
    ).pop();
}

// when equal amounts, returns the FIRST occurring element
function leastCommon(array:Array<number>) {
    const result:number|undefined = [...array.reduce((r, n) => // create a map of occurrences
            r.set(n, (r.get(n) || 0) + 1), new Map()
    )]
    .reduce((r, v) => v[1] < r[1] ? v : r)[0]; // get the the item that appear less times
    return result
}

async function runPartTwo(most:Boolean) {
    let data:number[][] = []
    await processLineByLine((line:string) => {
        let numArray = line.split('').map(Number)
        data.push(numArray)
    })
    let dataCopy = [...data]
    let i = 0
    let totalEntries = dataCopy.length

    while (totalEntries > 1) {
        let subset = dataCopy.map((each) => each[i])
        if (most==true) {
            subset.sort()
            var sorting = mode(subset)
        }
        else {
            subset.sort()
            var sorting = leastCommon(subset)
        }

        dataCopy = dataCopy.filter((each) => each[i] == sorting)
        totalEntries = dataCopy.length
        i += 1
    }
    let binaryNumber = dataCopy[0].map(String).join('')
    let finalDecimal:number =  parseInt(binaryNumber, 2)
    return finalDecimal

}

let oxygen = runPartTwo(true)
let oxygenNumber = oxygen.then((resolve) => console.log(resolve)).catch(err => console.log(err))
let carbonDioxide = runPartTwo(false)
let carbonDioxideNumber = carbonDioxide.then((resolve) => console.log(resolve)).catch(err => console.log(err))
