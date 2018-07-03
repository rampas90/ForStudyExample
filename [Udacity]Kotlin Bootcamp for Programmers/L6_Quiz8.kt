
enum class Direction{
    NORTH,EAST,WEST,SOUTH,START,END
}


class Game{
    var path = mutableListOf<Direction>(Direction.START)
    val north = {path.add(Direction.NORTH)}
    val south = { path.add(Direction.SOUTH)}
    val east={path.add(Direction.EAST)}
    val west = {path.add(Direction.WEST)}
    val end = {path.add(Direction.END); println("Game Over: $path"); path.clear(); false}


    fun move(where: () -> Boolean){
        where.invoke()
    }


    fun makeMove(command: String?) {
        if (command.equals("n")) move(north)
        else if(command.equals("s")) move(south)
        else if (command.equals("e")) move(east)
        else if(command.equals("w")) move(west)
        else move(end)

    }
}

fun main(args: Array<String>) {
    val game = Game()
    println(game.path)
    game.north()
    println(game.path)
    game.south()
    println(game.path)
    game.east()
    println(game.path)
    game.west()
    println(game.path)
    game.end()
    println(game.path)
    game.makeMove("n")
    println(game.path)
}

