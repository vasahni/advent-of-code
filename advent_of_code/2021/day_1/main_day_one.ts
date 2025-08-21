import {readFileSync} from 'fs'

// part 1
let reader:string[] = readFileSync('day_1/floor_measurements.txt', 'utf-8').toString().split("\n")
const toNumbers = (arr:string[]) => arr.map(Number)

let arrayNumbers:number[] = toNumbers(reader)
let arrayNumbersMaster:number[] = arrayNumbers
let previousNumber = arrayNumbers.shift()

let count = 0

for (const number of arrayNumbers) {
    if (previousNumber !== undefined) {
        if (number > previousNumber) {
            count += 1
        }
    }
    else {
        throw new Error('No undefined in list')
    }
    previousNumber = number
}

console.log(count)


//part 2
count = 0
const rollingSum = (array:number[], firstIndex:number, secondIndex:number, thirdIndex:number) =>  array[firstIndex] + array[secondIndex] + array[thirdIndex]

let firstIndex = 0
let secondIndex = 1
let thirdIndex = 2

let previousSum = rollingSum(arrayNumbersMaster, firstIndex, secondIndex, thirdIndex)

for (var i = 1; i < arrayNumbersMaster.length - 2; i++) {
    firstIndex += 1
    secondIndex += 1
    thirdIndex +=1

    let currentSum = rollingSum(arrayNumbersMaster, firstIndex, secondIndex, thirdIndex)

    if (currentSum > previousSum) {
        count += 1
    }

    previousSum = currentSum
}

console.log(count)
