from numpy import array
import cmath          
                    x1 = (-b + cmath.sqrt(discriminante))/(2*a)
                    x2 = (-b - cmath.sqrt(discriminante))/(2*a)

                    mensaje = "Raíces complejas: x1 = " + f'{x1:.2f}' + ", x2 = " + f'{x2:.2f}'
                    MensaEcuaciones2doGrado.config(text=mensaje)
                    
                    informacion = array([x1, x2])
                    x = informacion.real
                    y = informacion.imag

                    figura = Figure()
                    subfigura = figura.add_subplot(111)
                    subfigura.plot(x, y, 'r.')
                    subfigura.set(xlabel = 'Reales', ylabel = 'Imaginarios', title = "Raíces complejas: x1 = " + str(x1) + ", x2 = " + str(x2))
                    subfigura.legend()
                    subfigura.grid()
                    subfigura.set_ylim(y_i,y_f)
                    canvas = FigureCanvasTkAgg (figura, master = ventanaEcuaciones2doGrado)
                    canvas.get_tk_widget().grid(row = 4, column = 0, padx = 5, pady = 5, sticky = "nsew", columnspan = 10)
                    canvas.draw()
                    toolbar = NavigationToolbar2Tk(canvas, ventanaEcuaciones2doGrado, pack_toolbar=False)
                    toolbar.grid(row=5, column=0, padx=5, pady=5, sticky="nsew", columnspan=8)   