# import example_pkg

# example_pkg.foo.foo_func()
# example_pkg.bar.bar_func()
# example_pkg.baz.baz_func()

# from example_pkg import foo, bar, baz

# foo.foo_func()
# bar.bar_func()
# baz.baz_func()

from example_pkg import foo as ex_foo
from example_pkg import bar as ex_bar
from example_pkg import baz as ex_baz

ex_foo.foo_func()
ex_bar.bar_func()
ex_baz.baz_func()