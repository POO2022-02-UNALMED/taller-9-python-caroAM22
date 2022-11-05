from tkinter import Tk, Button, Entry, Label

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("295x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=10, padx=1, pady=1)
label=Label(pantalla,width=40,height=2, bg="black", fg="white",borderwidth=0)
label.grid(row=0, column=0)
resultado=[0]
a,b=0,0

def operador(p):
    global resultado
    global a
    global b
    if p=="+":
        resultado=a+b
    elif p=="-":
        resultado=a-b
    elif p=="*":
        resultado=a*b
    elif p=="/" and b!=0:
        resultado=a/b
    
def operar():
    global resultado
    global a
    global b
    a=0
    b=0
    label.config(text=str(resultado))

def guardar(n):
    global a
    global b
    if a==0:
        a=n
    elif a!=0 and b==0:
        b=n

# Configuración botones
boton_1 = Button(root, text="1", command=lambda: guardar(1), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", command=lambda: guardar(2),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", command=lambda: guardar(3), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", command=lambda: guardar(4), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", command=lambda: guardar(5), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", command=lambda: guardar(6), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", command=lambda: guardar(7), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", command=lambda: guardar(8), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", command=lambda: guardar(9), width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", command=lambda: operar(), width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+",command=lambda: operador("+"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=4, padx=1, pady=1)
boton_menos = Button(root, text="-",command=lambda: operador("-"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=4, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  command=lambda: operador("*"),width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=4, padx=1, pady=1)
boton_division = Button(root, text="/", command=lambda: operador("/"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=4, padx=1, pady=1)

root.mainloop()