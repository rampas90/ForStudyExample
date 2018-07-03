import java.util.*

fun main(args: Array<String>) {
    val rollDice_ = {Random().nextInt(12)+1}

    val rollDice = { sides: Int ->
        Random().nextInt(sides) + 1
    }

    val rollDice0 = { sides : Int ->
        if(sides ==0) 0
        else Random().nextInt(sides)+1
    }
    val rollDice2: (Int) -> Int = {sides ->
        if(sides==0) 0
        else Random().nextInt(sides)+1
    }

    println(rollDice_)
    println(rollDice(2))
    println(rollDice0(5))
    println(rollDice2(10))

    gamePlay(rollDice2(20))
}

fun gamePlay(diceRoll: Int){
    println(diceRoll)
}
