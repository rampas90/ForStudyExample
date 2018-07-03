package Aquarium.Decoration

fun main(args: Array<String>) {
//    makeDecorations()

    println(Color.RED)
}
fun makeDecorations(){
    val d1 = Decoration("granite")
    println(d1)

    val d2 = Decoration("slate")
    println(d2)

    val d3 = Decoration("slate")
    println(d3)


    println(d1.equals(d2))
    println(d3.equals(d2))

    val d4 = d3.copy()
    println(d3)
    println(d4)

    println(d3.equals(d4))

    val d5 = Decoration2("Crystal","aaa","bbb")

    val (rock :String, wood: String, diver : String) = d5
    println(rock)
    println(wood)
    println(diver)
}
data class Decoration(val rocks : String){}

data  class Decoration2(val rocks: String , val wood : String, val diver : String){}

enum class Color(val rgb: Int) {
    RED(0xFF0000), GREEN(0x00FF00), BLUE(0x0000FF);
}