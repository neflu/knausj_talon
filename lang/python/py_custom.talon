-
tag(): user.python
#  tag() ...

#package <user.python_packages>:
#    text = python_packages
#    insert(python_packages)
#
#meth <user.pandas_functions>:
#    text = pandas_functions
#    insert(text)

package {user.python_packages}:
    txt = python_packages
    insert(txt)

# change to separate pd.Dataframe-like function
# and df.dropna() like functions
dos {user.pandas_functions} [<user.text>]:
  argument = text or ""
  txt = "pd." + pandas_functions
  insert(txt)
  key(left)
  insert(argument)
 # insert between ^? need variable # nows

meth {user.pandas_functions}:
    txt = pandas_functions
    insert(txt)

#! REGEX


