package Aquarium

fun main(args: Array<String>) {
    buildAquarium()
}
fun buildAquarium(){
    val myAqualium= Aqualium()

    println("Length : ${myAqualium.length} \n" +
            "Width : ${myAqualium.width}\n"+
            "Height : ${myAqualium.width}\n"
    )

    println(myAqualium.volume)

    val simpleSpice = SimpleSpice()
    println("${simpleSpice.name} ${simpleSpice.heat}")


}