import math

def main():
    print("Let's find the roots of quadriatic equation ax**2+bx+c=0")

    def askvalue():
        print("enter A value different from 0:")
        val_A = int(input())
        print("enter B value:")
        val_B = int(input())
        print("enter C value:")
        val_C = int(input())
        print("Your values are:", "A =", val_A, "B =", val_B, "C =", val_C)

        def determinant():
            val_D = (val_B)**2 - 4*(val_A)*(val_C)
            print("Determinant is: ", val_D)

            def roots():
                if val_D < 0:
                    print("Your quadratic equation has no roots")
                elif val_D == 0:
                    root = -(val_B)/(2*val_A)
                    print("Your quadratic equation has only 1 root = ", "%.2f" % root)
                else:
                    root_1 = (-(val_B) + math.sqrt(val_D)) / (2 * val_A)
                    root_2 = (-(val_B) - math.sqrt(val_D)) / (2 * val_A)
                    print("Your quadratic equation has 2 roots: ", "root1 =", "%.2f" % root_1, "root2 =", "%.2f" % root_2)
            roots()
        determinant()
    askvalue()
main()