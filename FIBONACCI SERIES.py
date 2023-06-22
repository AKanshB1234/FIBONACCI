from tkinter import*
root = Tk()
root.geometry("500x600")
root.title("Fibonacci series")

t1 = Entry(root)
t1.pack()

l1= Label(root, text="Fibonacci series: ")
l1.pack()

l2 = Label(root)
l2.pack()

l3 = Label(root)
l3.pack()

def fibonacci():
    sum = 0
    first = 0
    second = 1
    count = 0
    un = t1.get()
    sum2 = 0
    while(count < int(un)):
        l1["text"] += str(sum) + " "
        l2["text"] = "Fibonacci sum: " + str(sum2)
        count = count + 1
        first = second
        second = sum
        sum = first + second
        sum2 = sum + sum2
        if(int(un) > 10):
            l3["text"] = "Flower is completely bloomed"
        else:
            l3["text"] = "Flower is partially bloomed"


b1 = Button(root, text="Show series", command=fibonacci)
b1.pack()

root.mainloop()