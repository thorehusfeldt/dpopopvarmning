fun main(args: Array<String>) {
  val words = if (args.size == 0) arrayOf("Hej", "verden!") else args
  System.`out`.println(words.joinToString(separator = " "))
}
