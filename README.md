_this is practical example from the [book](https://to.digital/typed-python)_

We will use hasbang at the entry point (`weather` file) to run our app without setting up an interpreter

First, we need to give `executable` access to the entry point:
```
chmod +x weather
```

Optionaly, We can create symlink and run our app from anywhere in system.
Call this in the root directory of your app:
```
sudo ln -s ${pwd}/weather /usr/local/bin/
```

**The main points of this book:**

`NamedTyple` is useful when you need a structure where you can get the value by name and also unpack it

`dataclass` allows you to create custom structures. if you add Frozen flag (which makes instances of this class immutable) and Slot flag (which adds __slot__ method for faster access to attributes), this structure will be more optimized than NamedTuple (which is handy when you don't need to unpack your values). You can test this with Python's `Pumpler` library.

`Iterable`, `Sequence`, `Mapping` are common data structures.
`Iterable` requires that passed data structure to be iterable (can be used in `for .. in` loop);
`Sequance` adds a requirement (in addition to iterability) to provide access to data by index;
`Mapping` is a data structure that privides access to data by key;

These common structures provide flexibility to the code. You can alse use generics and type aliases.

For functions you can use the `Callable` data structure which allows you to describe types of function's arguments and the type of return value.

It is also very useful to use static type checking tools such as `mypy`.
