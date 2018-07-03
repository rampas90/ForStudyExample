fun main(args: Array<String>) {
    delegate()
}
fun delegate(){
    val pleco = Plecostomus()
    println("Fish has color ${pleco.color}")
    pleco.eat()
}
interface FishAction{
    fun eat()
}
interface FishColor{
    val color : String
}
object GoldColor : FishColor{
    override val color = "gold"
}
class PrintingFishAction(val food: String): FishAction{
    override fun eat(){
        println(food)
    }
}

class Plecostomus(fishColor : FishColor = GoldColor):
        FishAction by PrintingFishAction("eat a log of algae"),
        FishColor by fishColor


abstract class Spice(val name:String, val spiciness:String = "mild",color: SpiceColor):
        SpiceColor by color{
    abstract  fun prepareSpice()
}

class Curry(name : String, spiciness:String,
            color : SpiceColor = YellowSpiceColor): Spice(name,spiciness,color),Grinder{
    override fun grind(){

    }
    override fun prepareSpice(){
        grind()
    }
}
interface Grinder{
    fun grind()
}
interface SpiceColor{
    val color: String
}
object YellowSpiceColor : SpiceColor{
    override  val color = "Yellow"
}