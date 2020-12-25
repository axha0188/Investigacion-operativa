from scipy.optimize import linprog
import os
def io():
    #============
    op = "1"
    #============
    while op == "1":
        z=[]
        r=[]
        cr=[]
        print("="*100)
        print("\t\t\t\tINVESTIGACION DE OPERACIONES")
        print("="*100)
        var = int(input("VARIABLES DE DECISION  QUE TIENE EL PROBLEMA: ")) 
        rec = int(input("RESTRICCIONES: "))
        print("="*100)
        print("FUNCION OBJETIVO")
        for i in range(var):
            vz= float(input("X{}: ".format(i+1)))
            z.append(vz)
        print("RESTRICCIONES \nINSERTE LOS COEFICIENTES DE Xn")
        for i in range(rec):
            r.append([])
            for j in range(var):
                vr = float(input("X({},{}): ".format((i+1),(j+1))))*-1
                r[i].append(vr)
        print("VALORES INDEPENDIENTES")
        for i in range(rec):
            vcr = float(input("C{}: ".format(i+1)))*-1
            cr.append(vcr)
#==============================================================================================================================
        print("="*100)
        print("VALORES INGRESADOS\nFUNCION OBJETIVO")
        print("Z = ",end=" ")
        for i in range(len(z)):
            print("{:.2f}X{} + ".format(z[i],i+1))
        print("COEFICIENTES DE LAS RESTRICCIONES")
        for i in r:
            print("[",end=" ")
            for j in i:
                print("{:5.2f}".format(j),end=" ")
            print("]")
        print("VALORES INDEPENDIENTES")
        for i in range(len(cr)):
            print("C{}: {:.2f}".format(i+1,cr[i]))
        input("PRESIONE UNA TECLA PARA CONTINUAR...")
#======================================================================================================================================
        print("PRE CALCULO REALIZADOS")
        res = linprog(z,r,cr,bounds=(0,None),method="interior-point")
#===================================================================================================================================
        print("="*100)
        print("SOLUCION")
        print("VALOR OPTIMO (FLOAT): ",(res.fun),"\nX: ",(res.x))
        print("="*100)
        print("VALOR OPTIMO (INT): {:.2f}".format(res.fun))
        for i in range(len(res.x)):
            print("X{}: {:.2f} ".format(i+1,res.x[i]))
#===================================================================================================================================        
        op = input("DESEA CONTINUAR (PRESS 1): ")
        os.system("cls")
    else:
        print("SESION FINALIZADA")

if __name__ == "__main__":
    io()