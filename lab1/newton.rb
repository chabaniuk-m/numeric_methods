def newton_method(x_0, epsilon, f)
  # к-сть ітерацій
  i = 0
  x = x_0
  loop do
    i += 1
    prev = x
    x = x - f.call(x).fdiv(yield(x))
    break if (x - prev).abs < epsilon
  end
  x
  print "\t\t[#{i}]\t f(x) = #{f.call(x)}   | "
end
