require './dichotomy.rb'
require './relaxation.rb'
require './newton.rb'


=begin
ПЕРША ЛАБА ЗДАНА - 100 % ✅
=end

# 0.5109..
f1 = lambda do |x|
  x + Math.sin(x) - 1
end
a1, b1 = 0, Math::PI / 2

# 1.15016
f2 = lambda do |x|
  x ** 3 - 3 * x ** 2 - 17 * x + 22
end
a2, b2 = 0, 2
t2 = 1.fdiv 19

df2 = lambda do |x|
  3 * x ** 2 - 6 * x - 17
end

# 0.65270
f3 = lambda do |x|
  x - 2.fdiv(111) *(x**3-10*x**2+44*x+29)
end
df3 = lambda do |x|
end
t3 = -2.fdiv 111

puts f3.call(-0.5)
puts f3.call(f3.call(-0.5))
puts f3.call(f3.call(f3.call(-0.5)))

print "Метод ділення навпіл: "
puts dichotomy_method(0, 1, 1e-4, &f3)

print "Метод релаксації: "
puts relaxation_method(-0.5, t3, 1e-4, &f3)

# print "Метод Ньютона: "
# puts newton_method(1, 1e-4, f3, &df3)
