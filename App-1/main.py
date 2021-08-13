class Paint:

    def __init__(self, buckets, color):  # Or get house area and height
        self.color = color
        self.buckets = buckets

    def total_price(self):
        if self.color == "white":
            return self.buckets * 1.99
        else:
            return self.buckets * 2.19


class DiscountedPaint(Paint):

    def discounted_price(self, discount_percentage):
        price = self.total_price()
        discount = price * discount_percentage / 100
        return price - discount


testing = DiscountedPaint(float(input('Number of Paint buckets you need?: ')), input("Which color paint you need?: "))
print('Total Price: ', testing.total_price())
print('Discounted Price: ', testing.discounted_price(10))

