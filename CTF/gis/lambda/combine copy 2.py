TRUE = lambda h:lambda i:h
FALSE = lambda h:lambda i:i
NOT = lambda h:h(FALSE)(TRUE)
PAIR = lambda h:lambda i:lambda j:j(h)(i)

print(
((
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda d:lambda e:(lambda f:(lambda g:g(TRUE))(f))(d)(lambda l:(TRUE))(lambda l:(TRUE(i)(FALSE))(
(lambda h:lambda i:(NOT)(
(TRUE(i(FALSE)(TRUE))(i(TRUE)(FALSE)))(h)(i)))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(d))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(e))) (a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(d))(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(e))))(TRUE)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(PAIR)(TRUE)(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(TRUE))(FALSE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(
(lambda h:lambda i:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda h:lambda i:lambda j:(lambda f:(lambda g:g(TRUE))(f))(h)(lambda l:(
(PAIR)(TRUE)(TRUE)))(lambda l:(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(h))(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(i))( (lambda h:lambda i:lambda j:(TRUE(TRUE)(i))(
(TRUE(i)(FALSE))(
(TRUE(i(FALSE)(TRUE))(i(TRUE)(FALSE)))(h)(i))(j))(
(TRUE(i)(FALSE))(h)(i)))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(h))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(i))(j) ))( (lambda h:lambda i:lambda j:(TRUE(i(FALSE)(TRUE))(i(TRUE)(FALSE)))(h)(
(TRUE(i(FALSE)(TRUE))(i(TRUE)(FALSE)))(i)(j)))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(h))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(i))(j) ))(TRUE))))(
(lambda i:lambda k:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda i:lambda k:(lambda h:h(lambda l:(FALSE))(TRUE))(k)(lambda l:i)(lambda l:a(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda f:lambda b:(lambda f:(lambda g:g(TRUE))(f))(f)(lambda l:(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(f)(b))(lambda l:(PAIR)(FALSE)(
(PAIR)(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(f))(a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(f))(b))))(TRUE)))(i)(FALSE))(
(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(k)))(TRUE))))(i)(
(FALSE(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(h))(k)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(i))))(h)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(i)))(
(lambda i:lambda k:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda i:lambda k:(lambda h:h(lambda l:(FALSE))(TRUE))(k)(lambda l:i)(lambda l:a(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda f:lambda b:(lambda f:(lambda g:g(TRUE))(f))(f)(lambda l:(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(f)(b))(lambda l:(PAIR)(FALSE)(
(PAIR)(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(f))(a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(f))(b))))(TRUE)))(i)(FALSE))(
(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(k)))(TRUE))))(i)(
(FALSE(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(h))(k)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(i))))(i)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(h)))(FALSE))(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda h:lambda i:(lambda f:(lambda g:g(TRUE))(f))(i)(lambda l:(
(PAIR)(TRUE)(TRUE)))(lambda l:(lambda h:lambda i:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda h:lambda i:lambda j:(lambda f:(lambda g:g(TRUE))(f))(h)(lambda l:(
(PAIR)(TRUE)(TRUE)))(lambda l:(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(h))(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(i))( (lambda h:lambda i:lambda j:(TRUE(TRUE)(i))(
(TRUE(i)(FALSE))(
(TRUE(i(FALSE)(TRUE))(i(TRUE)(FALSE)))(h)(i))(j))(
(TRUE(i)(FALSE))(h)(i)))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(h))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(i))(j) ))( (lambda h:lambda i:lambda j:(TRUE(i(FALSE)(TRUE))(i(TRUE)(FALSE)))(h)(
(TRUE(i(FALSE)(TRUE))(i(TRUE)(FALSE)))(i)(j)))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(h))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(i))(j) ))(TRUE))))(
(lambda i:lambda k:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda i:lambda k:(lambda h:h(lambda l:(FALSE))(TRUE))(k)(lambda l:i)(lambda l:a(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda f:lambda b:(lambda f:(lambda g:g(TRUE))(f))(f)(lambda l:(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(f)(b))(lambda l:(PAIR)(FALSE)(
(PAIR)(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(f))(a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(f))(b))))(TRUE)))(i)(FALSE))(
(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(k)))(TRUE))))(i)(
(FALSE(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(h))(k)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(i))))(h)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(i)))(
(lambda i:lambda k:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda i:lambda k:(lambda h:h(lambda l:(FALSE))(TRUE))(k)(lambda l:i)(lambda l:a(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda f:lambda b:(lambda f:(lambda g:g(TRUE))(f))(f)(lambda l:(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(f)(b))(lambda l:(PAIR)(FALSE)(
(PAIR)(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(f))(a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(f))(b))))(TRUE)))(i)(FALSE))(
(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(k)))(TRUE))))(i)(
(FALSE(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(h))(k)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(i))))(i)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(h)))(FALSE))(
(lambda h:lambda i:(i(h)(
(lambda i:lambda k:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda i:lambda k:(lambda h:h(lambda l:(FALSE))(TRUE))(k)(lambda l:i)(lambda l:a(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda f:lambda b:(lambda f:(lambda g:g(TRUE))(f))(f)(lambda l:(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(f)(b))(lambda l:(PAIR)(FALSE)(
(PAIR)(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(f))(a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(f))(b))))(TRUE)))(i)(FALSE))(
(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(k)))(TRUE))))(i)(
(FALSE(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(h))(k)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(i))))(
(PAIR)(TRUE)(TRUE))(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(h)))))(h)(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(i)))( (lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(a(h)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(i)))(FALSE) ) )(TRUE))))(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda inputVar:(
((
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda d:lambda e:(lambda f:(lambda g:g(TRUE))(f))(d)(lambda l:e)(lambda l:(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(d))(e))(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(d)))(TRUE))))(a(inputVar[1:]))(
(lambda i:lambda k:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda i:lambda k:(lambda h:h(lambda l:(FALSE))(TRUE))(k)(lambda l:i)(lambda l:a(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda f:lambda b:(lambda f:(lambda g:g(TRUE))(f))(f)(lambda l:(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(f)(b))(lambda l:(PAIR)(FALSE)(
(PAIR)(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(f))(a(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(f))(b))))(TRUE)))(i)(FALSE))(
(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(k)))(TRUE))))(i)(
(FALSE(lambda k:lambda a:lambda b:k(lambda m:lambda n:n(m(a)))(lambda l:b)(lambda h:h))(h))(k)(
(lambda n:(
(lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:lambda o:lambda n:lambda p:(lambda f:(lambda g:g(TRUE))(f))(n)(lambda l:p)(lambda l:a(o)(
(lambda f:(lambda g:g(FALSE))(
(lambda g:g(FALSE))(f)))(n))(o(
(lambda f:(lambda g:g(TRUE))(
(lambda g:g(FALSE))(f)))(n))(p)))(TRUE)))(lambda b:lambda k:(lambda k:TRUE(k(h)(i)))(k))(n)(FALSE))(i))))(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda k:(
((lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(a(k>>1)) (
(NOT)(
(lambda h:h(lambda l:(FALSE))(TRUE))(
((lambda a:(
(lambda b:a(lambda c:b(b)(c)))(lambda b:a(lambda c:b(b)(c)))))(lambda a:(lambda k:(
((lambda k:TRUE(k(h)(i)))(a(k-1))) if k else (FALSE)))))(k%2))) )) if k else (
(PAIR)(TRUE)(TRUE))))))(inputVar[0]))(
(lambda h:lambda i:lambda j:h(i(j)))(
(lambda k:TRUE(k(h)(i)))(TRUE(h(h(i)))))(TRUE(h(i)))))) if len(inputVar) else (
(PAIR)(TRUE)(TRUE))))))(input("> ").encode()))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(PAIR)(TRUE)(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(lambda f:lambda b:(PAIR)(FALSE)(
(PAIR)(b)(f)))(
(PAIR)(TRUE)(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(FALSE))(TRUE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(FALSE))(TRUE))(TRUE))(TRUE))(FALSE))(TRUE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(FALSE))(TRUE))))("lambda!")("lambda..."))
