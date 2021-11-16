# -*- coding: utf-8 -*-
import functools


def value_dispatch(func):
    """Like singledispatch() but dispatches by value of the first arg.
    Example:
      @value_dispatch
      def eat(fruit):
          return f"I don't want a {fruit}..."
      @eat.register('apple')
      def _eat_apple(fruit):
          return "I love apples!"
      @eat.register('eggplant')
      @eat.register('squash')
      def _eat_what(fruit):
          return f"I didn't know {fruit} is a fruit!"
    An alternative to applying multuple `register` decorators is to
    use the `register_for_all` helper:
      @eat.register_for_all({'eggplant', 'squash'})
      def _eat_what(fruit):
          return f"I didn't know {fruit} is a fruit!"
    """

    registry = {}

    @functools.wraps(func)
    def wrapper(arg0, *args, **kwargs):
        try:
            delegate = registry[arg0]
        except KeyError:
            pass
        else:
            return delegate(arg0, *args, **kwargs)

        return func(arg0, *args, **kwargs)

    def register(value):
        def wrap(func):
            if value in registry:
                raise ValueError(
                    f'@value_dispatch: there is already a handler '
                    f'registered for {value!r}'
                )
            registry[value] = func
            return func
        return wrap

    def register_for_all(values):
        def wrap(func):
            for value in values:
                if value in registry:
                    raise ValueError(
                        f'@value_dispatch: there is already a handler '
                        f'registered for {value!r}'
                    )
                registry[value] = func
            return func
        return wrap

    wrapper.register = register
    wrapper.register_for_all = register_for_all
    return wrapper
