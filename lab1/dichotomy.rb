def dichotomy_method(a, b, epsilon)
  # к-сть ітерацій
  i = 0
  loop do
    i += 1
    x = (a + b).fdiv 2
    fx = yield(x)
    break if fx == 0
    fa = yield(a)
    fb = yield(b)
    if fa * fx < 0
      b = x
    else
      a = x
    end
    break if (b - a).abs <= epsilon
  end
  x = (a + b).fdiv 2
  print "\t[#{i}]\t f(x) = #{yield(x)}  "
  (a + b).fdiv 2
end
