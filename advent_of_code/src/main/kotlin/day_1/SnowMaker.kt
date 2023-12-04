package day_1

import java.io.File
import java.lang.StringBuilder
import java.util.ArrayList

class SnowMaker {
}

val digitsByWord = mapOf(
    "one" to 1,
    "two" to 2,
    "three" to 3,
    "four" to 4,
    "five" to 5,
    "six" to 6,
    "seven" to 7,
    "eight" to 8,
    "nine" to 9
)

fun main(args: Array<String>) {
//    val lines = readFileLines("C:\\projects\\practice\\advent_of_code\\src\\main\\kotlin\\day_1\\puzzle.txt")
    val lines = readFileLines("C:\\projects\\practice\\advent_of_code\\src\\main\\kotlin\\day_1\\example_2.txt")
//    findNextDigit("abcone2threexyz")
    lines.forEach{ println(searchForWords(it)) }
    var totalCalibration: Long = 0
//    lines.forEach{
//        totalCalibration = totalCalibration + (calculateLineFromLetters(it)!!)
//    }
//    print("calibration: ${totalCalibration}")
}

private fun calculateLineFromDigits(line: String): Long? {
    var numbers = ArrayList<String>()
    println("\n line: " + line)
    for (i in 0..line.length - 1) {
        if (line[i].isDigit()) {
            numbers.add(line[i].toString())
        }
    }
    var totalCalibration = (numbers[0] + numbers[numbers.size - 1]).toLongOrNull()
    println("line calibration: " + totalCalibration)
    return totalCalibration
}



private fun searchForWords(line: String): Any? {
    var numbers = ArrayList<String>()
    var i: Int = 0
    println("line: ${line}")
    while (i < line.length) {
        if(line[i].isDigit()){
            numbers.add(line[i].toString())
            i++
        } else {
            var defaultKeyLength = line.substring(i, i+2)
            if (digitsByWord.containsKey(defaultKeyLength)) {
                numbers.add(digitsByWord.get(defaultKeyLength).toString())
                i += defaultKeyLength.length
            } else {
                var reset = false
                for(j in i + defaultKeyLength.length..line.length - 1 ) {
                    var key = line.substring(line.indexOf(defaultKeyLength), j + 1)
                    if (digitsByWord.containsKey(key)) {
                        numbers.add(digitsByWord.get(key).toString())
                        i += key.length
                    }
                    if(key.length == 5) {
                        i++
                        reset = true
                        break
                    }
                }
                if(!reset) i++
            }
        }
    }
    return numbers[0].toString().plus(numbers[numbers.size-1].toString())
}

private fun calculateLineFromLetters(line: String): Long? {
    println("\n line: " + line)

    var firstDigit: Int? = null
    var secondDigit: Int? = null

//    var numbers = ArrayList<Int>()
    var letters = StringBuilder()
    var res = StringBuilder()
//    findNextDigit(line)
//    for (i in 0..line.length - 1) {
//        if (!line[i].isDigit()) {
//            letters.append(line[i])
//        }
//        if (digitsByWord.containsKey(letters.toString())) {
//            res.append(digitsByWord.get(letters.toString())!!)
//            letters.clear()
//        }
//        if (res.length == 2) {
//            break
//        }
//    }
//    print(res.toString())
//    for (number in digitsByWord.keys) {
//        if (line.startsWith(number)) {
//            firstDigit = digitsByWord.get(number)!!
//        }
//        if (line.endsWith(number)) {
//            secondDigit = digitsByWord.get(number)!!
//        }
//        if (firstDigit == null) {
//            firstDigit = findFirstDigit(line, number, firstDigit)
//        }
//        if (secondDigit == null) {
//            secondDigit = findLastDigit(line, number, secondDigit)
//        }
//        if (firstDigit != null && secondDigit != null) {
//            break
//        }
//    }
//    var totalCalibration = firstDigit.toString() + secondDigit.toString()
//    println("line calibration: " + totalCalibration)

    return res.toString().toLongOrNull()
}

private fun findLastDigit(line: String, number: String, secondDigit: Int?): Int? {
    var secondDigit1 = secondDigit
    var index = line.lastIndexOf(number)
    if (index != -1) {
        secondDigit1 = digitsByWord.get(line.substring(index, index + number.length))
    }
    return secondDigit1
}


fun readFileLines(fileName: String): List<String> = File(fileName).useLines { it.toList() }

