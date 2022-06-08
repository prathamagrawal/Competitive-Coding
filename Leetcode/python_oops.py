class Employee:
    d = {}
    
    def __init__(self):
       self = self

    def put(self, key, value):
       self.d[key] = value
    
    def get(self, key):
        print(self.d.keys())
        return self.d[key]
    
    def remove(self, key):
        del self.d[key]

    def prints(self):
        print(self.d)
        


emp1 = Employee()
emp1.put("foo", "bar")
print(emp1.get("foo"))
emp1.remove("foo")
emp1.prints()