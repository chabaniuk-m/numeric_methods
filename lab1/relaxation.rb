def relaxation_method(x_0, t, epsilon)
  # к-сть ітерацій
  i = 0
  x = x_0
  loop do
    prev = x
    x = t * yield(x) + x
    i += 1
    break if (x - prev).abs < epsilon
  end
  print "\t[#{i}]\t f(x) = #{yield(x)}  "
  x
end