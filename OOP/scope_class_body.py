# The scope and namespace of the class's body.
# For methods inside of the class body does not work rule LEGB.
# To find a particular name which is presented inside of the class body,
# we have to find him via class or class instance.
# In other words here are some ways access to the class attributes.
# If we want to handle class attributes we have to handle them only via class object.
# If we handle it via instance it will create a new attribute for this instance and does not
# change a value of class attribute.
# Instance attributes should handle only via instance object and class attributes only via class. 

# PYTHON_DEV = 3
# GO_DEV = 2
# REACT_DEV = 4

class DepartmentIT:
    PYTHON_DEV = 3
    GO_DEV = 2
    REACT_DEV = 4

    def info_via_instance(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)

    def info_via_class(self):
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    @staticmethod
    def info_via_staticmethod():
        print(DepartmentIT.PYTHON_DEV, DepartmentIT.GO_DEV, DepartmentIT.REACT_DEV)

    @classmethod
    def info_via_classmethod(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @property
    def info_via_property(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)    

    def hire_a_developer_via_class(self):
        DepartmentIT.PYTHON_DEV += 1
    
    def hire_a_developer_via_instance(self):
        self.GO_DEV += 1


it_1 = DepartmentIT()
it_1.info_via_instance()
it_1.info_via_class()
it_1.info_via_staticmethod()
it_1.info_via_classmethod()
it_1.info_via_property
print()
print(it_1.hire_a_developer_via_class())
print(it_1.__dict__)
print(it_1.PYTHON_DEV)
print(DepartmentIT.PYTHON_DEV)
print()
print(it_1.hire_a_developer_via_instance())
print(it_1.__dict__)                            # here we see a new created instance attr
print(it_1.GO_DEV)                              # and here we get a value of this atrr
print(DepartmentIT.GO_DEV)
