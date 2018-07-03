package Aquarium.generics

open class WaterSupply(var needsProcessed:Boolean)

class TapWater : WaterSupply(true) {
    fun addChemicalCleaners() {
        needsProcessed = false
    }
}

class fishStoreWater : WaterSupply(false)

class LakeWater : WaterSupply(true){
    fun fillter(){
        needsProcessed=false
    }
}


class Aquarium<T : WaterSupply>(val waterSupply :T){
    fun addWater(cleander : Cleaner<T>){
        if(waterSupply.needsProcessed){
            cleander.clean(waterSupply)
        }


        println("adding water from $waterSupply")
    }

    inline fun <reified R : WaterSupply> hasWaterSupplyOfType() = waterSupply is R

}

interface Cleaner<in T: WaterSupply>{
    fun clean(waterSupply: T)
}

class TapWaterCleaner : Cleaner<TapWater>{
    override fun clean(waterSupply: TapWater) {
        waterSupply.addChemicalCleaners()
    }
}

fun addItemTo(aquarium: Aquarium<WaterSupply>) = println("item added")

fun <T:WaterSupply> isWaterClean(aquarium : Aquarium<T>){
    println("auarium water is clean: ${aquarium.waterSupply.needsProcessed}")
}
fun genericExample(){
     val cleaner = TapWaterCleaner()
    val aquarium : Aquarium<TapWater> = Aquarium(TapWater())
    aquarium.addWater(cleaner)
    /*aquarium.waterSupply.addChemicalCleaners()

    val aquarium4 : Aquarium<LakeWater> = Aquarium(LakeWater())
    aquarium4.waterSupply.fillter()
    aquarium4.addWater()

    println(aquarium4)*/
}
