package day_2

import java.io.File

val cubeConfig = mapOf(
    "red" to 12,
    "green" to 13,
    "blue" to 14
)

fun main() {
    val gamesRaw = readFileLines("C:\\projects\\practice\\advent_of_code\\src\\main\\kotlin\\day_2\\example.txt")
//    val gamesRaw = readFileLines("C:\\projects\\practice\\advent_of_code\\src\\main\\kotlin\\day_2\\puzzle.txt")
    val games = gamesRaw.map { mapToGame(it) }
    games.forEach{ println(it) }
    val validGames = games.filter {game ->
            game.rounds.all { round ->
                round.numberByColor  .all { (key, value) ->
                    value <= cubeConfig.get(key)!!
                }
            }
        }.distinctBy { it.id }

    val validGames2 = games.filter { game ->
        val result = game.rounds.all { round ->
            round.numberByColor.entries.all {
                val valueInRound = it.value
                val valueInCubeConfig = cubeConfig.get(it.key)!!
                val condition = valueInRound <= valueInCubeConfig
                if(condition) {
                    println("GAME ${game.id} OK ")
                }
                condition
            }
        }
        if (!result) {
            println("Game ${game.id} NOT OK ")
        }
        result
    }
        .map { it.id }
        .sum()

    println(validGames2)
}


fun mapToGame(gameRaw: String): Game {
    val id = gameRaw.substring("Game ".length, "Game ".length + 1).toInt()
    val game = Game(id, mutableListOf())
    val rounds = gameRaw.substring(gameRaw.indexOf(": ") + 2)
        .split("; ")
    rounds.forEach { str ->
        val cubes = str.split(", ")
        val numberByColor = cubes.map {
            val nrAndColor = it.split(" ")
            nrAndColor[1] to nrAndColor[0].toInt()
        }
        game.rounds.add(Round(numberByColor.toMap()))
    }
    return game
}

fun readFileLines(fileName: String): List<String> = File(fileName).useLines { it.toList() }