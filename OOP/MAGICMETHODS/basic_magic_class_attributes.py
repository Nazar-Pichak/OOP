
class BasicClassMagicAttributes:
    pass

print(dir(BasicClassMagicAttributes))
print()
object_1 = BasicClassMagicAttributes()
print(dir(object_1))

print(dir(BasicClassMagicAttributes) == dir(object_1))
print(BasicClassMagicAttributes is object_1)
print(id(BasicClassMagicAttributes), id(object_1))
print()

print(BasicClassMagicAttributes.__class__)
print(BasicClassMagicAttributes.__delattr__)
print(BasicClassMagicAttributes.__dict__)
print(BasicClassMagicAttributes.__dir__)
print(BasicClassMagicAttributes.__doc__)
print(BasicClassMagicAttributes.__eq__)
print(BasicClassMagicAttributes.__format__)
print(BasicClassMagicAttributes.__ge__)
print(BasicClassMagicAttributes.__getattribute__)
print(BasicClassMagicAttributes.__gt__)
print(BasicClassMagicAttributes.__hash__)
print(BasicClassMagicAttributes.__init__)
print(BasicClassMagicAttributes.__init_subclass__)
print(BasicClassMagicAttributes.__le__)
print(BasicClassMagicAttributes.__lt__)
print(BasicClassMagicAttributes.__module__)
print(BasicClassMagicAttributes.__ne__)
print(BasicClassMagicAttributes.__new__)
print(BasicClassMagicAttributes.__reduce__)
print(BasicClassMagicAttributes.__reduce_ex__)
print(BasicClassMagicAttributes.__repr__)
print(BasicClassMagicAttributes.__setattr__)
print(BasicClassMagicAttributes.__sizeof__)
print(BasicClassMagicAttributes.__str__)
print(BasicClassMagicAttributes.__subclasshook__)
print(BasicClassMagicAttributes.__weakref__)


