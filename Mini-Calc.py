#!/usr/bin/python3.2
 
from gi.repository import Gtk
 
mem = ''
mem_add = ''
mem_sub = ''
mem_mul = ''
mem_div = ''
intmem1 = ''
intmem2 = ''
 
class calc(Gtk.Window):
 
    def __init__(self): 
        Gtk.Window.__init__(self, title="Mini Calc")
        Gtk.Window.set_resizable(self, False)
         
        grid = Gtk.Grid()
        grid.set_column_spacing(2)
        grid.set_row_spacing(0)
        grid.set_column_homogeneous(self)
        self.add(grid)
 
        global display      
        display = Gtk.Entry()
        display.set_editable(False)
        display.set_alignment(1)
        display.set_max_length(10)
 
        global display2     
        display2 = Gtk.Entry()
        display2.set_editable(False)
        display2.set_alignment(1)
        display2.set_max_length(10)
 
        button_del = Gtk.Button(label="Clr")
        button_del.connect("clicked", self.clr_clicked)     
        button0 = Gtk.Button(label="0")
        button0.connect("clicked", self.b0_clicked)
        button1 = Gtk.Button(label="1")
        button1.connect("clicked", self.b1_clicked)
        button2 = Gtk.Button(label="2")
        button2.connect("clicked", self.b2_clicked)
        button3 = Gtk.Button(label="3")
        button3.connect("clicked", self.b3_clicked)
        button4 = Gtk.Button(label="4")
        button4.connect("clicked", self.b4_clicked)
        button5 = Gtk.Button(label="5")
        button5.connect("clicked", self.b5_clicked)
        button6 = Gtk.Button(label="6")
        button6.connect("clicked", self.b6_clicked)
        button7 = Gtk.Button(label="7")
        button7.connect("clicked", self.b7_clicked)
        button8 = Gtk.Button(label="8")
        button8.connect("clicked", self.b8_clicked)
        button9 = Gtk.Button(label="9")
        button9.connect("clicked", self.b9_clicked)
        button10 = Gtk.Button(label="+")
        button10.connect("clicked", self.b10_clicked)
        button11 = Gtk.Button(label="-")
        button11.connect("clicked", self.b11_clicked)
        button12 = Gtk.Button(label="*")
        button12.connect("clicked", self.b12_clicked)
        button13 = Gtk.Button(label="/")
        button13.connect("clicked", self.b13_clicked)
        button14 = Gtk.Button(label="=")
        button14.connect("clicked", self.b14_clicked)
 
        grid.attach(button_del, 0, 0, 6, 4)
        grid.attach_next_to(display, button_del, Gtk.PositionType.RIGHT, 26, 2)
        grid.attach_next_to(display2, display, Gtk.PositionType.BOTTOM, 26, 2)
        grid.attach(button7, 0, 4, 8, 4)
        grid.attach_next_to(button8, button7, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach_next_to(button9, button8, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach_next_to(button13, button9, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach(button4, 0, 8, 8, 4)
        grid.attach_next_to(button5, button4, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach_next_to(button12, button6, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach(button1, 0, 12, 8, 4)
        grid.attach_next_to(button2, button1, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach_next_to(button3, button2, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach_next_to(button11, button3, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach(button0, 0, 16, 16, 4)
        grid.attach_next_to(button14, button0, Gtk.PositionType.RIGHT, 8, 4)
        grid.attach_next_to(button10, button14, Gtk.PositionType.RIGHT, 8, 4)
         
    def b0_clicked(self, button0):
        global mem
        mem = mem + '0'
        display2.set_text(mem)
 
    def b1_clicked(self, button1):
        global mem
        mem = mem + '1'
        display2.set_text(mem)
 
    def b2_clicked(self, button2):
        global mem      
        mem = mem + '2'
        display2.set_text(mem)
 
    def b3_clicked(self, button3):
        global mem      
        mem = mem + '3'
        display2.set_text(mem)
     
    def b4_clicked(self, button4):
        global mem
        mem = mem + '4'
        display2.set_text(mem)
     
    def b5_clicked(self, button5):
        global mem
        mem = mem + '5'
        display2.set_text(mem)
     
    def b6_clicked(self, button6):
        global mem
        mem = mem + '6'
        display2.set_text(mem)
     
    def b7_clicked(self, button7):
        global mem
        mem = mem + '7'
        display2.set_text(mem)
     
    def b8_clicked(self, button8):
        global mem
        mem = mem + '8'
        display2.set_text(mem)
     
    def b9_clicked(self, button9):
        global mem
        mem = mem + '9'
        display2.set_text(mem)
     
    def b10_clicked(self, button10):
        global mem, mem_add     
        mem_add = mem
        display.set_text(mem_add)
        mem = ''
        display2.set_text('')
     
    def b11_clicked(self, button11):
        global mem, mem_sub
        mem_sub = mem
        display.set_text(mem_sub)
        mem = ''
        display2.set_text('')
     
    def b12_clicked(self, button12):
        global mem, mem_mul
        mem_mul = mem
        display.set_text(mem_mul)
        mem = ''
        display2.set_text('')
 
    def b13_clicked(self, button13):
        global mem, mem_div
        mem_div = mem
        display.set_text(mem_div)
        mem = ''
        display2.set_text('')
 
    def b14_clicked(self, button14):
        global mem, mem_add, mem_sub, mem_mul, mem_div, intmem1, intmem2
        if (mem_add != ''):
            intmem1 = float(mem_add)
            intmem2 = float(mem)
            intmem2 += intmem1
            mem = str(intmem2)
            display.set_text('')
            display2.set_text(mem)
            mem_add = ''
         
        elif (mem_sub != ''):
            intmem1 = float(mem_sub)
            intmem2 = float(mem)
            intmem2 = intmem1 - intmem2
            mem = str(intmem2)
            display.set_text('')
            display2.set_text(mem)
            mem_sub = ''
 
        elif (mem_mul != ''):
            intmem1 = float(mem_mul)
            intmem2 = float(mem)
            intmem2 *= intmem1
            mem = str(intmem2)
            display.set_text('')
            display2.set_text(mem)
            mem_mul = ''
 
        elif (mem_div != ''):
            intmem1 = float(mem_div)
            intmem2 = float(mem)
            intmem2 = intmem1/intmem2
            mem = str(intmem2)
            display.set_text('')
            display2.set_text(mem)
            mem_div = ''
 
    def clr_clicked(self, button_del):
        global mem, mem_add, mem_sub, mem_mul, mem_div
        display.set_text('')        
        display2.set_text('')
        mem = ''        
        mem_add = ''
        mem_sub = ''
        mem_mul = ''
        mem_div = ''
 
win = calc()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
