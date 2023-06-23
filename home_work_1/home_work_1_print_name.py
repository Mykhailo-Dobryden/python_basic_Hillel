from art import *

# ----------  first variant
print("Варіант 1: імʼя набране зірочками вручну: ", sep='\n')
print('                                               **')
print('*       *  *      *  *      *      *        *      *      *        ****')
print('* *   * *  *      *   *   *       *  *      *      *     *  *    *      *')
print('*   *   *  *    * *     *        ******     *    * *    *    *   *       *')
print('*       *  *  *   *    *  *     *       *   *  *   *   *      *   *     *')
print('*       *  **     *   *     *  *         *  **     *  *        *    ****')

# ---------- second variant
print("Варіант 2: імʼя надруковане артом: ")
mykhaylo2ascii = tprint("Micheal")
print(mykhaylo2ascii)

mykhaylo2ascii = tprint("Micheal", font="block")
print(mykhaylo2ascii)

mykhaylo2ascii = tprint("Micheal", space=10)
print(mykhaylo2ascii)
