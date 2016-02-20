from string import Template

class MyTemplate(Template):
	delimiter = '#'

def Main():
	cart = []
	cart.append(dict(item="Pen", price=10, qty=5))
	cart.append(dict(item="Pencil", price=3, qty=2))
	cart.append(dict(item="Notebook", price=50, qty=1))

	t = MyTemplate("#item X #qty = #price")
	total = 0
	print ":::::My Cart:::::"
	for data in cart:
		print t.substitute(data)
		total += data["price"]
	print "Total: " + str(total)

if __name__ == "__main__":
	Main()
